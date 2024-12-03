def mod_numbers(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return mod_numbers(n2,n1%n2)
print(mod_numbers(516,188))