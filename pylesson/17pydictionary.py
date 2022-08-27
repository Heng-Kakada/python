# dictionary =  A changeable, unordered collection of unique key:value pairs
#                      Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# print(capitals)

capitals.update({'Cambodia': 'Phnom Penh'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China')
capitals.clear()
# print(capitals['USA'])
# print(capitals.get('Cambodia'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
    print(key, value)





