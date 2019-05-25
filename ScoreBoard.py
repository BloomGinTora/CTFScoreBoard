import parser

API = input("API KEY : ")
user = input("USERNAME : ")
'''
HTB
'''
HTB = parser.htb(API)

id = HTB.get_userid(user)

rankHTB = HTB.get_rank(id)

print(rankHTB)

'''
ROOT ME
'''
rootme = parser.rootMe(username)
rankRM = rootme.get_rank()
print(rankRM)
