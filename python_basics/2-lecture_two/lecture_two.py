str = 'learn python'
print(str[1:4])

str1 = 'learn flask'
print(str1[-13:-1])

print(str.endswith('on'))

first_name = input("Enter First Name: ")

print(len(first_name))

count_value = "I am learning python."
print(count_value.count('n'))

age = 12

if(age >= 18):
    print("Eligible...")
elif(age<18):
    print("Not Eligible...")    
else:
    print("Break...")

test_even = int(input("Enter a number: ")) 

if(test_even % 2 == 0):
    print(test_even, "Is an Even Number")
else: 
    print(test_even, "Is an Odd Number")