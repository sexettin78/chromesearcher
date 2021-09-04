a = input("Aranacak yazıyı giriniz: ")
#b = a.replace(" ","+")
c = ("https://www.google.com/search?q="+a)
from selenium import webdriver
import time
driver_path = "C:\\Users\\PC\\Downloads\\chromedriver.exe"

browser = webdriver.Chrome(executable_path=driver_path)

browser.get(c)

