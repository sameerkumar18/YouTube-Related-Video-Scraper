from bs4 import BeautifulSoup
import requests
import urllib
import re
import copy
import pafy

url = "__full-YoutTube-Video-Link-(with-https)__"
base1 = "https://www.youtube.com"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page = requests.get(url,headers=headers)


vids = []

souped = BeautifulSoup(page.text, "lxml")
#works tag = souped.find_all(class_="video-list-item")[0].find(class_='content-wrapper').find_all('a')[0]
#tag = souped.find_all(id="watch-related")[0].find_all(class_="video-list-item")[0].find(class_='content-wrapper').find_all('a')
tag = souped.find_all(id="watch-related")
all_links = {}
count = 0
for tags in tag:
        

        link = tags.find_all(class_="video-list-item")[count+1].find(class_='content-wrapper').find_all('a')[count].get('href')
        print link
        new_link = base1 + link
        all_links = {count:copy.copy(str(new_link))}


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
