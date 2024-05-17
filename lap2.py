

x = int(input("Please enter number x"))
y = int(input("Please enter number y"))
op = input("operator + - * /: ")

result = {
    "+" : lambda x, y :x+y,
    "-" : lambda x, y :x-y,
    "*" : lambda x,y : x*y,
    "/" : lambda x,y : x/y
}

def add(x,y):
    return x + y
add = lambda x,y : x + y

print(result[op](x,y))