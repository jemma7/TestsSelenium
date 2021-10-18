from selenium import webdriver
from locators.locators import LocatorsXpath
import pytest

class Elements_contact_us:
    def __init__(self, driver):
        self.driver = driver
        self.name_button = LocatorsXpath.name
        self.e_mail_button = LocatorsXpath.e_mail
        self.telephone_button = LocatorsXpath.telephone
        self.country_button = LocatorsXpath.country
        self.company_button = LocatorsXpath.company
        self.message_button = LocatorsXpath.message
        self.submit_button = LocatorsXpath.submit
        self.clear_button = LocatorsXpath.clear
        self.field_req = LocatorsXpath.field_required
        self.invalid_em = LocatorsXpath.invalid_email
        self.invalid_ph = LocatorsXpath.invalid_phone
        self.feedback_popup = LocatorsXpath.feedback_sent
    
    def fill_in_name(self,text):
        print("XXXXXX")
        print(self.driver)
        input_name = self.driver.find_element_by_xpath(self.name_button)
        input_name.send_keys(text)
        print(input_name)
    
    def fill_in_email(self,email):
        print("XXXXXX")
        print(self.driver)
        input_email = self.driver.find_element_by_xpath(self.e_mail_button)
        input_email.send_keys(email)
        print(input_email)

    def fill_in_phone(self,text):
        print("XXXXXX")
        print(self.driver)
        input_phone = self.driver.find_element_by_xpath(self.telephone_button)
        input_phone.send_keys(text)
        print(input_phone)

    def fill_in_country(self,text):
        print("XXXXXX")
        print(self.driver)
        input_country = self.driver.find_element_by_xpath(self.country_button)
        input_country.send_keys(text)
        print(input_country)
    
    def fill_in_message(self,text):
        print("XXXXXX")
        print(self.driver)
        input_message = self.driver.find_element_by_xpath(self.message_button)
        while len(text) < 180:
            print(len(text))
            if len(text) > 180:
                break
            text += text
        input_message.send_keys(text)    
        
    def clear(self):
        print("XXXXXX")
        print(self.driver)
        clear_click = self.driver.find_element_by_xpath(self.clear_button)
        #clear_click.send_keys()
        clear_click.click()
        print(clear_click)

    def submit(self):
        print("XXXXXX")
        print(self.driver)
        submit_click = self.driver.find_element_by_xpath(self.submit_button)
        submit_click.send_keys()
        submit_click.click()
        print(submit_click)  

    def pop_up(self):
        field_req_popup = self.driver.find_element_by_xpath(self.field_req)
        #field_req_popup.send_keys()
        print("GGGGGG")



