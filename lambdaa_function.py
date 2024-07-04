#syntax
#lambda params : expression

add = lambda x,y:x+y
multiply = lambda x,y,z:(x*y)+z
full_name = lambda fname,lname:fname+" "+lname
age_check = lambda age:"Eligible for voting!!" if age >= 18 else "Not eligible for voting"

print(age_check(44))