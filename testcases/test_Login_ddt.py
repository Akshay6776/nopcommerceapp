import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login_Page
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utelities.customlogger import LogGen
from utelities.readProperties import ReadConfig
from utelities import Excelutility



class Test_002_DDT_Login:
    base_url = ReadConfig.getApplicationurl()
    path="C:\\akshay python projects\\nopcommerceApp\\TestData\\LoginData.xlsx"

    log=LogGen.getLogger()

    @pytest.mark.regression
    def test_login_DDT(self,setup):
        log=self.log.info('********************  Test_002_DDT_Login  ********************')
        log=self.log.info('********************  verifying the Log In DDT test  ********************')
        self.driver=setup
        self.driver.get(self.base_url)
        self.lp=Login_Page(self.driver)
        self.rows=Excelutility.get_rowcount(self.path,'Sheet1')

        list_status=[]
        self.act=ActionChains(self.driver)

        for r in range(2,self.rows+1):
            self.email=Excelutility.readData(self.path,'Sheet1',r,1)
            self.password=Excelutility.readData(self.path,'Sheet1',r,2)
            self.exp=Excelutility.readData(self.path,'Sheet1',r,3)

            self.lp.enter_email(self.email)
            self.lp.enter_password(self.password)
            self.lp.click_log_in()
            time.sleep(2)

            act_title = self.driver.title
            exp_title='Dashboard / nopCommerce administration'

            if act_title==exp_title:
                if self.exp=='Pass':
                    log=self.log.info('**********  Passed  ***********')
                    self.lp.click_log_out();
                    list_status.append('pass')
                elif self.exp=='Fail':
                    log=self.log.info('**********  Failed  ***********')
                    self.lp.click_log_out();
                    list_status.append('Fail')

            if act_title != exp_title:
                if self.exp=='Pass':
                    log=self.log.info('**********  Failed  ***********')
                    list_status.append('Fail')
                elif self.exp=='Fail':
                    log=self.log.info('**********  Passed  ***********')
                    list_status.append('Pass')

        if 'Fail' not in list_status:
            log = self.log.info('***********  Login DDt Passed  **********')
            self.driver.close()
            assert True
        else:
            log = self.log.info('***********  Login DDt Failed  **********')
            self.driver.close()
            assert False

        log=self.log.info('********************  End of Loging ddt test case  ********************')
        log=self.log.info('********************  completed Test_002_DDT_Login  ********************')