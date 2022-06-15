from xml.dom.minidom import Element
from git import Object


class BasePage(Object):
    def __init__(self,driver):
        self.driver=driver
        
        
class MainPage(BasePage):
    def is_title_matches(self):
        return "Python" in self.driver.title
    def click_go_button(self):
        element= self.driver.find_element_by_id("submit")
        element.click()