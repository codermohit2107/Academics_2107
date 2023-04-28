import random
def generate():
    n = random.randint(8,12)
    l = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
    return ''.join(random.choices(l,k=n))
print("The generated OTP is ",generate())