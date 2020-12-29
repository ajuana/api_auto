# coding=gbk
# ��½�ӿ�
import requests
import json
from common.get_headers import get_header
from common.get_user import get_user
from config.conf import get_url
# ��½�ӿ�
url=get_url()+'/cgi/oryx/admin/user/login'
res=requests.post(url=url,json=get_user(),headers=get_header())
token=res.json()['data']['token']
with open("../../common/token.scv", "w") as fp:
    json.dump(token, fp)
print(res.json()['data'].get('token'))