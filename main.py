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