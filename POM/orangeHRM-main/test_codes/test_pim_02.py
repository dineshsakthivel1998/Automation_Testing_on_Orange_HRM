import time
from pageObjects.LoginPage import Login
from pageObjects.pimpage import AddNewEmployee


class Test_Edit_Employee:
    baseurl = "https:/opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    def test_edit_employee_details(self, setup):
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
        self.pimpageobj.enterEmployeeName("Rameshkumar")
        self.pimpageobj.clicksearch()
        self.pimpageobj.clickeditbutton()
        self.pimpageobj.editMaritialstatus()
        self.update = self.pimpageobj.updateConformation()
        time.sleep(3)
        if self.update == True:
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False
