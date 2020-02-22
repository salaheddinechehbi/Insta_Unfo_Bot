from selenium import webdriver
from time import sleep

class InstaBot:

    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Connectez-vous')]").click()
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        sleep(5)
    

fh = open("compte.txt","r")
my_text_username = str(fh.readline())
my_text_pw = str(fh.readline())
#print(my_text_pw)
#print(my_text_username)
InstaBot(my_text_username,my_text_pw)