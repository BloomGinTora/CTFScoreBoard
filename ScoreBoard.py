import parser

API = input("API KEY : ")
user = input("USERNAME : ")
'''
HTB
'''
HTB = parser.htb(API)

id = HTB.get_userid(user)

rank = HTB.get_rank(id)

print(rank)

'''
ROOT ME
'''
rootme = parser.rootMe(username)
rootme.get_rank()
