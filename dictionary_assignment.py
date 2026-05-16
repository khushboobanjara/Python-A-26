# Create a dictionary with keys &#39;name&#39;, &#39;age&#39;, and &#39;city&#39; using the provided values and return it.

student_data = {
    'name': "alice",
    'age': 25,
    'city': 'paris'

}

print("Student Data",student_data)

# 2. Given a dictionary, return the value associated with a given key. Return None if key does not exist.

dic = {'a':10, 'b': 20}
key = 'a'

# for i in dic:
if key in dic:
    print(dic[key])
else:
    print("none")

# 3.Add a new key-value pair to an existing dictionary and return the updated dictionary.

dic = {'a':10, 'b': 20}
dic['c'] = 30
print(dic)

# 4.Remove a specified key from the dictionary and return the updated dictionary. Do nothing if key is absent.

dic = {'a':1, 'b':2, 'c':3, 'd':4}
key = 'd'


if key in dic:
    dic.pop(key)

print(dic)

# 5. Return the total number of key-value pairs in the given dictionary.

dic = {'a':10, 'b': 20,'x':True,'y':None}
counter = 0
for i in dic:
    counter+=1
print("number of elements in dictionary ",counter)
    

# 6. Return True if the given key exists in the dictionary, otherwise return False.

dic = {'name': 'khushi', 'age': '20'}
key = 'name'

is_valide = True
for i in dic:
    if key in dic:
        is_valide = True
    else:
        is_valide = False
print(is_valide)

# 7. Get All Keys

dic= {'b':1, 'a':2, 'c':3, 'd':4}
key= sorted(list(dic.keys()))
print(key)


# 8. Return a list of all values in the dictionary (in insertion order).

dic= {'name': "khushi", 'roll_num':30}

val= list(dic.values())
print(val)

# 9.Merge two dictionaries. If a key exists in both, the value from the second dictionary should be kept.

first_dic= {'name': "khushi", 'roll_num':30}
second_dic = {'b':2, 'a':1, 'c':3}

new_dic = {}

for key in first_dic:
    new_dic[key] = first_dic[key]

for key in second_dic:
    new_dic[key] = second_dic[key]

print(new_dic)
# 10.Create and return a shallow copy of the given dictionary without modifying the original.

dic = {'name': "khushi", 'roll_num':30}

new_dic = dic.copy()
print("copied dictionary",new_dic)

print("original dictionary ",dic)


# 11. Return a new dictionary where keys become values and values become keys. Assume all values are unique and hashable.


dic = {'a':1, 'b':2, 'c':3, 'd':4}

new_dic = {}

for key in dic:
    value = dic[key]
    new_dic[value]= key
print(new_dic)

# 12. Given a string, return a dictionary with each word as a key and its frequency as the value.

s = 'khushi'
dic = {}
for i in range(len(s)):
    current=s[i]
    if current in dic:
        dic[current] = dic[current]+1
    else:
        dic[current] = 1
print(dic)

# 13. Return a new dictionary containing only the key-value pairs where the value is greater than a given threshold.

dic = {'b':2, 'a':1, 'c':3}
threhold = 2
new_dic ={}

for i in dic:
    if dic[i]>threhold:
        new_dic[key] = dic[i]
print("new dictionary ",new_dic)


# 14. Return a list of (key, value) tuples sorted by values in ascending order.

dic = {'b':2, 'a':1, 'c':3}

li = list(dic.items())
print(li)

for i in range(len(li)):
    for j in range(1+i,len(li)):
        if li[i][1]>li[j][1]:
            li[i],li[j] = li[j],li[i]
print(li)


# 15. Given a list of (item, category) tuples, return a dictionary mapping each category to a list of its items.



# 16. Given a nested dictionary and a list of keys, return the value found by traversing the nesting path. Return None if
# any key is missing.

dic = {'a': {'b': {'c': 42}}}
keys = ['a','b','c']
new_dic=dic

for i in keys:
    if i in new_dic:
        new_dic = new_dic[i]
    else:
        new_dic = None
print(new_dic)

# 17. Given two lists (keys and values), return a dictionary pairing them. If lengths differ, ignore extra elements.

keys = [1,2,3,4,5]
values = ['a','b','c','d']


new_dic={}

minimum_length = min(len(keys), len(values))

for i in range(minimum_length):
    k = keys[i]
    v = values[i]
    new_dic[k] = v

print(new_dic)


# 18.Return the key associated with the maximum value in the dictionary. If multiple keys share the max, return any one.

dic = {'a':13, 'b':34, 'c':35,'d':35}

max_val = dic['a']

for key,value in dic.items():
    if value>max_val:
        max_val = value
        max_key = key
print("maximum value' key",max_key)

# 19. Return a new dictionary with all key-value pairs where the value is None removed.

dic = {'a':13, 'b':34, 'h':None, 'c':35}
new_dic = {}
for key,value in list(dic.items()):
    if value is None:
        dic.pop(key)
    else:
        k = key
        v = value
        new_dic[k]=v
     
print('......new_dic')

# 20.Flatten a two-level nested dictionary into a single-level dictionary using 'parent_child' keys.

dic = { 'a': { 'x':1, 'y':2 }, 'z':3}
new_dic = {}
for key, value in dic.items():
    if type(value)== dict:
        for child_key,child_value in value.items():
            new_key = key + '_'+ child_key
            new_dic[new_key] = child_value
    else:
        new_dic[key]= value
print(new_dic)


# 21.Recursively merge two nested dictionaries. When both dicts have the same key and both values are dicts, merge
# them recursively; otherwise the second dict's value wins.

# 23. Build a Trie (prefix tree) using nested dictionaries. Implement insert(word) and search(word) returning True/False.

trie = {}

trie[1] = 'cat'
trie[2] = 'car'

search_word = 'car'
print(trie)

found = False
for word in trie:
    if search_word==trie[word]:
        found = True
    else:
        found = False
print(found)


# 24. Given a list of strings, group anagrams together using a dictionary keyed by sorted character tuple. Return list of
# groups.

li = ['eat', 'tan', 'ate', 'tea','abc', 'bca','cab','xyz','zyx']

dic = {}

for i in range(len(li)):
    key = tuple(sorted(li[i]))

    if key not in dic:
        dic[key] = []
    dic[key].append(li[i])

result = list(dic.values())
print(result)


# 25.Given a list of edges (u, v, weight), build a weighted adjacency dictionary and return the shortest path cost
# between two nodes using Dijkstra&#39;s algorithm.


edges = [('a','b', 1 ), ('b','c',2), ('a','c', 5)]

staring_point = 'a'
destination = 'b'

# 26. Implement a function that serializes a nested dictionary to a JSON-like string and another that deserializes it back.
# Handle str, int, float, bool, None, list, and dict types.

dic = {
    "name": 'khushi',
    "age": 20,
    "female": True,
    "subject": None
}

# -------------------Serialization----------------------------------

for key in dic:
    value = dic[key]
    if type(value) is bool:
        if value ==True:
            dic[key]='true'
        else:
            dic[key]='false'
    elif value is None:
            dic[key]= 'null'
    elif type(value) is str:
        dic[key] = f"{value}"

    else:
        dic[key] = str(value)
print(dic)

# 27. Implement an LRU cache with a fixed capacity using OrderedDict. Support get(key) and put(key, value)
# operations. get returns -1 for missing keys.

capacity = 2

cache = {}

# to put the key value --------
key , value = 1,1
if key in cache:
    value = cache.pop(key)
cache[key] = value

# to put the next key value --------
key, value = 2,2
if key in cache:
    value = cache.pop(key)
cache[key] = value


# capacity checker ---------

if len(cache)>capacity:
    first_key = next(iter(cache))
    del cache[first_key]

print(f"Put {key}: {value} ")


# to get the key -------

search_key = 1
if search_key in cache:
    deleted_item = cache.pop(key)
    cache[search_key] = deleted_item
    result = deleted_item
else:
    result = -1

print("get", result)

# to put the next key value 3,3 ------
key, value = 3,3
if key in cache:
    value = cache.pop(key)
cache[key] = value

# to get the key  2----

search_key = 2
if search_key in cache:
    deleted_item = cache.pop(key)
    cache[search_key] = deleted_item
    result = deleted_item
else:
    result = -1

print("get",result)

print(cache)

# 28 Write a memoize decorator using a dictionary as cache. Apply it to a recursive Fibonacci function and verify results
# with call count reduction.

fibo = 21
memorize_dic = {0:0,1:1}
counter = 0

i =2
while(i<=fibo):
    if i not in memorize_dic:
        memorize_dic[i] = memorize_dic[i-1]+memorize_dic[i-2]
        counter+=1
    i+=1
print(f"only {counter} unique calls")

print("fibonacci result",memorize_dic[fibo])
