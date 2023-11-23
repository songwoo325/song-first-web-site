persons = [
    ['우현', '대방', '윤중'],
    ['남규', '대길', '강남'],
    ['기범', '대동', '대림'],
]
print(persons[0][0])

for person in persons:
    print(person[0]+','+person[1]+','+person[2])

person = ['우현', '대방', '윤중']
name = person[0]
address = person[1]
interest = person[2]
print(name, address, interest)

name, address, interest = ['우현', '대방', '윤중']
print(name, address, interest)

for name, address, interest in persons:
    print(name+','+address+','+interest)