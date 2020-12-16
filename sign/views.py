from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "index.html")


# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '') #对应form表单中的<input>标签的name属性
        password = request.POST.get('password', '')
        '''
        if username == 'admin' and password == 'admin123':
            # return HttpResponse('login success!')

            # return HttpResponseRedirect('/event_manage/')            
        '''
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) # 登录

            request.session['user'] = username  # 将session信息记录到浏览器

            # response.set_cookie('user', username, 3600) # 添加浏览器cookie,保持时间3600秒
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error':'username or password error!'}) # 返回错误提示的字典

# 发布会管理
@login_required
def event_manage(request):
    # return render(request, "event_manage.html")

    # username = request.COOKIES.get('user', '') # 读取浏览器cookie
    username = request.session.get('user', '') # 读取浏览器session
    return render(request, "event_manage.html", {"user" : username})