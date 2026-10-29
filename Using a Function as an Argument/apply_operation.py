
def apply_operation(func,number):
   return func(number)

def double(number):
   return number * 2

def square(number):
   return number ** 2

result_double = apply_operation(double,7)
print(result_double)

result_square = apply_operation(square,3)
print(result_square)



 
    