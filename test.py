string = "Hey! What's up?"
characters = "'!?"

string = ''.join( x for x in string if x not in characters)
print(string)