def fizbuzz():
    for fbz in range(50):
        if fbz%3==0 and fbz%5==0:
            print("FizzBuzz")
            continue

        elif fbz%3==0:
            print("Fizz")
            continue

        elif fbz%5==0:
            print("Buzz")
            continue
        print(fbz)