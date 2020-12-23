sequence = [1,2,3,4,5]

total_product = 1
for n in sequence:
    total_product = total_product*n
    print(total_product)

new_sequence = [int(total_product/num) for num in sequence]
print(new_sequence)

#What if you can't use dividion?

from functools import reduce

total_product = reduce(lambda x,y: x*y, sequence)

final_list = []
for i in range(len(sequence)):
    mod_sequence = [num for j,num in enumerate(sequence) if j!=i]
    final_list.append(reduce(lambda x,y: x*y, mod_sequence))

print(final_list)
