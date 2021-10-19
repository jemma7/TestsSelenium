import selenium
from page.base_page import Base
import pytest
from time import sleep
from page.contact_us import Elements_contact_us 
import re

#3. check that phone field contains only digits, not letters, not empty

@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    @pytest.mark.parametrize("text",["45567789", "", "grfdytj"])
    def test_phone(self, text):
        driver = self.driver
        self.text = text
        contact = Elements_contact_us(driver)
        contact.fill_in_phone(text)
        if text.isdigit():
            assert text.isdigit(), "Valid phone number"
        elif len(text)==0:
            assert text.isdigit(), "Field error"
            assert driver.switch_to_alert(), "Alert found"
        else:
            assert text.isdigit(),"Invalid phone number"

        sleep(2)
