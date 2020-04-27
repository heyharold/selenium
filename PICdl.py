from selenium import webdriver
import urllib.request
import random

username = str(input("Enter username: "))

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/"+username+"/")

images = driver.find_elements_by_class_name("FFVAD")

for image in images[:2]:
    filename = 'img'+str(random.randint(1,100000))+'.jpg'
    url = image.get_attribute('src')
    urllib.request.urlretrieve(url, filename)

driver.close()
driver.quit()