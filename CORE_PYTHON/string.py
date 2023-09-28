# captitalize() : first string capitle

str = "hey i m artist"
print(str.capitalize()) 

# casefold () all letters small

str = "hey i m aRtist"
print(str.casefold()) 

# center () it will add # on left n right side 

str = "hey i m artist"
print(str.center(20,'#')) 

# count() : count the num of word

str = "hey ,hey i m artist"
print(str.count("hey")) 

# find() it will find text

str = "hey i m artist"
print(str.find("i")) 

#endwith () it will show ending word

str = "hey i m artist"
print(str.endswith("artist")) 

#expandtabs() makes space

str = "h\te\ty\ti\tm\t artist"
print(str.expandtabs()) 

#index()

str = "hey i m artist"
print(str.index("i"))
print(str.index("i", 2, 6)) 
