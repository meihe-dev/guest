import requests

# 查询发布会接口
url = 'http://127.0.0.1:8000/api/get_event_list'
r = requests.get(url, params={'eid':'1'})
result = r.json()

# 断言接口返回值
assert result['status'] == 200
assert result['message'] == 'success'
assert result['data']['name'] == '小米V发布会'
assert result['data']['address'] == '水立方'
assert result['data']['start_time'] == '2021-01-01T06:00:00'