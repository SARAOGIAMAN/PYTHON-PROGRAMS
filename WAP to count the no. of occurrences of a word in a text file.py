c=0
input1=input("enter the word to be searched in a file:")
file=open("file1.txt","r")
words=file.read().split(" ")
for i in words:
    if (input1==i) :
        c=c+1
print(c)
file.close()
