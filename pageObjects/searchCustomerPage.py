from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SecrchCustomerPage:

    def __init__(self,driver):
        self.driver=driver

    Email=(By.XPATH,'//input[@id="SearchEmail"]')
    First_name=(By.XPATH,'//input[@id="SearchFirstName"]')
    Last_name=(By.XPATH,'//input[@id="SearchLastName"]')
    Search=(By.XPATH,'//button[@id="search-customers"]')
    # Search_table=(By.XPATH,'(//table[@class="table table-bordered table-hover table-striped dataTable no-footer"])[1]')
    Table=(By.XPATH,'//table[@id="customers-grid"]')
    table_rows=(By.XPATH,'//*[@id="customers-grid"]/tbody/tr')
    table_columns=(By.XPATH,'//*[@id="customers-grid"]/tbody/tr/td')


    def Enter_search_email(self,email):
        self.driver.find_element(*SecrchCustomerPage.Email).clear()
        return self.driver.find_element(*SecrchCustomerPage.Email).send_keys(email)

    def Enter_first_name(self,first_name):
        self.driver.find_element(*SecrchCustomerPage.Email).clear()
        return self.driver.find_element(*SecrchCustomerPage.First_name).send_keys(first_name)

    def Enter_last_name(self,last_name):
        self.driver.find_element(*SecrchCustomerPage.Email).clear()
        return self.driver.find_element(*SecrchCustomerPage.Last_name).send_keys(last_name)

    def click_search(self):
        return self.driver.find_element(*SecrchCustomerPage.Search).click()

    def get_no_of_rows(self):
        return len(self.driver.find_elements(*SecrchCustomerPage.table_rows))

    def search_by_email(self,email):
        flag=False
        for r in range(1,self.get_no_of_rows()+1):
            table=self.driver.find_element(*SecrchCustomerPage.Table)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="customers-grid"]/tbody/tr['+str(r)+']/td[2]')))
            Email_id=table.find_element(By.XPATH,'//*[@id="customers-grid"]/tbody/tr['+str(r)+']/td[2]').text
            if Email_id==email:
                flag=True
                break;
        return flag

    def search_by_name(self,name):
        flag=False
        for r in range(1,self.get_no_of_rows()+1):
            table=self.driver.find_element(*SecrchCustomerPage.Table)
            Name=table.find_element(By.XPATH,'//*[@id="customers-grid"]/tbody/tr['+str(r)+']/td[3]').text
            if Name==name:
                flag=True
                break;
        return flag
