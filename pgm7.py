#if else
#age> 18-> watch a movie
#age< 18-> not allowed to watch movie

x=5
y=10

max_val=x if x>y else y
print(max_val)

age=input("Enter your age\n")
age=int(age)

result= "Yes, you can watch movie" if age > 18 else "No,wait patiencely till the right age"
print(result)