#POTATO PASSWORD GENERATOR 
#Python For Beginners
#trinket.io/python/08c0ad3359
#SadraDan
import random

print """
         ===========================================
                  POTATO PASSWORD GENERATOR
                        HELL YEAAH!
         ===========================================
"""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*().,"
prompt = "Number of passwords? "
number = int(raw_input(prompt))
potato = "Password's length? "
length = int(raw_input(potato))

print "Here are your passwords: "

for pwd in range(number):
    password = '' 
    for yellow in range(length):
        password += random.choice(characters)
        print password