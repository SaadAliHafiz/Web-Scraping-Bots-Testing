import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.python.org/")
        
        
    # def test_example(self):
    #     print("test")
    #     assert False    
        
    # def test_example1(self):
    #     print("test1")
    #     assert True
        
    # def not_a_test(self):
    #     print("this dont print automatically")
        
    def test_title(self):
        mainPage=page.MainPage()
        assert mainPage.is_title_matches()
    def tearDown(self):
        self.driver.close()
        

if __name__== "__main__":
    unittest.main()