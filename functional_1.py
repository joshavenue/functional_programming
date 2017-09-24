def apply_twice(func, arg):
   return func(func(arg))

def add_five(x):
   return x + 5

print(apply_twice(add_five, 10))

## This is more like math-related program
## f(f(x)) => add_five(add_five(10))
## f(f(x)) => x + 5 ( x + 5 ( 10 ) )
## f(f(x)) => x + 10 + 10
## f(f(x)) => x = 20
## Requires knowledge on composition of function -> more info : http://www.purplemath.com/modules/fcncomp2.htm
