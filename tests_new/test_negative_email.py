import selenium
from page.base_page import Base
import pytest
from time import sleep
from page.contact_us import Elements_contact_us 
import re

#2. check that the email is valid

global regex 
regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    @pytest.mark.parametrize("email",["ankitrai326@gmail.com", "   ", "556rai326.com"])
    def test_email(self, email):
        driver = self.driver
        self.email = email
        print("RRRR")
        contact = Elements_contact_us(driver)
        contact.fill_in_email(email)
        sleep(3)
        if regex.match(email):
            assert regex.match(email),"email is valid"
        elif len(email)==0:
            assert regex.match(email), "Field error"
            assert driver.switch_to_alert, "Alert found"
        else:
            assert regex.match(email), "email is not valid"


        sleep(4)   