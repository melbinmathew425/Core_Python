while True:
    try:
        age=int(input("whats your age "))
        a=10/age
        print(a)
    except ZeroDivisionError:
        print("Enter the age")
        continue
    finally:
        print("its ok. you are done")
        break
