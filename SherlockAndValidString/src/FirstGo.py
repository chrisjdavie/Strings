'''
Solving the hackerrank puzzle Sherlock and Valid String

https://www.hackerrank.com/challenges/sherlock-and-valid-string

This is classified as "difficult", but it doesn't look it from the start. But neither did "Morgan and a String", and that was a complete pain.

My solution is more rigourous than the test cases, it turns out.

----------------------

You know my powers, my dear Watson, and yet at the end of three months I was forced to confess that I had at last met an antagonist who was my intellectual equal.

A "valid" string is a string S such that for all distinct characters in S each such character occurs the same number of times in S.

For example, aabb is a valid string because the frequency of both characters a and b is 2, whereas aabbc is not a valid string because the frequency of characters a, b, and c is not the same.

Watson gives a string S to Sherlock and asks him to remove some characters from the string such that the new string is a "valid" string.

Sherlock wants to know from you if it's possible to be done with less than or equal to one removal.

Input Format

The first and only line contains S, the string Watson gives to Sherlock.

Output Format

Output YES if string S can be converted to a "valid" string by removing less than or equal to one character. 
Else, output NO.

----------------------

Created on 25 Jan 2016

@author: chris
'''


# load inputs
stringIn = raw_input().strip()

# count characters
charCounts = {}
for char in stringIn:
    try:
        charCounts[char] += 1
    except KeyError:
        charCounts[char] = 1

# Find the frequency (to find the modal value)
freqArr = {}
for val in charCounts.values():
    try:
        freqArr[val] += 1
    except KeyError:
        freqArr[val] = 1

# if there a single character with one count, it
# can (and should) be removed to see if the string
# is valid
Dv = 1
try:
    if freqArr[1] == 1:
        for char in charCounts:
            if charCounts[char] == 1:
                break
        charCounts.pop(char)
        Dv = 0
except KeyError:
    pass

# the modal value (the most common value will be the one
# for which the variance away from it is lowest, in terms
# of searching for a single charater deletion)

val0 = max(freqArr, key=freqArr.get)

# finally, search for characters to be eliminated
for val in charCounts.values():
    Dv -= abs(val-val0)
    if Dv < 0:
        print "NO"
        break
else:
    print "YES"

    
    
