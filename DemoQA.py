from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class locators:
    element_selector = (By.CSS_SELECTOR, '.top-card')
    check_box = (By.CSS_SELECTOR, ".btn-light")
    home_drop_down = (By.CSS_SELECTOR, '.rct-collapse')
    rtc_expanded = (By.XPATH, "//li[contains(@class, 'rct-node-expanded')]")
    rtc_downloads = (By.XPATH, "//li[contains(@class, 'rct-node-expanded')]//li[contains(@class, 'rct-node-expanded')]")
    downloads_dropdown = (By.CSS_SELECTOR, '.rct-collapse-btn')
    word_file_checkbox = (By.XPATH, "//label[@for='tree-node-wordFile']//span")
    word_file_checkbox_clicked = (By.XPATH, "//label[@for='tree-node-wordFile']//*[contains(@class, 'rct-icon-check')]")
    results = (By.XPATH, "//div[@id='result']/span")

class DataQA:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demoqa.com"

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator))

    def open_demoqa(self):
        self.driver.get(self.base_url)
    def click_element_button(self):
        #print(self.find_elements((By.CSS_SELECTOR(), '.top-card'))[0])
        self.find_elements(locators.element_selector)[0].click()

    def click_checkbox_button(self):
        self.find_elements(locators.check_box)[1].click()

    def click_home_dropdown_button(self):
        self.find_elements(locators.home_drop_down)[0].click()

    def click_download_dropdown(self):
        self.find_elements(locators.downloads_dropdown)[3].click()

    def click_wordfile_checkbox(self):
        self.find_elements(locators.word_file_checkbox)[0].click()

    def check_wordfile_checkbox(self):
        if len(self.find_elements(locators.word_file_checkbox_clicked)) == 1:
            check_string = ""
            for elem in self.find_elements(locators.results):
                check_string += elem.text
            return check_string
        else:
            return 'asdasd'

    def check_home_dropdown_expanded(self):
        if len(self.find_elements(locators.rtc_expanded)) == 1:
            return True
        else:
            return False

    def check_downloads_dropdown_expanded(self):
        if len(self.find_elements(locators.rtc_downloads)) == 1:
            return True
        else:
            return False
    def check_url(self):
        url = self.driver.current_url.split('/')[3]
        return url