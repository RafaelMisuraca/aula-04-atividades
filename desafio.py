def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b 

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return "Erro: Divisão por zero" if b == 0 else a / b

print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. sair")
opcao = int(input("Insira sua opção: "))
a = float(input("Insira um número: "))
b = float(input("Insira um outro número: "))

if opcao == "1":
    print(somar(a, b))


