# Write a function that returns all the prime numbers up to an inputted number
# (**Hint**: It might be helpful to use/modify the prime function you wrote earlier).

def check_if_prime(n):

    is_a_prime = True
    divides_by = 0

    for index in range(2,n):
        if n % index == 0:
            return False

    return True


def number_of_primes_up_to(n):

    total = 0

    for num in range(2,n):

        if check_if_prime(num) is True:
            total += 1

    return total


input_number = int(raw_input("Enter a number to be tested: "))
print "The number of primes up to {} is {}".format(input_number,number_of_primes_up_to(input_number))
