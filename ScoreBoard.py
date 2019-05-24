import parser

API = input("API KEY : ")
HTB = parser.htb(API)

id = HTB.get_userid("sesha569")

rank = HTB.get_rank(id)

print(rank)
