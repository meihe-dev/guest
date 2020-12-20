from django.contrib import auth as django_auth
from django.http import JsonResponse
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import base64
import time, hashlib
from sign.models import Event


# 用户认证
def user_auth(request):
    # request.META是一个Python字典，包含了本次HTTP请求的Header信息，例如用户认证、IP地址和用户Agent（通常是浏览器的名称和版本号）等。
    # HTTP_AUTHORIZATION用于获取HTTP认证数据，如果为空，将得到一个空的bytes对象。
    get_http_auth = request.META.get('HTTP_AUTHORIZATION', b'')
    auth = get_http_auth.split()
    try:
        auth_parts = base64.b64decode(auth[1]).decode('utf-8').partition(':')
    except IndexError:
        return 'null'
    username, password = auth_parts[0], auth_parts[2]
    user = django_auth.authenticate(username=username, password=password)
    if user is not None:
        django_auth.login(request, user)
        return 'success'
    else:
        return 'fail'

# 查询发布会接口--增加用户认证
def sec_get_event_list(request):
    auth_result = user_auth(request) # 调用认证函数
    if auth_result == 'null':
        return JsonResponse({'status':10011, 'message':'user auth null'})

    if auth_result == 'fail':
        return JsonResponse({'status':10012, 'message':'user auth fail'})

    eid = request.GET.get('eid', '')
    name = request.GET.get('name', '')

    if eid == '' and name == '':
        return JsonResponse({'status':10021, 'message':'parameter error'})

    if eid != '':
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'query result is empty'})
        else:
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status':200, 'message':'success', 'data':event})

    if name != '':
        datas = []
        results = Event.objects.filter(name__contains=name)
        if results:
            for result in results:
                event = {}
                event['name'] = result.name
                event['limit'] = result.limit
                event['status'] = result.status
                event['address'] = result.address
                event['start_time'] = result.start_time
                datas.append(event)
            return JsonResponse({'status':200, 'message':'success', 'data':datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})

# 签名 + 时间戳
def user_sign(request):
    if request.method == 'POST':
        client_time = request.POST.get('time', '') # 客户端时间戳
        client_sign = request.POST.get('sign', '') # 客户端签名
    else:
        return 'error'

    if client_time == '' or client_sign == '':
        return 'sign null'

    # 服务器时间
    now_time = time.time() # 例如：1608288688
    server_time = str(now_time).split('.')[0]
    # 获取时间差
    time_difference = int(server_time) - int(client_time)
    if time_difference >= 60:
        return 'timeout'

    # 签名检查
    md5 = hashlib.md5()
    sign_str = client_time + '&Guest-Bugmaster'
    sign_bytes_utf8 = sign_str.encode(encoding='utf-8')
    md5.update(sign_bytes_utf8)
    server_sign = md5.hexdigest()

    if server_sign != client_sign:
        return 'sign fail'
    else:
        return 'sign success'

# 添加发布会接口--增加签名+时间戳
def sec_add_event(request):
    sign_result = user_sign(request)
    if sign_result == 'error':
        return JsonResponse({'status':10011, 'message':'request error'})
    elif sign_result == 'sign null':
        return JsonResponse({'status':10012, 'message':'user sign null'})
    elif sign_result == 'timeout':
        return JsonResponse({'status':10013, 'message':'user sign timeout'})
    elif sign_result == 'sign fail':
        return JsonResponse({'status':10014, 'message':'user sign error'})
    elif sign_result == 'sign success':
        eid = request.POST.get('eid', '')
        name = request.POST.get('name', '')
        limit = request.POST.get('limit', '')
        status = request.POST.get('status', '')
        address = request.POST.get('address', '')
        start_time = request.POST.get('start_time', '')

        if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
            return JsonResponse({'status': 10021, 'message': 'parameter error'})

        result = Event.objects.filter(id=eid)
        if result:
            return JsonResponse({'status': 10022, 'message': 'event id already exists'})

        result = Event.objects.filter(name=name)
        if result:
            return JsonResponse({'status': 10023, 'message': 'event name already exists'})

        if status == '':
            status = 1

        try:
            Event.objects.create(id=eid, name=name, limit=limit, address=address, status=int(status),
                                 start_time=start_time)
        except ValidationError as e:
            error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
            return JsonResponse({'status': 10024, 'message': error})

        return JsonResponse({'status': 200, 'message': 'add event success'})