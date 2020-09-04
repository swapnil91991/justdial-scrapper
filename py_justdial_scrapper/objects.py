import requests
from bs4 import BeautifulSoup 
from bunch import Bunch

class Query:
    
    def __init__(self, data, proxy=None, user_agent = ''):
        self.headers = {'User-Agent':user_agent}
        self.proxy=proxy
        self.url = data['link']
        self.name =data['name']
        self.full_name =data['full_name']
        self.thumb =data['thumb']
        self.phone=data['phone']
        self.rating =data['rating']
        self.votes =data['votes']
        self.json = data 
    
    def get_complete_details(self):
        
        jd = requests.get(self.url, headers=self.headers)
        
        soup = BeautifulSoup(jd.text, 'lxml')
        
        data = {
            'name':soup.find('span', {'class':'fn'}).text,
            
            'is_verified':True if soup.find('span', {'class':'jd_verified'}) else False,
            'is_trusted':True if soup.find('span', {'class':'jd_trusted'}) else False,
            'images': [i['src'] for i in soup.find_all('img', {'class':'cc_imgs'})],
            'address':soup.find('span', {'class':'lng_add'}).text.replace('\r', '').replace('\t', '').replace('\n', ''),
            'also_listed_in': [i.text.replace('\r', '').replace('\t', '').replace('\n', '') for i in soup.find_all('a', {'class':'lng_als_lst'})],
            'accepted_modes_of_payment': [i.text.replace('\r', '').replace('\t', '').replace('\n', '') for i in soup.find_all('span', {'class':'lng_mdpay'})],
            }
        
        return Bunch(data)
    


    def __repr__(self):
        return f'<Query - {self.name}  phone = {self.phone} >'
    
    def __str__(self):
        return self.phone
    
class Merchant:
    def __init__(self, data):
        pass
        
