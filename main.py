#Loops
for x in [1,2,3,4,5,6]:
    for item in ['a','b','c','d']:
        print(1)
print('#######################################')
#iterable
users= {
    'name':'Juan',
    'age':50,
    'can_swim': False
}
for  item in users.items():
    print(item)
print('#####################################')
for  item in users.values():
    print(item)
print('#######################################')
for  item in users.keys():
    print(item)
print('#######################################')
for  item in users.items():
    key, value =item
    print(value)
print('#####################################')
my_list = [1,2,3,4,5,6,7,8,9,10]
counter=0
for item in  my_list :
    counter = counter + item
    print(counter)
print('#####################################')
#Ranges
for number in range(0,100):
    print(number)
print('#####################################')
for number in range(3):
    print(list(range(10)))

#enumeratem
print('#####################################')
for i,char in enumerate('helloooooo'):
     print(i,char)
print('#####################################')
#while
i=0
while i < 50:
    print(i)
    i+=1
else:
    print('Done')
print('#####################################')

some_list = ['a','b','c','d','e','b','c']

duplicate = []
for value in some_list:
    if some_list.count(value)>1:
        if value not in duplicate:
            duplicate.append(value)
print(duplicate)

