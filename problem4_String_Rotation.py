'''
Given two words, find if second word is the round rotation of first word.
For example: abc, cab
return 1
since cab is round rotation of abc
'''

string1="abc"
string2="cab"
temp =''

def IsRotation(string1,string2):
    if len(string1)!=len(string2):
        return 0
    else:
        temp=string1 + string1
        if (temp.count(string2)> 0):
            return 1
        else:
            return 0

if IsRotation(string1,string2):
    print "Strings are round rotations of each other"
else:
    print "Strings are not round rotations of each other"
