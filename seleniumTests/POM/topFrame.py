from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class TopFrame():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = "user[login]"
        self.password_textbox_name = "user[password]"
        self.login_button_class_name = "glyphicon-log-in"
        self.dropdown_button_id = "bg-nested-dropdown-brand"
        self.chemotion_repository_button_xpath = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[1]/a'
        self.complat_button_xpath              = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[2]/a'
        self.complat_on_github_button_xpath    = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[3]/a'
        self.eln_button_xpath                  = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[5]/a'
        self.about_button_xpath                = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[7]/a'
        self.signup_button_xpath               = '//*[@id="Home"]/div/div/div[1]/nav/div/div[2]/ul/li/a'
        self.edit_button_classname = "btn-primary"
        self.close_button_classname = "close"
        self.cancel_button_classname = "btn-warning"
        self.logout_button_classname = "glyphicon-log-out"

    def enter_username(self, username):
        elem = self.driver.find_element(By.NAME, self.username_textbox_name)
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password):
        elem = self.driver.find_element(By.NAME, self.password_textbox_name)
        elem.clear()
        elem.send_keys(password)

    def click_login(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.login_button_class_name)
        elem.click()

    def press_return_login(self):
        elem = self.driver.find_element(By.NAME, self.password_textbox_name)
        elem.send_keys(Keys.RETURN)

    def click_chemotion_repository(self):
        elem = self.driver.find_element(By.ID, self.dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.chemotion_repository_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)

    def click_complat(self):
        elem = self.driver.find_element(By.ID, self.dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.complat_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)

    def click_complat_on_github(self):
        elem = self.driver.find_element(By.ID, self.dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.complat_on_github_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)

    def click_eln(self):
        elem = self.driver.find_element(By.ID, self.dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.eln_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)

    def click_about(self):
        elem = self.driver.find_element(By.ID, self.dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.about_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)

    def click_signup(self):
        elem = self.driver.find_element(By.XPATH, self.signup_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)

    def click_edit(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.edit_button_classname)
        elem.click()

    def click_edit_close(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.close_button_classname)
        elem.click()

    def click_edit_cancel(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.cancel_button_classname)
        elem.click()

    def click_logout(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.logout_button_classname)
        time.sleep(1)
        elem.click()