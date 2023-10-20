
"""

- A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
- RegEx can be used to check if a string contains the specified search pattern.
- The re module offers a set of functions that allows us to search a string for a match
- Python has a built-in package called re, which can be used to work with Regular Expressions.

findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string
"""






import re
# Regular Expression : special sequence of charecters that uses serach pattern to find a string or set of strings
# Example text containing email addresses
text = "Contact us at support@example.com or info@website.net for assistance."

# Define a pattern to match email addresses
pattern = r'\b[\w\.-[+@[\w\.-]+\.\w+\b'

#Find all email addresses in the text
matches = re.findall(pattern, text)

#Print the matches
for match in matches:
    print("Email:", match)

# extractiong dates :
import re
number = "sscscscs"

pattern = r'\d{4}-\d{2}-\d{2}'

match = re.search(pattern,number)
if match:
    print("date:",match.group)

# META CHARECTERS :
# (\) Use to drop the special meaning charecter
import re
a= "hetv.i@gmail.com"
match = re.search(r"\.",a) #output : <re.Match object; span=(4, 5), match='.'>
print(match)
# ([]) Represent a charecter class
b = "hello"
match = re.search(r"[l]",b)
print (match)# output:<re.Match object; span=(3, 4), match='l'>

# (^)  matches the beginning
c = "hetvi@gmail.com"
match = re.search(r"^het",c)   #<re.Match object; span=(0, 3), match='het'>
print(match)

# ($) matches to the end
d = "hello.world@gmail.com"
match = re.search(r"com$", d) #output : <re.Match object; span=(18, 21), match='com'>
print(match)

# (.) matches any charecter except newline
e = "charlie chaplin and the chocolate factory"
match = re.findall(r"c.a", e) #output : ['cha', 'cha']
print(match)

# (|) Means or
e = "charlie chaplin and the chocolate factory"
match = re.findall(r"cha|fac", e) #output : ['cha', 'cha', 'fac]
print(match)

# (?) Matches zero or one
e = "charlie chaplin and the chocolate factory"
match = re.findall(r"th?e", e) #output : ['the', 'te']
print(match)

# (*) any number of occurence (o also)
e = "charlie chachaplin and the chocolate factory"
match = re.findall(r"ch?a", e) #output : ['cha', 'cha', 'cha']
print(match)

# (+) one or more occurences no matter how many time one word occurs
e = "abc,aba,aabbc,accb,aabc,aabb"
match = re.findall(r"ab+c", e) #output :['abc', 'abbc', 'abc']
print(match)

# ({}) it will show how many time one word is there in string
e = "abc,ab,abbc,accb,aabc,aabb"
match = re.findall(r"a{1,4}", e) #output :['a', 'a', 'a', 'a', 'aa', 'aa']
print(match)

# (()) enclose a group of regex
e = "abc,bc,abcc,aabbc,cac,abcabc"
match = re.findall(r"(a|c)bc", e) #output :['a', 'a', 'a', 'a', 'aa', 'aa']
print(match)

# Split : Function return a list where the string has been split at each match

import re

txt = "hello good morning"
x = re.split("\s", txt)
print(x)

# Replace every white-space character with the number 9:

import re

txt = "hello good morning"
x = re.sub("\s", "!", txt)
print(x)




"""
    []	A set of characters	"[a-m]"	
    \	Signals a special sequence (can also be used to escape special characters)	"\d"	
    .	Any character (except newline character)	"he..o"	
    ^	Starts with	"^hello"	
    $	Ends with	"planet$"	
    *	Zero or more occurrences	"he.*o"	
    +	One or more occurrences	"he.+o"	
    ?	Zero or one occurrences	"he.?o"	
    {}	Exactly the specified number of occurrences	"he.{2}o"	
    |	Either or	"falls|stays"	
    ()	Capture and group	 	 
    Special Sequences
    A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
    
    Character	Description	Example	Try it
    \A - Returns a match if the specified characters are at the beginning of the string	"\AThe"	
    \b - Returns a match where the specified characters are at the beginning or at the end of a word
    (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
    r"ain\b"	
    \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
    (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
    r"ain\B"	
    \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
    \D	Returns a match where the string DOES NOT contain digits	"\D"	
    \s	Returns a match where the string contains a white space character	"\s"	
    \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
    \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
    \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
    \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	
    Sets
    A set is a set of characters inside a pair of square brackets [] with a special meaning:
    
    Set	Description	: A set is a set of characters inside a pair of square brackets [] with a special meaning
    
    [arn] -	Returns a match where one of the specified characters (a, r, or n) is present	
    [a-n] -	Returns a match for any lower case character, alphabetically between a and n	
    [^arn] -	Returns a match for any character EXCEPT a, r, and n	
    [0123] - Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
    [0-9] -	Returns a match for any digit between 0 and 9	
    [0-5][0-9] - Returns a match for any two-digit numbers from 00 and 59	
    [a-zA-Z] - Returns a match for any character alphabetically between a and z, lower case OR upper case	
    [+] - In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

"""