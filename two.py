#import pafy
from bs4 import BeautifulSoup
import requests
import urllib
import re
import copy
import pafy

url = "https://www.youtube.com/watch?v=7Qp5vcuMIlk"
base1 = "https://www.youtube.com"
#save file
#file = open("yt.txt",'w')
#maybe
#urllib.urlretrieve(url,"test.txt")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page = requests.get(url,headers=headers)
#print page.text


vids = []

souped = BeautifulSoup(page.text, "lxml")
#works tag = souped.find_all(class_="video-list-item")[0].find(class_='content-wrapper').find_all('a')[0]
#tag = souped.find_all(id="watch-related")[0].find_all(class_="video-list-item")[0].find(class_='content-wrapper').find_all('a')
tag = souped.find_all(id="watch-related")
#print tag
#this works .find('a', attrs='href')
#tag = souped.find_all('div')[0].find_all(class_="video-list-item")
#tag = souped.select("div.watch-sidebar-section.content-wrapper href)" while using it [0]
all_links = {}
count = 0
for tags in tag:
        #link = tags.find_all('a', attrs='href')
        # if tag.has_attr('href'):
        #         print "The link is %s" %(tag.attrs['href'])

        link = tags.find_all(class_="video-list-item")[0].find(class_='content-wrapper').find_all('a')[0].get('href')
        new_link = base1 + link
        all_links = {count:copy.copy(str(new_link))}

        #or all_links [count] = link

        count = count + 1
print ""
print all_links
print ""
for i in range(0,len(all_links)):
        print all_links[i]

input = raw_input("Do you want to download all these Youtube videos? \n Press 1 for Yes")

if ( input == "1" ):

        for i in range(0,len(all_links)):

                video = pafy.new(all_links[i])

                x = video.getbest()

                download = x.download(filepath="/Users/sameer18051998/PycharmProjects/untitled1/d/")


print "Total count = %d" %(count)