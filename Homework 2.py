def hawkID():
    return("JGronberg")





    
def q1(origString, repeatCount, lettersToRepeat):
    result = ''
    n=0
    for l in origString:
        if l.lower() in lettersToRepeat:
            result += origString[n:n] + l*repeatCount
        else:
            result += origString[n:n+1]
        n+=1
    return result


def q2(num, string1, string2):
    n=0
    total=0
    for l in string1:
        print(n)
        if string1[n] != string2[n]:
            total+=1
        n+=1
    if total == num:
        return True
    else:
        return False
        
    
            
    
def q3(inputString, minLetter, lettersToIgnore, specialLetter):
    specialIsOddlyThere = False
    count=0
    currentMinChar = minLetter
    currentIndex = 0
    smallestLetter = None
    indexOfSmallestLetter = None
    for x in inputString:
        if specialLetter == x:
            count+=1
        if count % 2 != 0:
            specialIsOddlyThere = True
        x = inputString[currentIndex]
        if (currentMinChar == None) or (x < currentMinChar):
            currentMinChar = x
            smallestLetter = currentMinChar
        currentIndex = currentIndex + 1    
    return (smallestLetter, indexOfSmallestLetter, specialIsOddlyThere) 







