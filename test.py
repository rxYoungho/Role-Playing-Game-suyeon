


# (3*1) + (3*2) + (3*3) + ... - money = result 

price = 3
count = 4
money = 20


total = 0 # 3, 
for i in range(1,count + 1):
    total = total + price * i
    
    print(total)
    # total = 0 + 3, i = 1
    # total = 3 + 6, i = 2
    # total = 9 + 9, i = 3
    # total = 18 + 12, i =4

print(total)