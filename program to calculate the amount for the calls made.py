amt=1
call=int(input("enter the no. of calls "))
if call<=100:
    print("no amount to be paid ")
elif(call>100) and (call<=200):
    amt=amt*call*1
    print("your amount is ",amt)
elif(call>200) and (call<=300):
    amt=amt*call*2
    print("your amount is ",amt) 
elif(call>300) and (call<=400):
    amt=amt*call*3
    print("your amount is ",amt)
elif(call>400):
    amt=amt*call*5
    print("your amount is ",amt)
