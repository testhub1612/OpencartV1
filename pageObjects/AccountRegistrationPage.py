from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AccountRegistrationPage:
    #Collecting the locators
    txt_firstname_id="input-firstname"
    txt_lastname_id = "input-lastname"
    txt_email_id = "input-email"
    txt_password_id = "input-password"
    btn_subscribe_id = "input-newsletter"
    btn_privacy_policy_xpath = "//input[@name='agree']"
    btn_continue_xpath="//button[normalize-space()='Continue']"
    txt_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    #constructor
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,30)

    #Action methods
    def setFirstname(self,firstname):
        self.driver.find_element(By.ID,self.txt_firstname_id).send_keys(firstname)
    def setLastname(self,lastname):
        self.driver.find_element(By.ID,self.txt_lastname_id).send_keys(lastname)
    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txt_email_id).send_keys(email)
    def setPassword(self,pwd):
        self.driver.find_element(By.ID,self.txt_password_id).send_keys(pwd)
    def subscribeid_click(self):
        self.driver.find_element(By.ID,self.btn_subscribe_id).click()
    def privacypolicy_btn(self):
        self.driver.find_element(By.XPATH,self.btn_privacy_policy_xpath).click()
    def continue_btn(self):
        self.driver.find_element(By.XPATH,self.btn_continue_xpath).click()
    def confmessage(self):
        self.driver.find_element(By.XPATH,self.txt_msg_conf_xpath)