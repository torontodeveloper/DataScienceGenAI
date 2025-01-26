import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth 

api_key = 'Ll9KfB_2OOU83ssetKGKjA'
headers = {'Authorization': 'Bearer ' + api_key}
url = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'linkedin_profile_url': 'https://www.linkedin.com/in/yann-lecun/',
    'extra': 'include',
    'github_profile_id': 'include',
    'facebook_profile_id': 'include',
    'twitter_profile_id': 'include',
    'personal_contact_number': 'include',
    'personal_email': 'include',
    'inferred_salary': 'include',
    'skills': 'include',
    'use_cache': 'if-present',
    'fallback_to_cache': 'on-error',
}
response = requests.get(url,params=params,headers=headers)
print(response.json())
soup = BeautifulSoup(response.text,'html.parser')
profile_data = soup.prettify()
print(profile_data,type(profile_data))
#
# for key,value in profile_data.items():
#     print(f'{key}=========>{value}')