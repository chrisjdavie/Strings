'''
Created on 26 Jan 2016

@author: chris
'''
# checking tuples are ordered
a = (1,2)
print a
b = (2,1)
print b
print a == b

# checking tuples are hashable
dict1 = {}
dict1[a] = 2
dict1[b] = 3

print dict1

# checking sets store tuples as hashable uniques 

c = set()
c.add(a)
c.add(b)

print c

# these are all consistent, and therefore can be 
# used to simplify the calculations and memory
# use without me having to define data structures, 
# which is nice