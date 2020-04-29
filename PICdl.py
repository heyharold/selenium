from selenium import webdriver
import urllib.request
import random
import os 

username = str(input("Enter username: "))

driver = webdriver.Chrome("D:/testbot/chromedriver.exe")
driver.get("https://www.instagram.com/"+username+"/")

images = driver.find_elements_by_class_name("FFVAD")

path = r"D:\testbot"
fname = username
imagepath =os.path.join(path,fname)
os.makedirs(imagepath, exist_ok=True)
os.chdir(imagepath)

if  os.getcwd() == imagepath:  
    for image in images[:2]:
        filename = 'img'+str(random.randint(1,100000))+'.jpg'
        
        url = image.get_attribute('src')
        urllib.request.urlretrieve(url, filename)

driver.close()
driver.quit()