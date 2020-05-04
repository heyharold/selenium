import requests 
from bs4 import BeautifulSoup as bs 
import csv 


# NOTE: Web scraping is illegal if you do not follow by the rules 
# seek first robots.txt of the website before scrape 

# Sitemap: https://nevonprojects.com/sitemap_index.xml

# User-agent: *
# Allow: /

r = requests.get("https://nevonprojects.com/project-ideas/software-project-ideas/")

soup = bs(r.content, 'html.parser')

print(soup.prettify())

links = []
# find all the ul in the link returend by the response as soup  
ul = soup.find('ul', attrs={'class':'press'}) #in soup find ul tag with attributes of class: press  

for li in ul.findAll('li'): #in ul findAll li 
	link = {}
	link['title'] = li.a.text #in li access the a anchor tag and .text to get the text returned by a
	link['link'] = li.a['href'] #under li and a tag access the href attribute of a and return its text
	links.append(link) #append link dictionary in links list 

print(links) # see links details 

filename = './project.csv' #path of csv file
with open(filename, mode='w') as csv_file: #open csv as stream with mode write as an object
	writer = csv.DictWriter(csv_file, ['title', 'link']) #instantiate csv dictionary writer and specify headers
	writer.writeheader() #create header / column name 
	for link in links: 
		writer.writerow(link) #write to csv file per row 

#end of program 

# DIFFERENT TYPES OF MODE IN FILE HANDLING 

# r or rb
# Open file for reading.
# w or wb
# Truncate to zero length or create file for writing.
# a or ab
# Append; open or create file for writing at end-of-file.
# r+ or rb+ or r+b
# Open file for update (reading and writing).
# w+ or wb+ or w+b
# Truncate to zero length or create file for update.
# a+ or ab+ or a+b
# Append; open or create file for update, writing at end-of-file.