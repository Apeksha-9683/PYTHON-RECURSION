def sum_nat(n):
    if n==0:
        return 0
    return sum_nat(n-1)+n
print(sum_nat(int(input("Enter a number to be displayed its sum of natural numbers:"))))