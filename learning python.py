# For loops

for letter in "Giraffe Academy":
    print (letter)


friends = ["Carlos", "Maria", "Daniela", "Cacaita"]

for friend in friends:
    print(friend) 
    

# Exponent function
print (2**3)

# creating a function()

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range (pow_num):
        result = result * base_num
    return result

print (raise_to_power(3, 3))

## 2D LISTS &  Nested Loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][2])

# Nested for() loops

for row in number_grid:
    for col in row:
        print (col)

