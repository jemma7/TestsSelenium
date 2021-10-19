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
    @pytest.mark.parametrize("text",["Jack", "", "44678"])
    def test_name(self, text):
        driver = self.driver
        self.text = text
        contact = Elements_contact_us(driver)
        contact.fill_in_name(text)
        print("HHHHHHH")
        if text.isalpha():
            assert text.isalpha(), "valid name format"
        elif len(text)==0:
            assert text.isalpha(),"Field error"
            assert driver.switch_to_alert(), "Alert found"
        else:
            assert text.isalpha(),"Invalid name format"


        sleep(4)