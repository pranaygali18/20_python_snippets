# 20 python snippets


# 01 reverse a string

str1 = 'hello world'
reversed_str = str1[::-1]
print(reversed_str,'#Reversing a String')


# 02 checking a string contains a substring

str2 = 'hello world'
substr = 'world'
if substr in str2:
    print('Found Substring')
else:
    print('Not Found')


# 03 finding the maximum value in the list4

my_list = [2,5,8,9,6,1,4]
max_value = max(my_list)
print('The Maximun value is:',max_value)



# 04 finding the index of the maximum value in the list:

my_list1 = [2,5,8,9,6,1,4] # [0,1,2,3,4,5,6]
max_index = my_list1.index(max(my_list1))
print('The index of maximum value is:',max_index) # 3


# 05 Reversing the list

my_list2 = [2,5,8,9,6,1,4]
reversed_list = my_list2[::-1]
print('Reversing the list',reversed_list)


# 06 removing duplicates form the list

my_dup_list = [2,5,8,9,6,1,4,5,6,8]
remove_dup = list(set(my_dup_list))
print('Removed Duplicates from the list:',remove_dup)


# 07 checking if a list is empty

my_empty_list = [] # the brackets are empty
if not my_empty_list:
    print('list is empty')
else:
    print('list had some value')


# 08 converting a string in to a list

my_str = 'Hello World'
convrt_list = list(my_str)
print('Converted string to a list',convrt_list)


# 09 sorting a dictionary by value

my_dic = {'apple': 3,'banana':1,'orange':2}
sorted_dic = dict(sorted(my_dic.items(), key=lambda item: item[1]))
# Displaying the sorted dictionary
print('After Sorted',sorted_dic)


# 10 checking if a file exists

import os
if os.path.isfile('main.py'):
    print('File Existed')
else:
    print("File doesn't exists")


# 11 counting occurrences of an item in a list

my_list3 = [1,5,5,8,8,9,5,7,5]
count_list = my_list3.count(5) # 4
print('Counting the 5 number how many times came:',count_list)


# 12 checking if all elements in a list are unique

my_list4 = [1,2,3,4,5,6]
if len(my_list4) == len(set(my_list4)):
    print('All elements are Unique')
else:
    print('some changes')


# 13 Removing all occurrences of an item from a list

my_list5 = [1,2,3,2,1,4,5,4]
item = 2
my_list5 = [x for x in my_list5 if x != item]
print('The Number 2 will be removed',my_list5)


# 14 Flattening a nested list

my_nst_list = [[1,2],[3,4],[5,6]]
flattening_list = [x for sublist in my_nst_list for x in sublist]
print(flattening_list)


# 15 Merging two dictionaries

dict1 = {'apple':2,'banana':1}
dict2 = {'graps':5, 'orange':3}
merged_dict = {**dict1, **dict2}
print('After Merged',merged_dict)


# 16 Removing all whitespaces from a string

my_str = ' h e llo   wor    l    d'
new_str = ''.join(my_str.split())
print('After Removing White Spaces',new_str)


# 17 checking if a string is a palindrome
# palindrome means smallletters

my_string = 'racecar'
if my_string == my_string[::-1]:
    print('yes')
else:
    print('no')


# 18 removing duplicates from a string

my_dup_str = 'hello world'
new_dup = ''.join(set(my_dup_str))
print('After Removing Duplicates from a string',new_dup)


# 19 counting the numbers of words in a string

my_str_count = 'Hello World'
word_count = len(my_str_count.split())
print('After Counting the words in a string',word_count)


# 20Generating a random integer

import random
random_numb = random.randint(1,10)
print('The Random number is:',random_numb)