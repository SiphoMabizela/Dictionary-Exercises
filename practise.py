'''
Data structures: Set, Tuple, List
'''
# # fruits = {'banana', 'apple', 'orange', 'grapes', 'strawberries'} # set
# # fruits = ('banana', 'apple', 'orange', 'grapes', 'strawberries') # tuple
# fruits = ['banana', 'apple', 'orange', 'grapes', 'strawberries'] # list
# for fruit in fruits:
#     print(fruits)


# # fruits.remove('strawberries')
# # print(fruits)
# ================================================================================================================================================================
'''
Dictionary (data structure) index while iterating
'''
# capitals = {'South Africa': 'Cape Town',
#             'India': 'Dehli',
#             'Brazil': 'Rio',
#             'China': 'Beijing'}

# '''to iterate on  both the key and value, you call both iretable values
# on the for loop.
# '''
# index while iterating (like position 0, 1, 2…)
# for index, (country, capital) in enumerate (capitals.items()):
#     print(index, country, capital)


# # iterate over key–value pairs
# capitals = {'South Africa': 'Cape Town',
#            'China': 'Beijeng',
#            'Russia': 'Moscow',
#            'Brazil': 'Rio'}
# for country, capital in capitals.items():
#     print(country, capital)


# index of a specific key-value pair
capitals = {'South Africa': 'Cape Town',
           'China': 'Beijeng',
           'Russia': 'Moscow',
           'Brazil': 'Rio'}

# target_country = 'South Africa'
# target_capital = 'Capetown'

# for index, (country, capital) in enumerate(capitals.items()):
#     if country == target_country and capital == target_capital:
#         print('Index:', index)


# Index of a specific key only
# for index, country in enumerate(capitals):
#     if country == 'South Africa':
#         print(index)

# Index of a specific key value pair
for index, (country, capital) in enumerate(capitals.items()):
    if country == 'China' and capital == 'Beijeng':
        print(index, country, capital)

