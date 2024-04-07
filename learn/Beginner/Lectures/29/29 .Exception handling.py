# Exception = events detected during exception that interrupt the flow of program

try:
    number = int(input("Enter the number value to divide : "))
    _divided_by = int(input("Enter the number value to divide by : "))
    result = number / _divided_by #4/4 = 1 result = 1

except Exception as e:
    print(e)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print(int(result))  # 1.0 => 1
finally:
    print("Thanks Good job.")
