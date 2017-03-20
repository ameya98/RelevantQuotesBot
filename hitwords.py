import requests
import bs4

proxies = {
    }

topics_page = "http://www.brainyquote.com"
topics_page_obj = requests.get(topics_page + "/quotes/topics.html", proxies = proxies)
topics_page_html = bs4.BeautifulSoup(topics_page_obj.text, "html.parser")

topics_urls = []
topics_list = []

for link in topics_page_html.find_all('a'):
    topics_urls.append(link.get('href'))

topics_urls = [i for i in topics_urls if i is not None]
    
for add in topics_urls:
    if "/quotes/topics/topic_" in add:
        topics_list.append(add.split("/quotes/topics/topic_")[1].replace(".html", ""))

f  = open("hitwords.txt", "w")
for topic in topics_list:
    f.write(topic + "\n")

f.close()
    


