# coding=gbk
# 登陆接口
import requests
import json
from common.get_headers import get_header
from common.get_user import get_user
from config.conf import get_url
# 登陆接口
url=get_url()+'/cgi/oryx/admin/user/login'
res=requests.post(url=url,json=get_user(),headers=get_header())
token=res.json()['data']['token']
with open("../../common/token.scv", "w") as fp:
    json.dump(token, fp)
print(res.json()['data'].get('token'))