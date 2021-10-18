import selenium
from page.base_page import Base
import pytest
from time import sleep
from page.contact_us import Elements_contact_us 
import re

#  5. check that Message field cannot have more than 180 letters, can be empty

@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    def test_message(self):
        driver = self.driver
        contact = Elements_contact_us(driver)
        contact.fill_in_message("Have got some problems, need your help")
        print("Message field contains less than 180 symbols")

        sleep(2)