def is_prime(n):
    if n <= 1:
        return False
    elif n in [2, 3, 5]:
        return True
    elif n % 2 is 0 or n % 5 is 0:
        return False
    else:
        end_digit = [1, 3, 7, 9]
        index = 10
        third = n / 3.
        while index < third:
            for digit in end_digit:
                if n % (index + digit) is 0:
                    return False
            index += 10
        return True


def primes(n):
    prime_list = [2, 3, 5, 7]
    end_digit = [1, 3, 7, 9]

    index = 10
    while index < n:
        for digit in end_digit:
            if is_prime(index + digit):
                prime_list.append(index+digit)
        index += 10
    return prime_list
