import requests 
from bs4 import BeautifulSoup

url="http://www.dictionary.com/wordoftheday"
r=requests.get(url)
soup=BeautifulSoup(r.content,'lxml')

for k in soup.find_all('strong',limit=1):
	word = k.text

for k in soup.find_all('li',class_="first"):
	meaning = k.text

for k in soup.find_all(class_="citation-context"):
    citations = [item for i,item in enumerate(map(str,k.text.split("\n"))) if item != "" and i%2!=0] 

output = "The word of the day:\n{}\n\nMeaning:\n{}\n\nCitations:\n{}".format(word.upper(),meaning,"\n".join(citations))
print output

