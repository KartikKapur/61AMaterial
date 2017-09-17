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
