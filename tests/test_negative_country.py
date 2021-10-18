import selenium
from page.base_page import Base
import pytest
from time import sleep
from page.contact_us import Elements_contact_us 
import re

#4. check that country field contains only letters and spaces

@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    @pytest.mark.parametrize("text, result",[("Armenia", True),("        ", False),("44678", False)])
    def test_cuntry(self, text, result):
        driver = self.driver
        self.text = text
        self.result = result
        print("RRRR")
        print(driver)
        contact = Elements_contact_us(driver)
        contact.fill_in_country(text)
        if text.isalpha():
            print("Valid country name")
        else:
            print("Invalid country name")

        sleep(2)