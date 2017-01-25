from bs4 import BeautifulSoup
import requests
from sys import argv
import pafy
script, url = argv
#url = "https://www.youtube.com/watch?v=FyASdjZE0R0"
base1 = "https://www.youtube.com"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page = requests.get(url,headers=headers)


souped = BeautifulSoup(page.text, "lxml")


def download(input,all_links):
    if input == "1":

        for i in all_links:
            try:

                video = pafy.new(i)
                x = video.getbest()
                download = x.download(filepath="/Users/sameer18051998/PycharmProjects/untitled1/d/")

            except:
                print "Error downloading the video at URL - " + str(i)


def get_related_links(souped):
    all_links = []
    count = 0
    tag = souped.find_all('a', {"class": "content-link"})

    for i in tag:
        new_link = base1 + i.get('href')
        all_links.append(new_link)
        count = count + 1
    #i = 0
    print "Count is %d" % (count)

    print "Related links are: "
    for i in all_links:
        print i

    input = raw_input("Do you want to download all these Youtube videos? \n Press 1 for Yes")
    download(input,all_links)

    print "Total count = %d" %(count)

get_related_links(souped)
