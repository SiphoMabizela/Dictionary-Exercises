# about = {
#         'name': 'Vusi',
#         'age': 25,
#         'favorite_color': 'black'
#         }

# about['age'] = 26
# about['email'] = 'vusi09@gmail.com'
# about['city'] = 'Johannesburg'
# # print(about['age'])
# # print(about['favorite_color'])
# # print(about['name'])
# print(about['name'])


# ==============================================================================================================================================================
'''
Building a simple contact book
'''

contact = {'name': 'Sipho',
           'phone': '+270672029505',
           'email': 'jane1@gmail.com'}

# look up phone number
# print(contact['phone'])

# update email
contact['email'] = 'smabizela3@gmail.com'


# add birthday
contact['birthday'] = '17 November'
# add vehicle
contact.update({'vehicle': 'BMW M2'})

print(sorted(contact.items()))

# ==============================================================================================================================================================

# looping through dictionaries

# looping through keys
contact = {'name': 'Sipho',
           'phone': '+270672029505',
           'email': 'jane1@gmail.com'}

# for key in contact:
#     print(key)


# # looping through values
# for value in contact.values():
#     print(value)


# looping through key value pairs

for key, value in contact.items():
    print(f'{key}: {value}')

# ==============================================================================================================================================================

