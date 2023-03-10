import random
import string
import time

import pytest
from pageObjects.AddcustomerPage import AddCustomerPage
from pageObjects.LoginPage import Login_Page
from pageObjects.searchCustomerPage import SecrchCustomerPage
from selenium.webdriver.common.by import By
from utelities.customlogger import LogGen
from utelities.readProperties import ReadConfig


class Test_005_Search_Customer_by_Name:
    base_url = ReadConfig.getApplicationurl()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    log=LogGen.getLogger()

    @pytest.mark.regression
    def test_searchCustomer_by_name(self,setup):
        self.log.info('***********  Test_005_Search_Customer_by_Name  ***********')
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.lp=Login_Page(self.driver)
        self.lp.enter_email(self.email)
        self.lp.enter_password(self.password)
        self.lp.click_log_in()
        self.log.info('**********************  Loggin successfull  **************')

        self.add_customer=AddCustomerPage(self.driver)
        self.add_customer.click_Customers()
        time.sleep(2)
        self.add_customer.click_sub_Customers()
        self.log.info('**********************  Start search customer by name test  **************')

        self.search=SecrchCustomerPage(self.driver)
        self.search.Enter_first_name('Victoria')
        self.search.Enter_last_name('Terces')
        self.search.click_search()
        time.sleep(2)
        status=self.search.search_by_name('Victoria Terces')
        assert True==status
        self.log.info('**********************  search customer test finist **************')
        self.driver.close()