password = input("Please Enter your Password:")

result = []

if len(password) > 7:
    result.append(True)    
else:
    result.append(False)

digit = False  
for i in password:
    if i.isdigit() == True:
        digit = True
        continue
if digit == True:
    result.append(True)
else : 
    result.append(False)


upperCase = False  
for i in password:
    if i.isupper() == True:
        upperCase = True
        continue
if upperCase == True:
    result.append(True)
else : 
    result.append(False)

if all(result):
    print("Strong Password")

else:
    print("Not a Strong one")