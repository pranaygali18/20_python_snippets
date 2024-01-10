# 20 python snippets

# 01 reverse a string

str1 = 'hello world'
reversed_str = str1[::-1]
print(reversed_str)

# 02 checking a string contains a substring

str2 = 'hello world'
substr = 'world'
if substr in str2:
    print('Found Substring')
else:
    print('Not Found')

# 03 finding the maximum value in the list
my_list = [2,5,8,9,6,1,4]
max_value = max(my_list)
print(max_value)

# 04 finding the index of the maximum value in the list
my_list1 = [2,5,8,9,6,1,4] # [0,1,2,3,4,5,6]
max_index = my_list1.index(max(my_list1))
print(max_index) # 3

# 05 Reversing the list

my_list2 = [2,5,8,9,6,1,4]
reversed_list = my_list2[::-1]
print(reversed_list)

# 06 removing duplicates form the list
my_dup_list = [2,5,8,9,6,1,4,5,6,8]
remove_dup = list(set(my_dup_list))
print(remove_dup)

# 07 checking if a list is empty
my_empty_list = []
if not my_empty_list:
    print('list is empty')
else:
    print('list had some value')

# 08 converting a string in to a list
my_str = 'Hello World'
convrt_list = list(my_str)
print(convrt_list)

# 09 sorting a dictionary by value

my_dic = {'apple': 3,'banana':1,'orange':2}
sorted_dic = dict(sorted(my_dic.items(), key=lambda item: item[1]))
# Displaying the sorted dictionary
print(sorted_dic)

# 10 checking if a file exists

