import random
def generate(n):
    if n==1:
        return str(random.random())[-4:]
    elif n==2:
        return str(random.random())[-6:]
    else:
        l = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ''.join(random.choices(l,k=6))
print('Welcome to the OTP generator\nDue to multiple choices we are bound to ask what kind of otp you want to generate\n')
print('The options are:-\n1.4 digit\n2.6 digit\n3.6 Digit alphanumeric')
n = int(input())
out = generate(n)
print(out)