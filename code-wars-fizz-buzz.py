# DESCRIPTION:
# Return an array containing the numbers from 1 to N, where N is the parametered value.

# Replace certain values however if any of the following conditions are met:

# If the value is a multiple of 3: use the value "Fizz" instead
# If the value is a multiple of 5: use the value "Buzz" instead
# If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
# N will never be less than 1.

# Method calling example:

# fizzbuzz(3) -->  [1, 2, "Fizz"]
def fizzbuzz(n):
    # PREP
    #P value
    # R is value is multiple of 3: range numbers, and on value that is multiple of 3 >fiizz

    # value is multiple of 5: range number and if number is multiple of 5  "buzz"
    # if value is multiple of 3 & 5, "FizzBuzz"
    
    fizzify = [i + 1 for i in range(n)]
    
    for i in range(len(fizzify)):
        if fizzify[i] % 3 == 0 and fizzify[i] % 5 == 0:
            fizzify[i] = "FizzBuzz"
        elif fizzify[i] % 3 == 0:
            fizzify[i] =  "Fizz"
        elif fizzify[i] % 5 == 0:
            fizzify[i] = "Buzz"
        else:
            continue
    return fizzify
