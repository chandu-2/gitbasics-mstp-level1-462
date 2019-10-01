def addition(a,b):
    c= a+b
    print(c) 
def primeno(s):
    temp=0
    for i in range (1,s+1):
        if (s%i==0):
            temp=temp+1
    if temp==2:
        return True
    else:
        return False
           