import requests 
from bs4 import BeautifulSoup

def find_word_of_the_day():
    url="http://www.dictionary.com/wordoftheday"
    try:
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'lxml')
    except Exception as e:
        return e

    for k in soup.find_all('strong',limit=1):
        word = k.text

    for k in soup.find_all('li',class_="first"):
        meaning = k.text

    for k in soup.find_all(class_="citation-context"):
        c = [item.encode('utf-8') for item in k.text.split("\n")]
        citations = [item for i,item in enumerate(c) if item != "" and i%2!=0] 
    #output = "The word of the day:\n{}\n\nMeaning:\n{}\n\nCitations:\n{}".format(word.upper(),meaning,"\n".join(citations))
    print citations
    
    return (word.upper(),meaning,citations)


if __name__=="__main__":
    print find_word_of_the_day()
