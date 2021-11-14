user_play = "y"

while user_play == "y":
    numbers = int(input("How many numbers?"))

    for x in range(numbers):
        print(x)
    
user_play = input("Continue: (y)es or (n)o?")

