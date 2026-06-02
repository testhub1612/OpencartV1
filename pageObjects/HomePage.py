from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    # locators
    link_view_store_xpath="//a[@href='https://demo.opencart.com/']"
    link_myaccount_xpath = "//a[@title='My Account']"
    link_register_linktext = "Register"
    link_login_linktext = "Login"

    # constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 35)

    # action methods
    def click_view_store(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.link_view_store_xpath))
        ).click()
    def clickMyAccount(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.link_myaccount_xpath))
        ).click()

    def clickRegister(self):
        self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, self.link_register_linktext))
        ).click()

    def clickLogin(self):
        self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, self.link_login_linktext))
        ).click()
# import time
# from telnetlib import EC
#
# from selenium.webdriver.common.by import By
#
# class HomePage:
#     #collecting the locators
#     link_myaccount_xpath="//span[normalize-space()='My Account']"
#     link_register_linktext="Register"
#     link_login_linktext="Login"
#
#     #constructor
#     def __init__(self,driver):
#         self.driver=driver
#
#     #action methods
#     def clickMyAccount(self):
#         self.wait.until(
#             EC.element_to_be_clickable((By.XPATH, self.myaccount_xpath))
#         ).click()
#         self.driver.find_element(By.XPATH,self.link_myaccount_xpath).click()
#
#     def clickRegister(self):
#         self.wait.until(
#             EC.element_to_be_clickable((By.LINK_TEXT, self.register_linktext))
#         ).click()
#         self.driver.find_element(By.LINK_TEXT,self.link_register_linktext).click()
#
#     def clickLogin(self):
#         self.driver.find_element(By.LINK_TEXT,self.link_login_linktext).click()
#
