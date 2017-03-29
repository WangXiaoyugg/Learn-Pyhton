def square_of_sum(L):
    sum =0
    for i in L:
         x=i*i
         sum= sum +x
    return sum
    

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])