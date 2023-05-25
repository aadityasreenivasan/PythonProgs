def fizbuzz(n: int):
    """
    param: n- integer until fiuzzbuzz game will run
    """
    #taking numbers starting from 0 to n
    for fbz in range(n+1):

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