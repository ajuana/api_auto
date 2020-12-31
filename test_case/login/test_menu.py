# coding=gbk
# 获取菜单接口
import requests
from common.get_headers import get_header
from common.get_token import get_tokens
from common.get_user import get_user
from config.conf import get_url
url=get_url()+'/cgi/oryx/admin/user/menu'
res=requests.get(url=url,cookies=get_tokens())
print(res.text)