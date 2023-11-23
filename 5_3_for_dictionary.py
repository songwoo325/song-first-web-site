person = {'name':'dngus', 'address':'seoul', 'interest':'web'}
print(person['name'])

for key in person:
    print(key, person[key])

persons = [
    {'name':'dngus', 'address':'seoul', 'interest':'web'},
    {'name':'thddngus', 'address':'seoul', 'interest':'web'},
    {'name':'gus', 'address':'seoul', 'interest':'web'}
]

print('==== persons ====')
for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('----------------------------------------------------------')
