import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.UM_LoginPage import UM_Loginpage


class Test_001_UMP_Login:

    baseURL = "http://172.16.1.164:3000/"

    def test_Login(self):

        # Launch Browser
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        # Open Application
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Create Object for Login Page
        self.lp = UM_Loginpage(self.driver)

        # Login Actions
        self.lp.setUsername("bala@nta")
        self.lp.setPassword("$0m_1EDg")
        self.lp.clicksubmit()

        time.sleep(5)

        # Validation
        assert "Login successful!" in self.driver.page_source

        # Close Browser
        self.driver.quit()