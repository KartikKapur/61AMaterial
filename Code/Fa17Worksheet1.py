#Question about environments
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


#Enviornment Diagram Question
karty, party = 5, 10
def kart(ik):
    kart = ik(karty)
    while kart:
        def ik():
            return lambda kario, mart: 10
        party = kart
        kar = True == 6
    return ik
karty = lambda party: karty + kart(party)
karty = karty(kart)



#Tree Recursion Problem
def twos(n):
    if(n<=1):
        return 1
    power_of_two= 2
    total = 0
    while(power_of_two <=n):
        total += twos(n/power_of_two)
        power_of_two *= 2
    return total
print(twos(8))
