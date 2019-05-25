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
    
    
class rootMe:
    def __init__(self, username=''):
        '''
        Enter username.
        Might not work for some usernames, specially with spaces and special chars.
        '''
        self.username = username
    def get_rank(self):
        url = "https://www.root-me.org/{}?lang=en".format(self.username)
        url2 = "https://www.root-me.org/{}?inc=score&lang=en".format(self.username)
        check = requests.get(url2)
        r = requests.get(url)
        '''
        Check if user is on scoreboard :
        '''
        soupcheck = BeautifulSoup(check.content, 'html.parser')
        notOnScoreBoardMsg = str(soupcheck.find_all("h3")[-1])
        if notOnScoreBoardMsg == "<h3>This author does not participate to challenges.</h3>":
            print("User is not on scoreboard yet !")
            sys.exit()
        else:
            pass
        '''
        Split to get score :
        '''
        soup = BeautifulSoup(r.content, 'html.parser')
        var1 = soup.find("div", {"class" : "t-body tb-padding"})
        var2 = str(var1.find_all("li"))
        var3 = var2.split(">")[9]
        score = var3.split("<")[0]
        return score

