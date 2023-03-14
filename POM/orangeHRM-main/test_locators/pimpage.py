import time
from selenium.webdriver.common.by import By

class AddNewEmployee:

    clik_pim_xpath = "//span[text()='PIM']"
    clik_addemp_xpath = "//button[text()=' Add ']"
    inpt_firstname_xpath = "//input[@name='firstName']"
    inpt_lastname_xpath = "//input[@name='lastName']"
    clik_savebtn_xpath = "//button[@type='submit']"
    txtname_nickname_xpath = "//label[text()='Nickname']/parent::div/following-sibling::div/input"
    txtbx_otherid_xpath = "//div[2]/div[1]/div[2]/div[1]/div[2]/input"
    txtbx_drivinglicense_xpath ="//div[2]/div[2]/div[1]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    datepic_licenseexpdate_xpath ="//div[2]/div/div[2]/div/div/input[@placeholder='yyyy-mm-dd']"
    txtbx_ssnnumber_xpath = "//div[2]/div[3]/div[1]/div[1]/div[2]/input"
    txtbx_sinnumber_xpath ="//div[2]/div[3]/div[2]/div[1]/div[2]/input"
    drpdwn_nationality_xpath = "//form/div[3]/div/div[1]//div[text()='-- Select --']"
    select_nationality_xpath = "//*[contains(text(),'Indian')]"
    drpdwn_maritialstatus_xpath = "//div[2]/div/div[2]//div[@class='oxd-select-text-input']"
    select_single_xpath = "//*[contains(text(),'Single')]"
    select_married_xpath = "//*[contains(text(),'Married')]"
    datepic_DOB_xpath = "//div[3]//input[@placeholder='yyyy-mm-dd']"
    radiobtn_gender_xpath = "//label[text()='Male']"
    txtbx_militaryser_xpath = "//label[text()='Military Service']/parent::div/following-sibling::div/input"
    personaldetails_savebtn_xpath = "//div[5]/button[@type='submit']"
    drpdwn_bloodtype_xpath = "//form/div[1]/div/div[1]//div[text()='-- Select --']"
    select_bloodtype_xpath = "//*[contains(text(),'B+')]"
    customfield_savebtn_xpath = "//div[2]/button[@type='submit']"
    txtbx_empname_xpath = "//form/div/div/div[1]//input[@placeholder='Type for hints...']"
    drp_empname_xpath = "//*[contains(text(),'Rameshkumar')]"
    btn_search_xpath = "//button[@type='submit']"
    btn_editemp_xpath = "//button/i[@class ='oxd-icon bi-pencil-fill']"
    btn_deleteemp_xpath = "//button/i[@class='oxd-icon bi-trash']"
    btn_confirmdelete_xpath = "//button[text()=' Yes, Delete ']"
    txt_save_mes_xpath = "//*[text()='Successfully Saved']"
    txt_update_mes_xpath = "//*[text()='Successfully Updated']"
    txt_delete_mes_xpath = "//*[text()='Successfully Deleted']"


    def __init__(self,driver):
        self.driver = driver

    def gotopim(self):
        self.driver.find_element(By.XPATH, self.clik_pim_xpath).click()

    def clickaddemp(self):
        self.driver.find_element(By.XPATH, self.clik_addemp_xpath).click()

    def addfirstname(self,firstname):
        self.driver.find_element(By.XPATH, self.inpt_firstname_xpath).send_keys(firstname)

    def addlastname(self,lastname):
        self.driver.find_element(By.XPATH, self.inpt_lastname_xpath).send_keys(lastname)

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.clik_savebtn_xpath).click()

    def addnickname(self,nickname):
        self.driver.find_element(By.XPATH, self.txtname_nickname_xpath).send_keys(nickname)

    def addotherid(self,otherid):
        self.driver.find_element(By.XPATH, self.txtbx_otherid_xpath).send_keys(otherid)

    def adddrivinglicense(self,drivinglicense):
        self.driver.find_element(By.XPATH, self.txtbx_drivinglicense_xpath).send_keys(drivinglicense)

    def licenseexpdate(self,licenseexpdate):
        self.driver.find_element(By.XPATH, self.datepic_licenseexpdate_xpath).send_keys(licenseexpdate)

    def addssnnumber(self,ssnnumber):
        self.driver.find_element(By.XPATH, self.txtbx_ssnnumber_xpath).send_keys(ssnnumber)

    def addsinnumber(self,sinnumber):
        self.driver.find_element(By.XPATH, self.txtbx_sinnumber_xpath).send_keys(sinnumber)

    def nationality(self):
        self.driver.find_element(By.XPATH, self.drpdwn_nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.select_nationality_xpath).click()

    def maritialStatus(self):
        self.driver.find_element(By.XPATH, self.drpdwn_maritialstatus_xpath).click()
        self.driver.find_element(By.XPATH, self.select_single_xpath).click()

    def dateofbirth(self,dob):
        self.driver.find_element(By.XPATH, self.datepic_DOB_xpath).send_keys(dob)

    def gender(self):
        self.driver.find_element(By.XPATH, self.radiobtn_gender_xpath).click()

    def militaryService(self,militartservice):
        self.driver.find_element(By.XPATH, self.txtbx_militaryser_xpath).send_keys(militartservice)

    def personaldetailssave(self):
        self.driver.find_element(By.XPATH, self.personaldetails_savebtn_xpath).click()

    def bloodType(self):
        self.driver.find_element(By.XPATH, self.drpdwn_bloodtype_xpath).click()
        self.driver.find_element(By.XPATH, self.select_bloodtype_xpath).click()

    def customfieldsave(self):
        self.driver.find_element(By.XPATH, self.customfield_savebtn_xpath).click()

    def enterEmployeeName(self,employeename):
        self.driver.find_element(By.XPATH, self.txtbx_empname_xpath).send_keys(employeename)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.drp_empname_xpath).click()

    def clicksearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def clickeditbutton(self):
        self.driver.find_element(By.XPATH, self.btn_editemp_xpath).click()

    def editMaritialstatus(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.drpdwn_maritialstatus_xpath).click()
        self.driver.find_element(By.XPATH, self.select_married_xpath).click()
        self.driver.find_element(By.XPATH, self.personaldetails_savebtn_xpath).click()

    def deleteEmployee(self):
        self.driver.find_element(By.XPATH, self.btn_deleteemp_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_confirmdelete_xpath).click()


    def saveConformation(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_save_mes_xpath).is_displayed()
        except:
            return False
    def updateConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_update_mes_xpath).is_displayed()
        except:
            return False
    def deleteConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_delete_mes_xpath).is_displayed()
        except:
            return False