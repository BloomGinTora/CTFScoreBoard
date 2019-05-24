import requests
from bs4 import BeautifulSoup
import json
import sys

class htb:
    def __init__(self, username=''):
        '''
        Enter api key

        '''
        self.username = username
    def get_userid(self, username):
        '''
        get_user_id(self,username)

        gets the profile id of a user based on their name
        requires an API token
        '''

        url = 'https://www.hackthebox.eu/api/user/id?api_token={}'.format(self.username)
        r = requests.post(url,params={'username': username})
        try:
            data = r.json()
            print(data)
            return data['id']
        except:
            print("Invalid API key or Invalid Username!")
            sys.exit()
    def get_rank(self, id):
        url = "https://www.hackthebox.eu/profile/{}".format(id)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        var1 = list(soup.find_all("td"))[0]
        var2 = str(var1).split(">")
        return var2[1].split("<")[0]
