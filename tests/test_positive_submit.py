from page.base_page import Base
import pytest
from time import sleep
from page.contact_us import Elements_contact_us


# 6. Check that the success notification pops up after form submission

@pytest.mark.usefixtures('set_up')
class TestPositive(Base):
    def test_submit(self):
        driver = self.driver
        contact = Elements_contact_us(driver)
        contact.submit()
        pop_up_mess = Elements_contact_us(driver)
        pop_up_mess.pop_up()
        driver.switch_to_alert
        print("SSSSSSSSSSSSSSS")
        
        sleep(3)
