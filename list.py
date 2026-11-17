fruits=['apple','banana','pineapple']
#fruits.append('mango')
fruits.insert(1,'mango')
fruits.remove('banana')
print(fruits)

#tuple
contact=('Prathima',20,'Bengaluru')
name,age,city=contact
print(name)
print(city)

#set
numbers={'1','10','32','44'}
numbers.add('99')
numbers.discard('1')
print(numbers)

#dic
student={
    'name':'Prathima',
    'dept':'cse',
    'age':20,
    'marks':95
}
print(student['name'])
print(student.get('age'))
student['city']='bangalore'
student['marks']=98
student.pop('age')

print(student)

for key,value in student.items():
    print(key,':',value)

print(student.keys())
print(student.values())

#slicing,#indexing
marks=[20,52,25,36,15]
print(marks[1:3])
print(marks[0])
print(marks[::-1])