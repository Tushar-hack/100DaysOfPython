try:
    numerator = 10
    denominator = 5
    result = numerator / denominator
    print(result)
except ZeroDivisionError as err:
    print(err)
finally:
    print("this will run anyhow.")

# Any block of code that can have error in future will be inside try block
# except block will check for the exception type and based on that do something.
# finally block will run always whether the error will occur or not.
