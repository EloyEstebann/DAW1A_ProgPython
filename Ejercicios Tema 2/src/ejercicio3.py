def calculadora(num1,num2):
    if num2 == 0:
        return "Error!!"
    else: 
        return num1/num2


if __name__ == "__main__":
    
    num1 = int(input("Introduce el dividendo: "))
    num2 = int(input("Introduce el divisor: "))

    print(calculadora(num1,num2))