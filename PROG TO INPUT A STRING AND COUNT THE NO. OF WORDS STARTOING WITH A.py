def c_upper(text, char):
   text = text.title() #set leading char of words to uppercase
   char = char.upper() #set given char to uppercase
   k = 0 #counter
   for i in text:
     if i.istitle() and i == char: #checking conditions for problem, where i is a char in a given string
        k = k + 1
   return k
print("NUMBER OF WORDS ARE  ",c_upper("aman dghf aamabh fdhkfhzkjh ana JSAJfdlkjL SAJFLKVK ASJjdj", 'a'))
