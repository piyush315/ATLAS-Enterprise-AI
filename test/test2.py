from functools import lru_cache

@lru_cache(maxsize=128)
def square(n):
    print("Calculating...")
    return n * n

@lru_cache(maxsize=20)
def another_calculation(n):
    print("working....")
    return n * 5


print(square(5))
print(square(5))
print(square(5))
print(square(5))
print(square(10))
print(square(5))
print(square(10))
print(square(5))

print(another_calculation(10))
print(another_calculation(20))
print(another_calculation(20))
print(another_calculation(20))
print(another_calculation(20))