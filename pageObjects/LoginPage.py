from selenium.webdriver.common.by import By


class Login_Page:

    def __init__(self,driver):
        self.driver=driver

    Email=(By.XPATH,'//input[@id="Email"]')
    Password=(By.XPATH,'//input[@id="Password"]')
    Log_in=(By.XPATH,'//button[normalize-space()="Log in"]')
    Log_out=(By.XPATH,'//a[normalize-space()="Logout"]')


    def enter_email(self,email):
        self.driver.find_element(*Login_Page.Email).clear()
        return self.driver.find_element(*Login_Page.Email).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(*Login_Page.Password).clear()
        return self.driver.find_element(*Login_Page.Password).send_keys(password)

    def click_log_in(self):
        return self.driver.find_element(*Login_Page.Log_in).click()

    def click_log_out(self):
        return self.driver.find_element(*Login_Page.Log_out).click()
