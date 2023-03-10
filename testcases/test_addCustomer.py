import random
import string
import time

import pytest
from pageObjects.AddcustomerPage import AddCustomerPage
from pageObjects.LoginPage import Login_Page
from selenium.webdriver.common.by import By
from utelities.customlogger import LogGen
from utelities.readProperties import ReadConfig


class Test_003_AddCustomer:
    base_url = ReadConfig.getApplicationurl()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    log=LogGen.getLogger()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.log.info('***********  Test_003_AddCustomer  ***********')
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.lp=Login_Page(self.driver)
        self.lp.enter_email(self.email)
        self.lp.enter_password(self.password)
        self.lp.click_log_in()
        self.log.info('**********************  Loggin successfull  **************')

        self.log.info('**********************  Start add customer test  **************')

        self.add_customer=AddCustomerPage(self.driver)
        self.add_customer.click_Customers()
        time.sleep(2)
        self.add_customer.click_sub_Customers()
        self.add_customer.click_add_new()

        self.log.info('**************  Providing customer info  **************')
        self.email=random_generater() + '@gmail.com'
        self.add_customer.enter_email(self.email)
        self.add_customer.enter_password('Test003')
        self.add_customer.enter_first_name('Akshay')
        self.add_customer.enter_last_name('Jangamshetty')
        self.add_customer.select_gender('Male')
        self.add_customer.enter_DOB('12/8/1995')
        self.add_customer.enter_company_name('busyQ&A')
        self.add_customer.enter_Customer_roles('Guests')
        self.add_customer.select_Manager_of_Vender('Vendor 2')
        self.add_customer.click_save()
        self.log.info('*******************  customer info added and saved ******************')

        self.log.info('*******************  customer added info validation starts  *****************')

        self.msg=self.add_customer.alert_message()
        self.log.info('final allert message is'+self.msg)

        if 'The new customer has been added successfully.' in self.msg:
            assert True==True
        else:
            self.driver.save_screenshot('C:\\akshay python projects\\nopcommerceApp\\Screenshots\\test_addcustomer.png')
            self.log.error('*******************  customer added test Failed  *****************')
            assert False==False

        self.driver.close()
        self.log.info('************* End of customer adding test  **************')


def random_generater(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


