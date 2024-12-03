def mult_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+mult_numbers(n1,n2-1)
print(mult_numbers(4,5))