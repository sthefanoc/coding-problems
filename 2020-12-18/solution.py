numbers = [10, 15, 3, 7]
k = 24

def find_k_sum(numbers, k):
  for i,num in enumerate(numbers):
    target = k-num
    numbers_clean = [n for j,n in enumerate(numbers) if j != i]
    if target in numbers_clean:
      return True
  return False

print(find_k_sum(numbers, k))
