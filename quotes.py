import requests
import bs4

proxies = {
    'http': 'http://ameya.daigavane:IITG2020%21@202.141.80.20:3128/',
    'https': 'http://ameya.daigavane:IITG2020%21@202.141.80.20:3128/',
    }

common_url = "http://www.brainyquote.com/quotes/topics/topic_"

with open("hitwords.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

count = 0
with open("quotes.txt", "w") as f:
    
    for line in lines:
        
        web_obj = requests.get(common_url + line + ".html", proxies = proxies)
        web_html = bs4.BeautifulSoup(web_obj.text, "html.parser")

        f.write(str(count) + "\n")
        for ele in web_html.find_all("div", class_="m-brick grid-item boxy bqQt"):
            
            quotes = ele.find_all("a", title ="view quote")
            author = ele.find_all("a", title ="view author")
            
            for i in range(len(quotes)):
                q = ''.join(quotes[i].findAll(text=True))
                q += " - "
                a = ''.join(author[i].findAll(text=True))

                line = q + a
                f.write(line + "\n")
        
        f.write("\n")
        count += 1
        

