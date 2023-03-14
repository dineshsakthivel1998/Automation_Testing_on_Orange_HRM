from selenium.webdriver.common.by import By

class Login:
    txtbx_username_xpath = "//input[@name='username']"
    txtbx_password_xpath = "//input[@name='password']"
    btn_loginbutton_xpath = "//button[@type='submit']"
    txt_admin_xpath = "//span[text()='Admin']"
    mes_invalidcredential_xpath = "//p[text()='Invalid credentials']"

    def __init__(self,driver):
        self.driver = driver

    def setusername (self,username):
        self.driver.find_element(By.XPATH, self.txtbx_username_xpath).send_keys(username)

    def setpassword (self, password):
        self.driver.find_element(By.XPATH, self.txtbx_password_xpath).send_keys(password)

    def clickloginbutton (self):
        self.driver.find_element(By.XPATH, self.btn_loginbutton_xpath).click()

    def admin(self):
        return self.driver.find_element(By.XPATH, self.txt_admin_xpath).text


    def invalidcredential(self):
        return self.driver.find_element(By.XPATH, self.mes_invalidcredential_xpath).text

