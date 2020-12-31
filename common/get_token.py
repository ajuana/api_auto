def get_tokens():
    cookies = ""
    dict={}
    with open("../../common/token.scv", "r") as f:
        for line in f:
            cookies = line
    dict['JSESSIONID']=eval(cookies)
    print(dict)
    print(type(dict))
    return dict