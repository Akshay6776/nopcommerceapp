import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login_Page
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utelities.customlogger import LogGen
from utelities.readProperties import ReadConfig


class Test_001_Login:
    base_url = ReadConfig.getApplicationurl()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()

    log=LogGen.getLogger()

    @pytest.mark.regression
    def test_homepageTitle(self,setup):
        log=self.log.info('**********************  Test_001_Login  **************')
        log=self.log.info('**********************  Verify HomePage Title  **************')

        self.driver=setup
        self.driver.get(self.base_url)
        act_title=self.driver.title
        self.driver.close()

        if act_title=='Your store. Login':
            assert True
            log=self.log.info('**********************  HomePage Title test Passed  **************')
        else:
            log=self.log.error('**********************  HomePage Title test Failed  **************')
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        log=self.log.info('********************  verifying the Log In test  ********************')
        self.driver=setup
        self.driver.get(self.base_url)
        self.lp=Login_Page(self.driver)
        self.lp.enter_email(self.email)
        self.lp.enter_password(self.password)
        self.lp.click_log_in()
        act_title=self.driver.title

        if act_title=='Dashboard / nopCommerce administration':
            assert True
            log=self.log.info('**********************  Loggin test Passed  **************')
            self.driver.close()

        else:
            self.driver.save_screenshot('C:\\akshay python projects\\nopcommerceApp\\Screenshots\\test_login.png')
            self.driver.close()
            log=self.log.error('**********************  Loggin test Failed  **************')
            assert False

