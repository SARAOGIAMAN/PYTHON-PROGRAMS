def reverse(s):
    revstr=""   
    for i in s:
        revstr=i+revstr
    print(revstr)

s=input("Enter the string:")
reverse(s)
