from urllib import request
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from urllib.request import urlopen
import time
from requests.api import head



fields = ['단어', '뜻1', '뜻2', '뜻3','뜻4','뜻5','뜻6']  # csv 파일 제일 상단의 필드





url= "https://dic.daum.net/search.do?q=" #검색할 사이트 url
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

xlsx=pd.read_excel("단어장1.xlsx")#convert xlsx to csv, set your xlsx file which you want to fill meanings of word
xlsx.to_csv("converted.csv") 

data=list() # list for storage word data
meaning=list()#list for meaning searched from web


f=open("converted.csv",'r')

rea=csv.reader(f)   
for row in rea: #load and save data to list 'data'
    data.append(row[1]) # change number in '[]' if you want to read other collunm

f.close() 


meaning=[] #2D list for saving means for word 

f=open("converted.csv",'w',newline='') #set your csv file location
write=csv.writer(f)
write.writerow(fields) #write fields



for i in range(0,len(data)): ##load data from web and save data to 2D list
    response = requests.get(url+data[i],headers=headers)
    readed_web = BeautifulSoup(response.text,'html.parser')
    time.sleep(0.5)
    line=[]
    line.append(data[i])
    for p in readed_web.select("div.cleanword_type ul.list_search span.txt_search"):
        
        line.append(p.get_text())
        print(p.get_text())
    
    meaning.append(line)
        



write.writerows(meaning) #write meaning to csv file


    
        
  
    



