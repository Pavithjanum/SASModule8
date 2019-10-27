
#1 Write a program to fetch hyperlinks from any website which user enters

import requests
from bs4 import BeautifulSoup
import youtube_dl

import os
os.chdir(r'C:\Users\PAVI\Desktop\Edureka\Python Certification\Module8')
os.getcwd()

website = input('Enter any Website address from which you need all hyperlinks from: ')
hyperlinks=[]
headers={"content-type":"text"}
try:
    r=requests.get(website,headers=headers,verify=False)
    c = r.content
    s = BeautifulSoup(c,'html.parser')
    for f in s.find_all('a'):
        if f.get('href') not in (None,'',' '):
            hyperlinks.append(f.get('href'))
except Exception as e:
    print('Not a valid website..Try again',e)
finally:
    print('The Hyperlinks present in the provided websites are as follows\n')
    for entry in enumerate(hyperlinks,start=1):
        print(str(entry[0])+'.'+entry[1])

 
from bs4 import BeautifulSoup 
import requests 
url = input("Enter a website to extract the URL's from: ") 
r = requests.get(url,headers=headers,verify=False) 
data = r.text 
soup = BeautifulSoup(data) 
for link in soup.find_all('a'): 
    print(link.get('href'))
    
#2 # Write a program to download all the videos from youtube.com for django from the hyperlink

import requests
from bs4 import BeautifulSoup
website = 'https://www.youtube.com/playlist?list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD'
headers = {'Name':'Pavi'}
raw_data = requests.get(website,headers=headers,verify=False)
raw_content = raw_data.content
video_temp_url=[]
video_temp2_url=[]
video_url=[]
import re
j = re.compile(r'(.*com)(.*)')
i = j.findall(website)
print(i)
main_url = i[0][0]
soup_data = BeautifulSoup(raw_content,'html.parser')
for l in soup_data.find_all('a'):
    if l.get('href') not in (None,'',' '):
        if (l.get('href').startswith('/watch?v')):
            video_temp_url.append(main_url+''+l.get('href'))
video_temp2_url=list(set(video_temp_url))

for item in video_temp_url:
    if ((item in video_temp2_url) and (item not in video_url)):
        video_url.append(item)


import youtube_dl
ydl_opts = {}
i=1
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([website])
print('Completed Downloading')    


import lxml
import html5lib
from bs4 import BeautifulSoup 
import csv 
soup = BeautifulSoup (open("test.html"),lxml)
f = csv.writer(open("outfile.csv", "w")) 
f.writerow(["Name", "Link"]) # Write column headers as the first line 
links = soup.find_all('a') 
for link in links: 
    names = link.contents[0] 
    fullLink = link.get('href') 
    f.writerow([names,fullLink])
    f = open("outfile.csv", "r") 
    f.read()
    
