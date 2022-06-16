import unittest
import page
from selenium import webdriver
from page import SearchTextElement
from page import SearchResultPage

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.python.org/")
        
        
    def test_search_python(self):
        mainPage=page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element ="pycon"
        mainPage.click_go_button()
        search_result_page=page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
    # def test_example(self):
    #     print("test")
    #     assert False    
        
    # def test_example1(self):
    #     print("test1")
    #     assert True
        
    # def not_a_test(self):
    #     print("this dont print automatically")
        
    # def test_title(self):
    #     mainPage=page.MainPage()
    #     assert mainPage.is_title_matches()
    def tearDown(self):
        self.driver.close()
        

if __name__== "__main__":
    unittest.main()
