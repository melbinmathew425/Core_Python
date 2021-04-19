try:
    a=int(input("Enter a value"))
    print("a= ",a)
except:
      print("Enter a int value")
finally:#finally block is always working either try block or ecept block workin
        print("its final")