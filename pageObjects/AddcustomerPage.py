import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddCustomerPage:

    def __init__(self,driver):
        self.driver=driver

    Customers=(By.XPATH,'//a[@href="#"]//p[contains(text(),"Customers")]')
    Sub_customers=(By.XPATH,'//a[@href="/Admin/Customer/List"]//p[contains(text(),"Customers")]')
    Add_new=(By.XPATH,'//a[normalize-space()="Add new"]')
    Email=(By.XPATH,'//input[@id="Email"]')
    Password=(By.XPATH,'//input[@id="Password"]')
    First_name=(By.XPATH,'//input[@id="FirstName"]')
    Last_name=(By.XPATH,'//input[@id="LastName"]')
    Male_rad_button=(By.XPATH,'//input[@id="Gender_Male"]')
    Female_rad_button=(By.XPATH,'//input[@id="Gender_Female"]')
    DOB=(By.XPATH,'//input[@id="DateOfBirth"]')
    Company_name=(By.XPATH,'//input[@id="Company"]')
    News_letter=(By.XPATH,'//div[@class="k-widget k-multiselect k-multiselect-clearable k-state-focused k-state-border-down"]//div[@role="listbox"]')
    NL_List_item_your_store_name=(By.XPATH,"//li[contains(.,'Your store name')]")
    NL_List_item_Test_store_2=(By.XPATH,'//li[normalize-space()="Test store 2"]')
    Customer_Roles=(By.XPATH,'//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div')
    CR_List_item_Administrators=(By.XPATH,'//li[normalize-space()="Administrators"]')
    CR_List_item_Forum_Moderators=(By.XPATH,'//li[normalize-space()="Forum Moderators"]')
    CR_List_item_Guests=(By.XPATH,'//li[normalize-space()="Guests"]')
    CR_List_item_Registered=(By.XPATH,'//li[normalize-space()="Registered"]')
    CR_List_item_Vendors=(By.XPATH,'//li[contains(text(),"Vendors")]')
    Manager_of_Vender=(By.XPATH,'//select[@id="VendorId"]')
    Activ_Checkbox=(By.XPATH,'//input[@id="Active"]')
    Save=(By.XPATH,'//button[@name="save"]')
    alert_msg=(By.XPATH,'//div[@class="alert alert-success alert-dismissable"]')

    def click_Customers(self):
        element=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.Customers))
        return self.driver.execute_script("arguments[0].click();",element)

        # return self.driver.find_element(*AddCustomerPage.Customers).click()

    def click_sub_Customers(self):
        return self.driver.find_element(*AddCustomerPage.Sub_customers).click()

    def click_add_new(self):
        return self.driver.find_element(*AddCustomerPage.Add_new).click()

    def enter_email(self,email):
        return self.driver.find_element(*AddCustomerPage.Email).send_keys(email)

    def enter_password(self,password):
        return self.driver.find_element(*AddCustomerPage.Password).send_keys(password)

    def enter_first_name(self,first_name):
        return self.driver.find_element(*AddCustomerPage.First_name).send_keys(first_name)

    def enter_last_name(self,last_name):
        return self.driver.find_element(*AddCustomerPage.Last_name).send_keys(last_name)

    def select_gender(self,gender):
        if gender=='Male':
            self.driver.find_element(*AddCustomerPage.Male_rad_button).click()
        elif gender=='Female':
            self.driver.find_element(*AddCustomerPage.Female_rad_button).click()
        else:
            self.driver.find_element(*AddCustomerPage.Male_rad_button).click()

    def enter_DOB(self,date):
        return self.driver.find_element(*AddCustomerPage.DOB).send_keys(date)

    def enter_company_name(self,company_name):
        return self.driver.find_element(*AddCustomerPage.Company_name).send_keys(company_name)

    def click_news_letter(self):
        return self.driver.find_element(*AddCustomerPage.News_letter).click()

    def click_NL_your_store_name(self):
        return self.driver.find_element(*AddCustomerPage.NL_List_item_your_store_name).click()

    def click_NL_Test_store_2(self):
        return self.driver.find_element(*AddCustomerPage.NL_List_item_Test_store_2).click()

    def enter_Customer_roles(self,role):
        self.driver.find_element(*AddCustomerPage.Customer_Roles).click()
        time.sleep(2)
        if role=='Administrators':
            self.list_item=self.driver.find_element(*AddCustomerPage.CR_List_item_Administrators).click()
        elif role=='Forum_Moderators':
            self.list_item=self.driver.find_element(*AddCustomerPage.CR_List_item_Forum_Moderators).click()
        elif role=='Guests':
            #customer cannot be Registered and Guest at the same time
            self.driver.find_element(By.XPATH,'//*[@id="SelectedCustomerRoleIds_taglist"]/li[1]/span[2]').click()
            self.list_item=self.driver.find_element(*AddCustomerPage.CR_List_item_Guests).click()
        elif role=='Registered':
            self.list_item=self.driver.find_element(*AddCustomerPage.CR_List_item_Registered).click()
        elif role=='Vendors':
            self.list_item=self.driver.find_element(*AddCustomerPage.CR_List_item_Vendors).click()
        else:
            self.list_item=self.driver.find_element(*AddCustomerPage.CR_List_item_Guests).click()
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",self.list_item)
        return self.list_item

    def select_Manager_of_Vender(self,value):
        drp=Select(self.driver.find_element(*AddCustomerPage.Manager_of_Vender))
        return drp.select_by_visible_text(value)

    def click_save(self):
        return self.driver.find_element(*AddCustomerPage.Save).click()

    def alert_message(self):
        return self.driver.find_element(*AddCustomerPage.alert_msg).text





















