def findMaxInList(numbersList) :
    Maxnumber = numbersList[0]
    for num in numbersList[1:] :
        if num > Maxnumber :
            Maxnumber = num 
    return Maxnumber
# This is not doing anything when I run it.  can I please get an explanation if this is correct and if not, what's the correct way?
