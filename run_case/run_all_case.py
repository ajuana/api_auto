import pytest
import allure
import os
if __name__ == '__main__':
    # pytest.main(['../test_case/test_case_01.py','--alluredir'])
    pytest.main(['../test_case/login/test_login.py','../test_case/login/test_getinfo.py','--alluredir','../report/','--clean-alluredir'])
    os.system('allure generate ./temp -o ../report --clean')