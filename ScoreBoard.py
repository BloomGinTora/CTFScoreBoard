import parser

API = input("API KEY : ")
user = input("USERNAME : ")
HTB = parser.htb(API)

id = HTB.get_userid(user)

rank = HTB.get_rank(id)

print(rank)
