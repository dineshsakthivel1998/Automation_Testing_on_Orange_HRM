import time
from pageObjects.LoginPage import Login
from pageObjects.pimpage import AddNewEmployee


class Test_Add_Employee:
    baseurl = "https:/opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    def test_add_new_employee(self, setup):
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
        self.pimpageobj.clickaddemp()
        self.pimpageobj.addfirstname("Dinesh")
        self.pimpageobj.addlastname("S")
        self.pimpageobj.clicksave()
        self.pimpageobj.addnickname("omiya")
        self.pimpageobj.addotherid(14072)
        self.pimpageobj.adddrivinglicense("TN8344422936200")
        self.pimpageobj.licenseexpdate("2030-04-24")
        self.pimpageobj.addssnnumber("987654")
        self.pimpageobj.addsinnumber("234567")
        self.pimpageobj.nationality()
        self.pimpageobj.maritialStatus()
        self.pimpageobj.dateofbirth("1998-09-17")
        self.pimpageobj.gender()
        self.pimpageobj.militaryService("No")
        self.pimpageobj.personaldetailssave()
        self.pimpageobj.bloodType()
        self.pimpageobj.customfieldsave()
        self.saveSuccess = self.pimpageobj.saveConformation()

        if self.saveSuccess == True:
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False