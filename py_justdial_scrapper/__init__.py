import requests
from bs4 import BeautifulSoup 
from py_justdial_scrapper.exceptions import QueryNotFound
from py_justdial_scrapper.objects import Query
from bunch import Bunch
class JDScrapper:
    
    def getDigit(self, digit):
        index = {
            'yz':'1',
            'wx':'2',
            'vu':'3',
            'ts':'4',
            'rq':'5',
            'po':'6',
            'nm':'7',
            'lk':'8',
            'ji':'9',
            'acb':'0'
            }
        cls = digit['class'][1].replace('icon-', '')
        if cls in index.keys(): return index[cls]
        else: return ''
    
    def scrape_merchant(self, merchant):
        data = {
            "link":merchant['data-href'],
            "name":merchant.find('span', {'class':'lng_cont_name'}).text,
            "rating":float(merchant.find('span', {'class':'green-box'}).text),
            "votes": int(''.join([i  for i in  merchant.find('span', {'class':'rt_count lng_vote'}).text.replace('Votes', '').replace('\n', '') if i in '0123456789'])),
            }
        
        imgTag  = merchant.find('img', {'class':'altImgcls'})
        
        data['full_name'] = merchant.find('img', {'class':'altImgcls'})['title'] if imgTag else ''
        data['thumb'] = merchant.find('img', {'class':'altImgcls'})['data-src'] if imgTag else ''
        
        ts = merchant.find('p', {'class':'contact-info'}).a
        if ts.b != None:
            ts = ts.b
        digits = ts.find_all('span', {'class':'mobilesv'})
        num = []
        for digit in digits:
            num.append(self.getDigit(digit))
        data['phone'] = "".join(num)
        
        return data
        
    
    def scrape(self,
               query, 
               city, 
               user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36", 
               proxy = None
            ):
        self.user_agent = user_agent
        self.proxy=proxy
        self.query = query
        self.city = city
        
        self.headers = {
            'User-Agent':self.user_agent
            }
        
        jd = requests.get(f'https://www.justdial.com/{self.city}/{self.query}', headers=self.headers)
        
        assert(jd.status_code == 200), f"The request returned with status code {jd.status_code}"
        
        open('page.html', 'w+').write(jd.text)
        
        soup = BeautifulSoup(jd.text, 'lxml')
        
        not_found = soup.find('span', {'class':'srchnthd'})
    
        if not_found != None:
            raise QueryNotFound()
        
        data = []
        
        for page in range(10):
            
            jd = requests.get(f'https://www.justdial.com/{self.city}/{self.query}/page-{page}', headers=self.headers)
            
            soup = BeautifulSoup(jd.text, 'lxml')
            
            people = soup.find_all('li', {'class':'cntanr'})
            
            for i in people:
                data.append(Query(self.scrape_merchant(
                    i),
                    proxy=self.proxy,
                    user_agent=self.user_agent))
            
            #open('data.json', 'w+').write(str(
                                            #{'data':data
                                                #}
                                              #))
            
        return data

#t = JDScrapper()
#t.scrape( 'Hardware Shops', 'Nashik')
