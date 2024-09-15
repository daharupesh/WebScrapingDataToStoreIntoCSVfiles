import pandas as pd
import requests
from bs4 import BeautifulSoup

headers={
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive'
}

webpage = requests.get('https://www.ambitionbox.com/list-of-companies?page=1',headers=headers).text
soup = BeautifulSoup(webpage, 'html.parser')
company = soup.find_all('div',class_='companyCardWrapper')

name=[]
description = []
rating =[]
reviews= []

for i in company:
    name.append(i.find('h2').text.strip())
    rating.append(i.find('span',class_='companyCardWrapper__companyRatingValue').text.strip())
    description.append(i.find('span', class_='companyCardWrapper__interLinking').text.strip())
    reviews.append(i.find_all('span',class_='companyCardWrapper__ActionCount')[0].text.strip())
   
        
data_dict = {
    'Company Name':name,
    'description':description,
    'Rating' : rating,
    'Reviews' : reviews,
}

company_dataFrame = pd.DataFrame(data_dict)
print(company_dataFrame)
company_dataFrame.to_csv('company_data.csv')
