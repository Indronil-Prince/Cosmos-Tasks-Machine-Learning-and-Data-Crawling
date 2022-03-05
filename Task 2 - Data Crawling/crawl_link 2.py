from comcrawl import IndexClient
from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

def crawl_link(domain, index):
    #link search with domain from the specific index client
    client = IndexClient(index, verbose=True)
    client.search(domain+"/*", threads=4)
    
    #search links by checking titles related with covid and economy related words
    links = []
    for i in range(0, len(client.results)):
        url = client.results[i]['url']
		if (('COVID' in url) or ('Covid' in url) or ('covid' in url) or ('coronavirus' in url) or ('Coronavirus' in url)) and (('Econom' in url) or ('econom' in url)):
			try:
				response = requests.get(url)
				html = response.text
				title = (str(BeautifulSoup(html).title))
				if (('COVID' in title) or ('Covid' in title) or ('covid' in title) or ('coronavirus' in title) or ('Coronavirus' in title)) and (('Econom' in title) or ('econom' in title)):
					links.append(url)
			except:
				True
            
    return links
	

domains = ["www.adb.org","www.worldbank.org","www.weforum.org","www.wto.org","www.un.org","www.imf.org", "reliefweb.int","www.financialexpress.com","www.economist.com", 
         "www.thedailystar.net","www.oecd.org","www.wsj.com","www.undp.org","www.washingtonpost.com","www.theguardian.com","www.telegraph.co.uk","www.dailytelegraph.com.au", 
         "www.aljazeera.com","www.bloomberg.com","www.business-standard.com","www.indiatimes.com"]
		 
index = ["2020-50","2020-45","2020-40","2020-34","2020-29"]
output = Workbook()
out_sheet = output.active

for domain in domains:
    crawled_links = crawl_link(domain, index)
    for link in crawled_links:
        out_sheet.append(link)
        
output.save("Links.xlsx")
output.close()