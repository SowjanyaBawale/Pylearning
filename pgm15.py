# Continue
#To find the even numbers
for num in range(1, 10):
    if num % 2 == 0:
        print("Found even Number", num)
        print(f"Found even Number {num}")
        continue
    print("Odd number Found", num)
#To skip the vallues
for i in range(1,10):
    if i == 5:
        pass
    else:
        print(i)