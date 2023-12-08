

def prime_number_checker(number):

  num_divisors = 1
  for i in range(1, 9):
    if number % i == 0:
      num_divisors += 1
  
  if num_divisors > 2:
    print("Not prime")
  else:
    print("Prime")

  return
    
  
test_n = int(input("Enter number to test: "))
prime_number_checker(test_n)
