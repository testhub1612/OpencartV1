from selenium.webdriver.common.by import By


class UM_Loginpage:

    def __init__(self, driver):

        # Initialize driver
        self.driver = driver

        # Collecting Locators
        self.txtbox_username_id = "username"
        self.txtbox_password_id = "password"
        self.btn_submit_xpath = "//*[@id='root']/div/div/div/div[2]/div/form/div[3]/button[2]/span"

    # Username
    def setUsername(self, username):
        self.driver.find_element(By.ID, self.txtbox_username_id).send_keys(username)

    # Password
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtbox_password_id).send_keys(password)

    # Submit button
    def clicksubmit(self):
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()