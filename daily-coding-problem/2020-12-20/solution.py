stripe_integers = [1,3,5,7,3,7,3,0,-5,2]

def find_lowest_integer(stripe_integers):
  lowest_integer_sorted_set = sorted(stripe_integers)
  last_number = 0
  for i in lowest_integer_sorted_set[1:]:
    if i <= 0:
      # print('aaaaaaaaa')
      pass
    else:
      if i - last_number > 1:
        # print('>1',i, last_number)
        return last_number+1
      else:
        # print('<1',i, last_number)
        last_number = i
  return last_number + 1


print(find_lowest_integer(stripe_integers))
print(find_lowest_integer([0,1,3,7,-9,-5,-6,-3,0,-9,13,5,6,3,2,2,2,1,0,3,-1]))
print(find_lowest_integer([3, 4, -1, 1]))
print(find_lowest_integer([1, 2, 0]))
