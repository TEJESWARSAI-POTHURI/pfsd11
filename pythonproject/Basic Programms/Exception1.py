while True:
    try:
        n=int(input("Please enter an integer: "))
        m=int (input("Please enter an integer: "))
        z=n/m
        break

    except Exception as e:
        print("Not an Integer")
        print(e)
    except ValueError:
        print("Not an Integer! Value Error")
    finally:
        print("You have successfully entered an integer!")