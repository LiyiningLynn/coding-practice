#整理list列表的各种操作：function method 运算等以及一些注意事项
list1 = [23,12,1,24,12,31,7]
list2 = ['leo','lucky','nemo']
list3 = [[1,2],3,[4,5,6],7]
list4 = []
list = ['cat', 12, 35.8]   #mixed type element
# a list of variables we defined somewhere else 可以分行
things = [
    one_variable,
    another_variable,
    third_variable, # this trailing comma is legal in Python
]

#access using index
print(list1[0])

#slice operations
#count from the end
print(list1[-1])
#这类slice操作得到的都是片段的拷贝，原list没有变
list1[1:] #包含最后一个元素
list1[1:3]  #不含3号元素
list1[:3]
list1[:]  # a copy of the whole list
list[::2]  #use step size

'''
#modifications on original list
'''
list1.append(171)
list1.count(12)  # count how many times a value appears in the list
list1.extend([56, 2, 12])  #append several elements once at a time
list1.index(12)   #find the index of a value, if there are many, only returns the first one
list1.insert(0, 45) # insert 45 at the beginning of the list; insert a value at a particular index
my_number = list1.pop(0)  # remove an element by its index and assign it to a variable
list1.remove(12)   #remove an element by its value;if the value appears more than once, only the first one will be removed
# modify original list in place
list1.sort()
list1.reverse()


del list1[3]    #delete


'''
don't change the original list
'''
#some built-in functions:
len(list2)  # the length of a list
sum(list1)  # the sum of a list of numbers
any([1,0,1,0,1])  # are any of these values true?
all([1,0,1,0,1])  # are all of these values true?

#check existence in a list
val = 12
if val in list1:
    print val
if val not in list1:
    print 'not in'

# these return a modified copy
sorted(list1)  #original list not be changed
#reversed function actually returns a generator, not a list，
#so we have to convert it to a list before we can print the contents. 
list(reversed(numbers)) #notice the difference in names like 'sort' and 'sorted'

pet = list(list2) #pet gets a modified copy of list2, pet and list2 are different objects


'''
arithmetic operators 
'''
print([1, 2, 3] + [4, 5, 6])   #concatenate
print([1, 2, 3] * 3)    #concatenate with itself


