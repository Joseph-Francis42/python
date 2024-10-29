check_prime=int(input("Enter a number:"))
for i in range(2,(check_prime//2)+1):
    if check_prime%i==0:
        break
if i==check_prime//2:
        print(f"the numbe {check_prime} is a prime number")
else:
   print(f"The number {check_prime} is not a prime number")