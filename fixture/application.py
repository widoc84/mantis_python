from selenium import webdriver
from fixture.session import SH
from fixture.projects import PH
from fixture.james import JS
from fixture.mail import MH
from fixture.signup import SGH
from fixture.soap import SoapH


class Applicaton:
    def __init__(self, browser, config):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognazed browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SH(self)
        self.projects = PH(self)
        self.james = JS(self)
        self.config = config
        self.mail = MH(self)
        self.signup = SGH(self)
        self.soap = SoapH(self)
        Applicaton.base_url = config['web']['BaseUrl']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
