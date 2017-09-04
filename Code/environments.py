peanut = butter = "crunchy"
jelly = "strawberry"


def sandwich(butter, bread):
    if (len(bread) > len(butter) and len(butter) != 0):
        return sandwich(butter[1:], bread + butter[0])
    return bread


sandwich(peanut + " ", jelly)



peanut = butter = "crunchy" #global variables
jelly = "strawberry" #global variable
def sandwich(butter, bread): #function name
    if (len(bread) > len(butter) and len(butter) != 0): #conditional
        return sandwich(butter[1:], bread + butter[0]) #recursive call
    return bread #return statement


sandwich(peanut + " ", jelly) #function call
