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
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Connectez-vous')]").click()
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]").click()
        sleep(5)
        #self.driver.find_elements_by_class_name("gmFkV").
        #self.driver.find_element_by_xpath("//a[contains(text(), 'crepeccino_ma')]").click()
        #self.driver.find_element_by_xpath("//a[@href='/"+ username + "/']").click()
        sleep(5)
    
    def getInfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(text(), 'crepeccino_ma')]").click()
        sleep(10)
    
    def sleepBot(self):
        sleep(2)    

fh = open("compte.txt","r")
my_text_username = str(fh.readline())
my_text_pw = str(fh.readline())
#print(my_text_pw)
#print(my_text_username)
my_bot = InstaBot(my_text_username,my_text_pw)
#my_bot.getInfollowers()
