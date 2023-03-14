import time
from test_locators.LoginPage import Login
from test_locators.pimpage import AddNewEmployee


class Test_Delete_Employee:
    baseurl = "https:/opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    def test_delete_employee(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.loginpageobj = Login(self.driver)
        self.loginpageobj.setusername(self.username)
        self.loginpageobj.setpassword(self.password)
        self.loginpageobj.clickloginbutton()
        time.sleep(3)
        self.pimpageobj = AddNewEmployee(self.driver)
        self.pimpageobj.gotopim()
        self.pimpageobj.enterEmployeeName("Dinesh")
        self.pimpageobj.clicksearch()
        self.pimpageobj.deleteEmployee()
        self.delete = self.pimpageobj.deleteConformation()
        time.sleep(3)
        if self.delete == True:
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False