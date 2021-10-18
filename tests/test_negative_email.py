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
    @pytest.mark.parametrize("email, regex",[("ankitrai326@gmail.com", regex),("   ", regex),("556rai326.com", regex)])
    def test_email(self, email, regex):
        driver = self.driver
        self.email = email
        self.regex = regex
        print("RRRR")
        contact = Elements_contact_us(driver)
        contact.fill_in_email(email)
        sleep(3)
        if regex.match("email"):
            print("email is valid")
        elif len(email)==0:
            print("Field error")
            driver.switch_to_alert
            print("Alert found")
        else:
            print("email is not valid")

        sleep(4)   