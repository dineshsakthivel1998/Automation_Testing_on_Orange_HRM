import time
from test_locators.LoginPage import Login

class Test_Login_02:

    baseurl = "https:/opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "invalidpassword"


    def test_invalid_login (self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.loginpageobj= Login(self.driver)
        self.loginpageobj.setusername(self.username)
        self.loginpageobj.setpassword(self.password)
        self.loginpageobj.clickloginbutton()
        time.sleep(3)
        self.wronglogin = self.loginpageobj.invalidcredential()
        if self.wronglogin == "Invalid credentials":
            self.driver.close()
            assert True
            
        else:
            self.driver.close()
            assert False
