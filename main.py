from selenium import webdriver
from time import sleep

class InstaBot:

    username =""
    def __init__(self,usern,pw):
        self.username = usern
        username = self.username
        self.password = pw
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Connectez-vous')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]").click()
        sleep(2)
    
    def getInfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(text(), 'crepeccino_ma')]").click()
        sleep(5)
      

fh = open("compte.txt","r")
my_text_username = str(fh.readline())
my_text_pw = str(fh.readline())
my_bot = InstaBot(my_text_username,my_text_pw)
