def hawkID():
    return("JGronberg")


def q1 (num):
    if(num%2!=0 and num%7!=0 and num%14!=0):
        return 0
    elif(num%2==0 and num%14!=0):
        return 2
    elif(num%7==0 and num%14!=0):
        return 7
    else:
        return 14
    return


def q2(n):
    result=0
    final=0
    if(n==0):
        return 0
    while(n>0):
        result=q1(n)
        final+=result
        #print(n)
        n-=1
    return final




def sumDigitsOf(number):
    digit=0
    sum=0
    newNumber=0
    while(number!=0):
        digit=number%10
        sum+=digit
        newNumber=number//10
        number=newNumber
    return sum



    

 