from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate

class TestGoogleLogin(StaticLiveServerTestCase):

    fixtures = ['allauth_fixture']

    @classmethod
    def setUpClass(cls):
        cls.host = "127.0.0.1" # or ip
        cls.port = 8081
        super(TestGoogleLogin, cls).setUpClass()
 
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.wait = WebDriverWait(self.browser, 10)
        activate('en')
 
    def tearDown(self):
        self.browser.quit()
 
    def get_element_by_id(self, element_id):
        return self.browser.wait.until(EC.presence_of_element_located(
                (By.ID, element_id)))
 
    def get_button_by_id(self, element_id):
        return self.browser.wait.until(EC.element_to_be_clickable(
                (By.ID, element_id)))

    def get_button_by_xpath(self, element_xpath):
        return self.browser.wait.until(EC.element_to_be_clickable(
                (By.XPATH, element_xpath)
        ))
 
    ## given a reverse name, returns full url.
    def get_full_url(self, namespace):
        print(self.live_server_url + reverse(namespace))
        return self.live_server_url + reverse(namespace)
 
    def test_google_login(self):
        self.browser.get(self.get_full_url("home"))
        google_login = self.get_element_by_id("google_login")
        ### make sure there is no logout id element
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("logout")
        ### make sure the link equals to 'localhost:8081/accounts/google/login'
        self.assertEqual(
            google_login.get_attribute("href"),
            self.live_server_url + "/accounts/google/login")
        google_login.click()
        ### if there is google_login raise timeoutexception
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("google_login")
        self.user_login()
        google_logout = self.get_element_by_id("logout")
        google_logout.click()

        # are you really sure you want to sign out submit button
        sign_out = self.get_button_by_xpath("/html/body/div/form/button")
        sign_out.click()

        # we have signed out and on the main page again
        google_login = self.get_element_by_id("google_login")


    # https://groups.google.com/forum/#!searchin/django-allauth/facebook/django-allauth/4EVgul6Zq3k/duFBH6nLsq8J
    def user_login(self):
        import json
        with open("website/fixtures/google_user.json") as f:
            credentials = json.loads(f.read())
        
        self.get_element_by_id("identifierId").send_keys(credentials["Email"]) 
        self.get_button_by_id("identifierNext").click()

        self.browser.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
        self.browser.find_element(By.XPATH, "//input[@type='password']").send_keys(credentials["Passwd"])
        self.get_button_by_id("passwordNext").click()