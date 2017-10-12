from decimal import *
import math

print("Shop Keeper: Enter price of the Item Purchased")
p=float(input())
print("Customer : Enter money given to shop keeper")
m=float(input())
changeM= p-m
finalVal = format(changeM,'.2f')

print("Remaining change ",finalVal)


split_num = str(finalVal).split('.')
dollar = int(split_num[0])
deciNum = int(split_num[1])
#print("deciNum",deciNum)
quaters = int(deciNum/25)
cents = deciNum%25
dime = 0
if cents ==10:
    dime=cents/10
elif cents > 10:
    dime = int(cents / 10)
    cents = cents%10

print("Give below denomination to Customer")
print("dollar",dollar)
print("quaters",quaters)
print("dime",dime)
print("cents",cents)
