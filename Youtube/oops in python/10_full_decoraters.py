import time as t

def example_function(func):
    def wrapper(*args):
        start=t.time()
        result=func(*args)
        end=t.time()
        print(f"{func.__name__} range in {end-start} time")
        return result
    return wrapper

@example_function
def greet(n):
    t.sleep(n)

greet(2)