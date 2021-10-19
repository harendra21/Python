# 20 Helpful Python Snippets you must learn in 2021

[Click here to read](https://medium.com/p/65d52b538bd3/)

![image](https://cdn-images-1.medium.com/max/800/1*erVqlTKQ7b1wnZhdBRMNKQ.jpeg)

Python is one of the most popular languages used by many in data science, machine learning, web development, scripting automation, and many more. One of the reasons for this popularity is its simplicity and its ease of learning. If you are reading this article you are most likely already using python or at least interested in it.

------------

- ### Checking for uniqueness in Python List
**This method can be used to check if there are duplicate items in the given list.**

```python
# Let's leverage set()
def all_unique(lst):
    return len(lst) == len(set(lst))

y = [1,2,3,4,5]
print(all_unique(x))
print(all_unique(y))
```

- ### Anagram
An Anagram is a word or phrase formed by rearranging the letters of another word or phrase
**This method can be used to check if two strings are anagrams.**

```python
from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)

anagram("abcd3", "3acdb")
```

- ### Memory
**And this can be used to check the memory usage of an object:**

```python
import sys 

variable = 30 
print(sys.getsizeof(variable))
```

- ### Size in bytes
**The method returns the length of the string in bytes:**

```python
def byte_size(string):
    return(len(string.encode('utf-8')))
    
print(byte_size('?'))
```
```python
print(byte_size('Hello World'))
```

- ### Print the string N times
**This snippet can be used to output a string n once without the need to use loops for this:**

```python
n = 2; 
s = "Programming"

print(s * n);
```

- ### Makes the first letters of words large
**The snippet uses a method title() to capitalize each word in a string:**

```python
s = "programming is awesome"

print(s.title()) # Programming Is Awesome
```
- ### Separation
**This method splits the list into smaller lists of the specified size:**

```python
def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]
	
lstA = [1,2,3,4,5,6,7,8,9,10]
lstSize = 3
chunk(lstA, lstSize)
```
- ### Removing false values
**So you remove the false values ( False, None, 0 and '') from the list using filter():**

```python
def compact(lst):
    return list(filter(bool, lst))
  
compact([0, 1, False, 2, '',' ', 3, 'a', 's', 34])
```

- ### Counting

```python
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
[print(i) for i in transposed]
```

- ### Chain comparison
**You can do multiple comparisons with all kinds of operators in one line:**

```python
a = 3
print( 2 < a < 8) # True
print(1 == a < 2) # False
```

- ### Separate with comma
**convert a list of strings to a single string, where each item from the list is separated by commas**

```python
hobbies = ["singing", "soccer", "swimming"]

print("My hobbies are:") # My hobbies are:
print(", ".join(hobbies)) # singing, soccer, swimming
```

- ### Count the vowels
**This method counts the number of vowels (“a”, “e”, “i”, “o”, “u”) found in the string:**

```python
import re

def count_vowels(value):
    return len(re.findall(r'[aeiou]', value, re.IGNORECASE))

print(count_vowels('foobar')) # 3
print(count_vowels('gym')) # 0
```

- ### Converting the first letter of a string to lowercase
**Use to convert the first letter of your specified string to lowercase:**

```python
def decapitalize(string):
    return string[:1].lower() + string[1:]
  
print(decapitalize('FooBar')) # 'fooBar'
```

- ### Anti-aliasing
**The following methods flatten out a potentially deep list using recursion:**

```python
newList = [1,2]
newList.extend([3,5])
newList.append(7)
print(newList)
```

```python
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list

deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]
```

- ### Difference
**The method finds the difference between the two iterations, keeping only the values that are in the first:**

```python
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)

difference([1,2,3], [1,2,4]) # [3]
```

- ###  The difference between lists
**The following method returns the difference between the two lists after applying this function to each element of both lists:**

```python
def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


from math import floor
print(difference_by([2.1, 1.2], [2.3, 3.4],floor)) # [1.2]
print(difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])) # [ { x: 2 } ]
```

- ### Chained function call
**You can call multiple functions on one line:**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 4, 5
print((subtract if a > b else add)(a, b)) # 9
```

- ### Finding Duplicates
**This code checks to see if there are duplicate values ​​in the list using the fact that set()it only contains unique values:**

```python
def has_duplicates(lst):
    return len(lst) != len(set(lst))
    
x = [1,2,3,4,5,5]
y = [1,2,3,4,5]
print(has_duplicates(x)) # True
print(has_duplicates(y)) # False
```

- ### Combine two dictionaries
**The following method can be used to combine two dictionaries:**

```python
def merge_dictionaries(a, b):
    return {**a,**b}

a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}
```

- ### Convert two lists to a dictionary
**The following method can be used to combine two dictionaries:**

```python
def merge_dictionaries(a, b):
    return {**a,**b}

a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}
```

- ### Convert two lists to a dictionary
**Now let’s get down to converting two lists into a dictionary:**

```python
def to_dictionary(keys, values):
    return dict(zip(keys, values))
    
keys = ["a", "b", "c"]    
values = [2, 3, 4]
print(to_dictionary(keys, values)) # {'a': 2, 'c': 4, 'b': 3}
```

### Conclusion
So, in this article, I have covered the top 20 python snippets which are very useful while developing any python application. These snippets can help you save time and let you code faster.
I hope you like this article. Please clap and [follow me](https://harendraverma21.medium.com/) for more articles like this. Thank you for reading.

**Read more here**

https://python.plainenglish.io/30-useful-python-list-snippets-eae1e7b0c41e

https://python.plainenglish.io/automate-whatsapp-messages-with-python-9c9d5cfad0d0

https://python.plainenglish.io/how-to-create-a-screen-and-webcam-recorder-using-python-21c407277d42

https://python.plainenglish.io/30-python-string-snippets-part-2-ee6690dc7f9a
