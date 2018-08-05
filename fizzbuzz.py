for i in range(101):
    count = i + 1
    if count % 3 and count % 5==0:
        print("fizzbuzz")
    elif count % 3 == 0:
        print("fizz")
    elif count % 5==0:
        print("buzz")
    
    else:
        print(count)
