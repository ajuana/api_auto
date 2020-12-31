# coding=gbk
# 获取首页概况
import requests
from common.get_headers import get_header
from common.get_token import get_tokens
from common.get_user import get_user
from config.conf import get_url

url_list=get_url()+'/cgi/oryx/admin/download/center/list'
# 获取常用功能接口
url_functions=get_url()+'/cgi/oryx/admin/home/common/functions'
# 获取商城信息接口
url_info=get_url()+'/cgi/oryx/admin/home/service/version/info'
# 获取公告接口
url_home=get_url()+'/admin/notice/business/home'
Params = {
    "page": 1,
    "num": 5
}
res_list=requests.get(url=url_list,cookies=get_tokens(),params=Params)
res_functions=requests.get(url=url_functions,cookies=get_tokens())
res_info=requests.get(url=url_info,cookies=get_tokens())
res_home=requests.get(url=url_home,cookies=get_tokens())
print(res_list.text)
print(res_functions.text)