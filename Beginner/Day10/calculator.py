def add(n1,n2):
    return n1 + n2

def subtrac(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operation = {
"+":add,
"-":subtrac,
"*": multiply,
"/": divide
}

# def operation(n1,n2,op):
#     if op == "+":
#         return n1 + n2
#     elif op == "-":
#         return n1-n2
#     elif op == "*":
#         return n1*n2
#     else:
#         return n1/n2
def calculation():
    n1 = int(input("Write a number: "))
    n2 = int(input("Write a second number: "))

    print ("Choose a operation: ")
    for o in operation:
        print(o)
    op = input("Write the operation :")
    result = operation[op](n1,n2)
    print(f"{n1} {op} {n2} = {result}")
    # print(operation(n1,n2,op))
    cont = True
    while cont:
        continuar = input("Do you want continue Y/N: ").lower()
        if continuar == "y":
            op = input("Write the operation: ")
            n3 = int(input("Write a number: "))
            result_1 = operation[op](result, n3)
            print(f"{result} {op} {n3} = {result_1}")
            result = result_1
        else:
            calculation()
calculation()
