from test_locators.LoginPage import Login

class Test_Login:

    baseurl = "https:/opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"


    def test_login (self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.loginpageobj= Login(self.driver)
        self.loginpageobj.setusername(self.username)
        self.loginpageobj.setpassword(self.password)
        self.loginpageobj.clickloginbutton()
        self.confmsg = self.loginpageobj.admin()
        if self.confmsg == "Admin":
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False
