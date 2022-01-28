from selenium.webdriver.common.by import By

class MainFrame():

    def __init__(self, driver):
        self.driver = driver

        self.close_button_classname = "close"
        self.export_dropdown_button_id = "export-dropdown"
        self.import_button_xpath = '//*[@id="app"]/div/div[1]/nav/div/ul/div[3]/div[1]/div[1]/ul/li[7]/a'
        self.import_file_select_button_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/input'
        self.import_import_button_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/button[2]'
        self.export_button_xpath = '//*[@id="app"]/div/div[1]/nav/div/ul/div[3]/div[1]/div[1]/ul/li[6]/a'
        self.export_checkbox_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/ul/li[1]/label'
        self.export_export_button_xpath = '//*[@id="md-export-dropdown"]/span'
        self.my_data_button_id = "tree-id-My Data"
        self.sample_link_xpath = '//*[@id="tabList-pane-0"]/div/div[2]/table/tbody[1]/tr[2]/td[2]'
        self.analyses_tab_id = "SampleDetailsXTab-tab-analyses"
        self.qc_tab_id = "SampleDetailsXTab-tab-qc_curation"
        self.references_tab_id = "SampleDetailsXTab-tab-references"
        self.literature_tab_id = "SampleDetailsXTab-tab-literature"
        self.results_tab_id = "SampleDetailsXTab-tab-results"
        self.properties_tab_id = "SampleDetailsXTab-tab-properties"
        self.spectra_editor_button_classname = "fa-area-chart"
        self.spectra_close_button_classname = "button-right.btn.btn-sm.btn-danger"
        self.sample_close_button_classname = "fa.fa-times"
        self.sample_edit_molecule_button_xpath = '//*[@id="SampleDetailsXTab-pane-properties"]/span[1]/div/table/tbody/tr[1]/td/div/div[1]/div[1]/span/span/button'
        self.sample_name_textbox_id = "txinput_name"
        self.sample_save_button_classname = "fa.fa-floppy-o"
        self.sample_name_label_xpath = '//*[@id="tabList-pane-0"]/div/div[2]/table/tbody[1]/tr[2]/td[2]/span/span[2]'
        self.sample_boiling_temperature_textbox_xpath = '//*[@id="SampleDetailsXTab-pane-properties"]/span[1]/div/table/tbody/tr[2]/td/div/div[3]/div/span/input'
        self.sample_melting_temperature_textbox_xpath = '//*[@id="SampleDetailsXTab-pane-properties"]/span[1]/div/table/tbody/tr[2]/td/div/div[4]/div/span/input'

    def click_import(self):
        self.driver.find_element(By.ID, self.export_dropdown_button_id).click()
        self.driver.find_element(By.XPATH, self.import_button_xpath).click()
    
    def enter_path_import_file_select(self, path):
        self.driver.find_element(By.XPATH, self.import_file_select_button_xpath).send_keys(path)

    def click_import_import(self):
        self.driver.find_element(By.XPATH, self.import_import_button_xpath).click()

    def click_import_close(self):
        self.driver.find_element(By.CLASS_NAME, self.close_button_classname).click()

    def click_export(self):
        self.driver.find_element(By.ID, self.export_dropdown_button_id).click()
        self.driver.find_element(By.XPATH, self.export_button_xpath).click()

    def click_export_checkbox(self):
        self.driver.find_element(By.XPATH, self.export_checkbox_xpath).click()

    def click_export_export(self):
        self.driver.find_element(By.XPATH, self.export_export_button_xpath).click()

    def click_export_close(self):
        self.driver.find_element(By.CLASS_NAME, self.close_button_classname).click()

    def click_my_data_button(self):
        self.driver.find_element(By.ID, self.my_data_button_id).click()

    def click_sample_link(self):
        self.driver.find_element(By.XPATH, self.sample_link_xpath).click()

    def click_analyses_tab(self):
        self.driver.find_element(By.ID, self.analyses_tab_id).click()

    def click_qc_tab(self):
        self.driver.find_element(By.ID, self.qc_tab_id).click()

    def click_literature_tab(self):
        self.driver.find_element(By.ID, self.literature_tab_id).click()

    def click_references_tab(self):
        self.driver.find_element(By.ID, self.references_tab_id).click()

    def click_results_tab(self):
        self.driver.find_element(By.ID, self.results_tab_id).click()

    def click_properties_tab(self):
        self.driver.find_element(By.ID, self.properties_tab_id).click()

    def click_spectra_editor_button(self):
        self.driver.find_element(By.CLASS_NAME, self.spectra_editor_button_classname).click()

    def click_spectra_close_button(self):
        self.driver.find_element(By.CLASS_NAME, self.spectra_close_button_classname).click()

    def click_sample_close_button(self):
        self.driver.find_element(By.CLASS_NAME, self.sample_close_button_classname).click()

    def click_sample_edit_molecule_button(self):
        self.driver.find_element(By.XPATH, self.sample_edit_molecule_button_xpath).click()

    def click_sample_edit_molecule_close_button(self):
        self.driver.find_element(By.CLASS_NAME, self.close_button_classname).click()

    def enter_sample_name(self, name):
        elem = self.driver.find_element(By.ID, self.sample_name_textbox_id)
        elem.clear()
        elem.send_keys(name)

    def get_sample_name_from_label(self):
        return self.driver.find_element(By.XPATH, self.sample_name_label_xpath).text

    def save_sample(self):
        self.driver.find_element(By.CLASS_NAME, self.sample_save_button_classname).click()

    def enter_boiling_temperature(self, temperature):
        elem = self.driver.find_element(By.XPATH, self.sample_boiling_temperature_textbox_xpath)
        elem.clear()
        elem.send_keys(temperature)

    def enter_melting_temperature(self, temperature):
        elem = self.driver.find_element(By.XPATH, self.sample_melting_temperature_textbox_xpath)
        elem.clear()
        elem.send_keys(temperature)

    def get_boiling_temperature(self):
        return self.driver.find_element(By.XPATH, self.sample_boiling_temperature_textbox_xpath).get_attribute("value")

    def get_melting_temperature(self):
        return self.driver.find_element(By.XPATH, self.sample_melting_temperature_textbox_xpath).get_attribute("value")