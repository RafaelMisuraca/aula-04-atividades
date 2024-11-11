horario = float(input("Digite aqui seu horário: "))

def saudacao(horario):
    if  0 <= horario <= 12:
        print("Bom Dia!")
    elif 12 < horario <=18:
        print("Boa tarde!")
    elif 18 < horario <= 24:
        print("Boa noite!")
    else:
        print("Horário desejado é inválido, tente novamente.")

saudacao(horario)