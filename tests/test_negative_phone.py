import selenium
from page.base_page import Base
import pytest
from time import sleep
from page.contact_us import Elements_contact_us 
import re

#3. check that phone field contains only digits, not letters, not empty

@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    @pytest.mark.parametrize("text, result",[("45567789", True),("", False),("grfdytj", False)])
    def test_phone(self, text, result):
        driver = self.driver
        self.text = text
        self.result = result
        print("RRRR")
        print(driver)
        contact = Elements_contact_us(driver)
        contact.fill_in_phone(text)
        if text.isdigit():
            print("valid phone number")
        elif len(text)==0:
            print("Field error")
            driver.switch_to_alert
            print("Alert found")
        else:
            print("invalid phone number")

        sleep(2)
