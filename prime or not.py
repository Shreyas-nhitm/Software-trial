n=int(input('Enter the number to check prime or not'))
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False
        else: return True
if not check_prime(n):
    print("The number is prime")
else:
    print("The number is not prime")