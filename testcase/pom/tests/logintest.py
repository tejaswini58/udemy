from selenium import webdriver
import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from testcase.pom.pages.loginpage import loginpage
from testcase.pom.pages.homepage import homepage

class logintests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)

    def test_login_cred(self):
        driver =self.driver
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com")
        login =loginpage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.login_btn()

        Homepage=homepage(driver)
        Homepage.click_welcome()
        Homepage.click_logout()


        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").send_keys(Keys.ENTER)
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(5)
        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("test completed")


if __name__ == '__main__':
    unittest.main()
