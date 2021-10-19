import selenium
from page.base_page import Base
import pytest
from time import sleep
from page.contact_us import Elements_contact_us 
import re

#4. check that country field contains only letters and spaces

@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    @pytest.mark.parametrize("text",["Armenia", "     "])
    def test_cuntry(self, text):
        driver = self.driver
        self.text = text
        contact = Elements_contact_us(driver)
        contact.fill_in_country(text)
        if text.isalpha():
            assert text.isalpha, "Valid country name"
        else:
            assert text.isalpha,"Valid country name"


        sleep(2)