# zip (*iterables)

username = ["Ahmad","Adel","Omar"]
password = ["12345Ahmad","12345Adel","12345Omar"]
date = ["1/1/2021","1/1/2020","1/1/2019"]

# users = zip(username,password)
#
# for i in users:
#     print(i)

# users = dict(zip(username,password))  #key:value
#
# for (key,value) in users.items():
#     print(key + " : " + value)

users_2 = zip(username,password,date)

for i in users_2:
    print(i)

# print(users)