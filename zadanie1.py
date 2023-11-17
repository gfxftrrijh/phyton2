def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(start, end):
    print("Простые числа в диапазоне от", start, "до", end, ":")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

print_primes(start, end)