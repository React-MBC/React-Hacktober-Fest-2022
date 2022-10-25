# pip install google
from googlesearch import search 

query = "Medium.com"
 
for url in search(query):
    print(url)