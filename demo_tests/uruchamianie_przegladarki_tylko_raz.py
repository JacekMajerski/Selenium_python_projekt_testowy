import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
    @classmethod    #dzieki temu kod wykona sie przed wszystkimi testami w klasie
    def setUpClass(self):
        self.driver = webdriver.Chrome()


    def test_demo_login(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Logowanie' == title


    def test_demo_accounts(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Logowanie' == title


    def test_demo_pulpit(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/pulpit.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Pulpit' == title


    def test_demo_transfer(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/przelew_nowy_zew.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Przelew' == title

    @classmethod
    def tearDownClass(self):
        self.driver.quit()