import os.path
import time

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString


class Test_001_AccountReg:
    baseURL="https://www.opencart.com/index.php?route=cms/demo"

    def test_account_reg(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.click_view_store()
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.rpage=AccountRegistrationPage(self.driver)
        self.rpage.setFirstname("John")
        self.rpage.setLastname("smith")
        self.email=randomString.random_string_generator()+'@gmail.com'
        self.rpage.setEmail(self.email)
        self.rpage.setPassword("admin@123")
        self.rpage.subscribeid_click()
        self.rpage.privacypolicy_btn()
        self.rpage.continue_btn()
        self.confmsg=self.rpage.confmessage()
        self.driver.close()
        #assert "Your account has been created!" in self.confmsg
        if self.confmsg=="Your account has been created!":
         assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png ")
            self.driver.close()
            assert False




