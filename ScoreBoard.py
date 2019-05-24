import parser

API = "E0T1wLHz5H2Pc96d78DYbNu9WAye18lWbS6fendLQCZDQ0MIltlFPKQdJ3Dd"
HTB = parser.htb(API)

id = HTB.get_userid("sesha569")

rank = HTB.get_rank(id)

print(rank)