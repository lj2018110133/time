from functools import wraps
def decorator_name(f):
   @wraps(f)
   def decorator(*args,**kwargs):
       if not can_run:
           return "Funtion is run"
       return f(*args,**kwargs)
   return decorator

@decorator_name
def func():
    return  "yes is runing"

can_run = False
print(func())
# Output: Function is running

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


result = addition_func(4)
print(result)

if __name__ == '__main__':
    print(addition_func(5))