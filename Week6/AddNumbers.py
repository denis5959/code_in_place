def add_many_numbers(numbers):
  total_so_far = 0 
  for number in numbers:
    total_so_far+= number
  return total_so_far

numbers = [1,2,3,4,5]
sum_of_numbers = add_many_numbers(numbers)
print(sum_of_numbers)
