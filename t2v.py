
#doc_source = "/home/ckwang/project/txt2voice/t2v.txt"
#f = open(doc_source, "r")
#context = f.read()
#print context


import urllib2
from bs4 import BeautifulSoup
import requests
import re
import smtplib
from email.header import Header


fs_number=2002
req=requests.get('http://www.jiqizhixin.com/article/2651')
soup=(BeautifulSoup(req.text.encode('utf-8'), "html.parser"))

paragraphs = soup.find_all('p')
#print paragraphs
string_list = []
for p in paragraphs:
    p = str(p)    
    start = p.find('">')
    #if(start == -1):
    #    continue
    head = p[(start+2):(start+5)]
    if((head == "<sp") or (head == "<im") or (head == "<st") or (head == "<em")):
        continue
    #if((len(p)-start) < 10):  
    #    continue
    if(p[(start-3):(start+1)] == 'em;"'):
        end = p.find("</p")
        print p[(start+2):end]
        string_list.append(p[(start+2):end])
        print p
        print "\n\n\n"
string_all = ' '.join(string_list)
print string_all
context = string_all





from gtts import gTTS
from tempfile import TemporaryFile
tts = gTTS(text=context, lang='zh-cn')
f = TemporaryFile()
tts.write_to_fp(f)


tts = gTTS(text=context, lang='zh-cn')
f = TemporaryFile()
tts.write_to_fp(f)
f.close()

tts.save("hello.mp3")
#'zh-cn' : 'Chinese (Mandarin/China)'
#'zh-tw' : 'Chinese (Mandarin/Taiwan)'
#'zh-yue' : 'Chinese (Cantonese)'



import pygame,sys
pygame.init()
pygame.mixer.init()
pygame.time.delay(1000)
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()







import BeautifulSoup
import urllib2
from bs4 import BeautifulSoup
import MySQLdb
import requests
import re
import smtplib


def get_articles(dom, date):
    #soup = BeautifulSoup(urllib2.urlopen(dom))#BeautifulSoup(dom)#, 'html.parser')
    fs_number = 2002
    financial_statement = str(BeautifulSoup(urllib2.urlopen('http://jsjustweb.jihsun.com.tw/z/zc/zca/zca_' + str(fs_number) +'.djhtm').read()))
    print financial_statement
    soup = BeautifulSoup(urllib2.urlopen('http://jsjustweb.jihsun.com.tw/z/zc/zca/zca_' + str(fs_number) +'.djhtm').read())
    articles = [] 
    divs = soup.find_all('div', 'r-ent')
    for d in divs:
        if d.find('div', 'date').string == date:  

            push_count = 0
            if d.find('div', 'nrec').string:
                try:
                    push_count = int(d.find('div', 'nrec').string) 
                except ValueError: 
                    pass		
            if d.find('a'):  
                href = d.find('a')['href']
                title = d.find('a').string
                articles.append({
                    'title': title,
                    'href': href,
                    'push_count': push_count
                })
    return articles


page = get_articles('http://www.ptt.cc/bbs/Beauty/index.html','12/21')
if page:
    date = time.strftime("%m/%d").lstrip('0') 
    current_articles = get_articles(page, date)
    for post in current_articles:
        print(post)



