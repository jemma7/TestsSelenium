from page.base_page import Base
import pytest
from time import sleep
from page.contact_us import Elements_contact_us

# 7. Check the clear button

@pytest.mark.usefixtures('set_up')
class TestPositive(Base):
    def test_clear(self):
        driver = self.driver
        contact = Elements_contact_us(driver)
        contact.fill_in_name("Smith")
        contact.fill_in_email("sgdysdc.ru")
        contact.fill_in_phone("3567980542")
        contact.fill_in_country("Armenia")
        contact.fill_in_message("Need your help")
        sleep(3)
        contact.clear()

        print("CLEARED")

        sleep(3)