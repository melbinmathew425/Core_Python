while True:
    try:
        age=int(input("Enter your age"))
        print(age)
        10/age
    except ValueError:
        print("Enter a proper no.")
    except ZeroDivisionError:
        print("Enter a no greater than zero.")
    else:
        print("thank you")
        break