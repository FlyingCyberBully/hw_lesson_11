from selenium.webdriver.common.by import By


class FormPage:

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    USER_EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.XPATH, "//label[@for='gender-radio-1']")
    MOBILE = (By.ID, "userNumber")
    SUBMIT = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://demoqa.com/automation-practice-form")

    def fill_first_name(self, value):
        self.driver.find_element(*self.FIRST_NAME).send_keys(value)
        
    def fill_last_name(self, value):
        self.driver.find_element(*self.LAST_NAME).send_keys(value)
        
    def fill_email(self, value):
        self.driver.find_element(*self.USER_EMAIL).send_keys(value)
        
    def select_gender(self):
        self.driver.find_element(*self.GENDER_MALE).click()
        
    def fill_mobile(self, value):
        self.driver.find_element(*self.MOBILE).send_keys(value)

    def submit(self):
        submit_button = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()
        