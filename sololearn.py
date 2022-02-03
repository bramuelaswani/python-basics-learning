from sympy import prime


if 1 + 1 == 2:
    if 2 * 2 == 8:
        print("if")
    else:
        print("else")
print(2*2)

if not True:
    print("1")
elif not (1 + 1 == 3):
    print("2")
else:
    print("3")

if 1 + 1 * 3 == 6:
    print("Yes")
else:
    print("No")

x = 4
y = 2
if not 1 + 1 == y or x == 4 and 7 == 8:
    print("Yes")
elif x > y:
    print("No")

nums = [5, 4, 3, 2, 1]
print(nums[1])
4

print(len([2, ]))

x = "hello world!"
print(x[6])
x

num = [5, 4, 3, [2], 1]
print(num[0])
print(num[3][0])
print(num[4])

# lists change
nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])

# in lists
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])
