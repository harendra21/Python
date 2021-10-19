# 30 useful python list snippets

[Click here to read](https://medium.com/p/eae1e7b0c41e)

![image](https://miro.medium.com/max/1400/1*-gHylNq-EK-SIIsvIHTYNA.jpeg)

Hello everyone, Today I am going to list down the important python list snippets which are very reusable while developing any application. So let's get started with a list of all the important python lists snippets.

## What is the list in python?

Python List is an ordered and flexible collection of data objects. Unlike similar members, which may contain items of the same type, a list may contain a combination of items.

- [30 useful python list snippets](#30-useful-python-list-snippets)
  - [What is the list in python?](#what-is-the-list-in-python)
  - [1. a to z list (python all alphabet list)](#1-a-to-z-list-python-all-alphabet-list)
  - [2. How to convert a set to a list in python](#2-how-to-convert-a-set-to-a-list-in-python)
  - [3. How to slice lists in python](#3-how-to-slice-lists-in-python)
  - [4. How to join python lists](#4-how-to-join-python-lists)
  - [5. How to add an element at the first position in python lists](#5-how-to-add-an-element-at-the-first-position-in-python-lists)
  - [6. How to find the first value of a list](#6-how-to-find-the-first-value-of-a-list)
  - [7. How to access the last element of a list in python](#7-how-to-access-the-last-element-of-a-list-in-python)
  - [8. How to convert python list to string separated by comma](#8-how-to-convert-python-list-to-string-separated-by-comma)
  - [9. How to count unique values in python list](#9-how-to-count-unique-values-in-python-list)
  - [10. How to clear a list in python](#10-how-to-clear-a-list-in-python)
  - [11. How to convert number to list of digits in python](#11-how-to-convert-number-to-list-of-digits-in-python)
  - [12. How to sort a list alphabetically in python](#12-how-to-sort-a-list-alphabetically-in-python)
  - [13. How to remove the item from the list in python](#13-how-to-remove-the-item-from-the-list-in-python)
  - [14. How to remove repeated elements from the list in pythons](#14-how-to-remove-repeated-elements-from-the-list-in-pythons)
  - [15. How to iterate a list in python](#15-how-to-iterate-a-list-in-python)
  - [16. Get element from python list](#16-get-element-from-python-list)
  - [17. How to return a list in python](#17-how-to-return-a-list-in-python)
  - [18. How to subtract lists in pythons](#18-how-to-subtract-lists-in-pythons)
  - [19. How to get the index list of a set value in python](#19-how-to-get-the-index-list-of-a-set-value-in-python)
  - [20. How to find an index of the item in the python list](#20-how-to-find-an-index-of-the-item-in-the-python-list)
  - [21. How to add all elements of a python list](#21-how-to-add-all-elements-of-a-python-list)
  - [22. How to find an index of sublist in list python](#22-how-to-find-an-index-of-sublist-in-list-python)
  - [23. How to convert a tuple to a list in python](#23-how-to-convert-a-tuple-to-a-list-in-python)
  - [24. How to convert list to list of strings in python](#24-how-to-convert-list-to-list-of-strings-in-python)
  - [25. How to create dictionary python from two lists in python](#25-how-to-create-dictionary-python-from-two-lists-in-python)
  - [26. How to add one list to another list python (combine two lists in python)](#26-how-to-add-one-list-to-another-list-python-combine-two-lists-in-python)
  - [27. Python list of tuples](#27-python-list-of-tuples)
  - [28. How to round the values in a python list](#28-how-to-round-the-values-in-a-python-list)
  - [29. How to find common elements in two lists python](#29-how-to-find-common-elements-in-two-lists-python)
  - [30. How to check if the type is the list in python](#30-how-to-check-if-the-type-is-the-list-in-python)
  - [Summary](#summary)

## 1. a to z list (python all alphabet list)
```python

atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

```

```python

#Python: premade alphabet string 

import string
string.ascii_lowercase
	#output: 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase
	#output: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

```

## 2. How to convert a set to a list in python
```python

my_set = set([1,2,3,4])
my_list = list(my_set)
print my_list
>> [1, 2, 3, 4]

```
```python

names = ['Barry', 'Alice', 'Bob', 'Bob']

unique_names = set(names)
# Result:
# {'Alice', 'Barry', 'Bob'}

```

## 3. How to slice lists in python

```python

# Example 1:
your_list = [0, 1, 2, 3, 4, 5]
your_list[0:5:1]
--> [0, 1, 2, 3, 4] # This illustrates how stop is not inclusive

# Example 2:
your_list = [0, 1, 2, 3, 4, 5]
your_list[::2] # Return list items for even indices
--> [0, 2, 4]

# Example 3:
your_list = [0, 1, 2, 3, 4, 5]
your_list[1::2] # Return list items for odd indices
--> [1, 3, 5]

# Example 4:
your_list = [0, 1, 2, 3, 4, 5]
your_list[4:-6:-1] # Return list items from 4th element from the left to 
#	the 6th element from the right going from right to left
--> [4, 3, 2, 1]
# Note, from the right, lists are 1-indexed, not 0-indexed 

```

## 4. How to join python lists

```python

l = ['aaa', 'bbb', 'ccc']

s = ''.join(l)
print(s)
# aaabbbccc

s = ','.join(l)
print(s)
# aaa,bbb,ccc

s = '-'.join(l)
print(s)
# aaa-bbb-ccc

s = '\n'.join(l)
print(s)
# aaa
# bbb
# ccc

```

## 5. How to add an element at the first position in python lists

```python

list = ["a", "b"]
list.insert(0, "c")
print(list)     # ['c', 'a', 'b']

```

## 6. How to find the first value of a list

```python

list = [1,2,3]
firstdigit = list[0] // 1 

list = ['Hello', 'bye', 'Adios']
firstvalue = list[0] // 'Hello'

```

## 7. How to access the last element of a list in python

```python

# To get the last element in a list you use -1 as position
bikes = ['trek', 'redline', 'giant']
bikes[-1]
# Output:
# 'giant'

```

## 8. How to convert python list to string separated by comma

```python 

hobbies = ["basketball", "football", "swimming"]
print("My hobbies are:")      	# My hobbies are:
print(", ".join(hobbies)) 		# basketball, football, swimming

```

## 9. How to count unique values in python list

```python 

# Basic syntax:
len(set(my_list))
# By definition sets only contain unique elements, so when the list
# is converted to a set all duplicates are removed. 

# Example usage:
my_list = ['so', 'so', 'so', 'many', 'duplicated', 'words']
len(set(my_list))
--> 4

# Note, list(set(my_list)) is a useful way to return a list containing
#	only the unique elements in my_list

```

## 10. How to clear a list in python

```python

lst = [1,2,3,4,5,6,7,8,9,10]
lst.clear()

```

## 11. How to convert number to list of digits in python

```python

n = 1234
# convert integer to list of digits
list_of_digits = list(map(int, f"{n}"))

# convert list of digits back to number
number = int(''.join(map(str, list_of_digits)))

```

## 12. How to sort a list alphabetically in python

```python

my_list = ['pera', 'apple', 'orange', 'grape']
my_list.sort() # ['apple', 'grape', 'orange', 'pera']

```

## 13. How to remove the item from the list in python

```python

# removes item with given name in list
list = [15, 79, 709, "Back to your IDE"]
list.remove("Back to your IDE")

# removes the last item in the list
list.pop()

# pop() also works with an index...
list.pop(0)

# ...and returns also the "popped" item
item = list.pop()

```

## 14. How to remove repeated elements from the list in pythons

```python

mylist = ["a", "b", "b", "c", "a"]
mylist = sorted(set(mylist))
print(mylist)

```

## 15. How to iterate a list in python

```python 

list = [1, 3, 5, 7, 9] 

# with index   
for index, item in enumerate(list): 
    print (item, " at index ", index)
    
# without index
for item in list:
  	print(item)

```

## 16. Get element from python list

```python

my_list = ["pizza", "soda", "muffins"]

my_list[0] # outputs "pizza"
my_list[-1] # outputs the last element of the list which is "muffins"
my_list[:] # outputs the whole list
my_list[:-1] # outputs the whole list except its last element

```


## 17. How to return a list in python

```python

def retList():
    list = []
    for i in range(0,10):
        list.append(i)
    return list
a = retList()
print a
#Output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```
## 18. How to subtract lists in pythons

```python

# Example usage using list comprehension:
list_a = [1, 2, 3]
list_b = [1, 1, 1]
[a_i - b_i for a_i, b_i in zip(list_a, list_b)]
--> [0, 1, 2]

```

## 19. How to get the index list of a set value in python

```python

>>> ["foo", "bar", "baz"].index("bar")
1

```
## 20. How to find an index of the item in the python list

```python

test = [ 'test 1', 'test 2', 'test 3' ]
for index, value in enumerate( test ):
  print( index, value )

```

## 21. How to add all elements of a python list

```python 

# Python code to demonstrate the working of  
# sum() 
numbers = [1,2,3,4,5,1,4,5] 
  
# start parameter is not provided 
Sum = sum(numbers) 
print(Sum) # result is 25  
# start = 10 
Sum = sum(numbers, 10) 
print(Sum) # result is 10 +25 = 35

```

## 22. How to find an index of sublist in list python

```python

greeting = ['hello','my','name','is','bob','how','are','you','my','name','is']

def find_sub_list(sl,l):
    results=[]
    sll=len(sl)
    for ind in (i for i,e in enumerate(l) if e==sl[0]):
        if l[ind:ind+sll]==sl:
            results.append((ind,ind+sll-1))

    return results

print find_sub_list(['my','name','is'], greeting) 
# [(1, 3), (8, 10)]

```

## 23. How to convert a tuple to a list in python

```python

aTuple = (123, 'xyz', 'zara', 'abc');
aList = list(aTuple)
print "List elements : ", aList

```

## 24. How to convert list to list of strings in python

```python

# Python program to convert a list 
# to string using list comprehension 
   
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas'] 
  
# using list comprehension 
listToStr = ' '.join([str(elem) for elem in s]) 
  
print(listToStr)

#output: I want 4 apples and 18 bananas

```
## 25. How to create dictionary python from two lists in python

```python

>>> keys = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>> dictionary = dict(zip(keys, values))
>>> print(dictionary)

#output: {'a': 1, 'b': 2, 'c': 3}

```
## 26. How to add one list to another list python (combine two lists in python)

```python

# Basic syntax:
first_list.append(second_list) # Append adds the the second_list as an
#	element to the first_list
first_list.extend(second_list) # Extend combines the elements of the 
#	first_list and the second_list

# Note, both append and extend modify the first_list in place

# Example usage for append:
first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9]
first_list.append(second_list)
print(first_list)
--> [1, 2, 3, 4, 5, [6, 7, 8, 9]]

# Example usage for extend:
first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9]
first_list.extend(second_list)
print(first_list)
--> [1, 2, 3, 4, 5, 6, 7, 8, 9]

```

## 27. Python list of tuples 

```python

#List of Tuples
list_tuples =  [('Nagendra',18),('Nitesh',28),('Sathya',29)]

#To print the list of tuples using for loop you can print by unpacking them
for name,age in list_tuples:
  print(name,age)

#To print with enumerate--->enumerate is nothing but gives the index of the array.
for index,(name,age) in list_tuples:
  #print using fstring
  print(f'My name is {name} and age is {age} and index is {index}')
  #print using .format
  print('My name is {n} and age is {a} and index is {i}'.format(n=name,a=age,i=index))

```

## 28. How to round the values in a python list

```python

a_list = [1.234, 2.345, 3.45, 1.45]
round_to_whole = [round(num) for num in a_list]

print(round_to_whole)

#output: [1, 2, 3, 1]

```

## 29. How to find common elements in two lists python

```python

# Example 1
list1 = ['little','blue','widget']
list2 = ['there','is','a','little','blue','cup','on','the','table']

list3 = set(list1)&set(list2)

list4 = sorted(list3, key = lambda k : list1.index(k))

# Example 2
list1 = [1,2,3,4,5,6]
list2 = [3, 5, 7, 9]
list(set(list1).intersection(list2))

```

## 30. How to check if the type is the list in python

```pythons

isinstance([0, 10, 20, 30], list) 		# True
isinstance(50, list)					# False

```

## Summary

I have covered 30 different types of python list snippets. I think these are important and used very frequently while working with python. 

I hope you like this post, if you like it please clap for it. Thank you in advance.