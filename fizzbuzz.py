import sys

order_of_succession = sys.argv
order_of_succession.pop(0)

for item in order_of_succession:
    a=int(item)%3
    b=int(item)%5
    if a==0 and b==0:
        print("fizzbuzz")
    elif a==0:
        print("fizz")
    elif b==0:
        print("buzz")
    else:
        print(item)
