from selenium import webdriver
from time import sleep

class InstaBot:

    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(10)
    

#Twitter()
fh = open("compte.txt","r")

my_text_pw = str(fh.readline())
my_text_username = str(fh.readline())
print(my_text_pw)
print(my_text_username)
InstaBot(my_text_username,my_text_pw)