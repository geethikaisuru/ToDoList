new_member = input("Add a new member: ") + "\n"   # Gets a new member to memory
file = open(r"C:\Users\LENOVO\Downloads\members.txt", 'r')
members = file.readlines()
file.close()
members.append(new_member)\

file = open(r"C:\Users\LENOVO\Downloads\members.txt", 'w')  
file.writelines(members)
file.close()