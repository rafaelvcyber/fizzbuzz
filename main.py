limit = 1000
counter = 1
while counter <= limit:
    if counter % 5 == 0 and counter % 15 == 0:
        print("fizzbuzz")   
    elif counter % 15 == 0:
        print("buzz")
    elif counter % 5 == 0:
        print("fizz")
    else:
        print(counter)
    counter += 1