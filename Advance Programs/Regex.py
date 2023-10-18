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
