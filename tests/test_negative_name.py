import selenium
from page.base_page import Base
import pytest
from time import sleep
from page.contact_us import Elements_contact_us 
import re

#1. check that the name field contains only letters and is not empty

@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    @pytest.mark.parametrize("text, result",[("Jack", True),("", False),("44678", False)])
    def test_name(self, text, result):
        driver = self.driver
        self.text = text
        self.result = result
        contact = Elements_contact_us(driver)
        contact.fill_in_name(text)
        print("HHHHHHH")
        if text.isalpha():
            print("valid name format")
        elif len(text)==0:
            print("Field error")
            driver.switch_to_alert
            print("Alert found")
        else:
            print("Invalid name format")

        sleep(4)