
def is_prime(num):
    if num <= 1:
        return False
    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_upto_n(n):
    print(f"Prime numbers up to {n}:")
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=" ")
    print() # Newline at the end

# Example usage:
if __name__ == "__main__":
    try:
        n = int(input("Enter a number (n): "))
        print_primes_upto_n(n)
    except ValueError:
        print("Please enter a valid integer.")
