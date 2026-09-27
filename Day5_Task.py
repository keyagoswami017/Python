import random

letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']']
num = ['1','2','3','4','5','6','7','8','9']


print("Welcome to the PyPassword Generator!\n")
get_letters = int(input("How many letters would you like in your password?\n"))
get_symbols = int(input("How many symbols would you like?\n"))
get_num = int(input("How many numbers would you like?\n"))

password = ""
password_list = []

for i in range(1, get_letters + 1):
    #password += random.choice(letters)
    password_list.append(random.choice(letters))

for j in range(1,get_symbols + 1):
    #password += random.choice(symbols)
    password_list.append(random.choice(symbols))

for k in range(0, get_num):
    #password += random.choice(num)
    password_list.append(random.choice(num))

#print('Password is: ',password)
print(password_list)
random.shuffle(password_list)
print('Password List is: ',password_list)

passw = ""
for i in password_list:
    passw += i

print(passw)






