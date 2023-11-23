
no1 = int(input("Enter the 1st no"))
no2 = int(input("Enter the 2nd no"))

try:
    no3 = no1/no2
    print("Division is =",no3)
except Exception as e:
    print("Exception =",e)

# except ZeroDivisionError:
#     print("Divide by zero Exception")

else:
    print("Else block code")