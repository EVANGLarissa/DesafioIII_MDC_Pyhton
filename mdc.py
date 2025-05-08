# Solicitar entrada dos números ao usuário
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

fatores_num1 = []
fatores_num2 = []

# função de fatoração
divisor = 2
while num1 > 1:
    while num1 % divisor == 0:
        fatores_num1.append(divisor)
        num1 //= divisor
    divisor += 1
divisor = 2
while num2 > 1:
    while num2 % divisor == 0:
        fatores_num2.append(divisor)
        num2 //= divisor
    divisor += 1

# array
fatores_comuns = []
for fator in fatores_num1:
    if fator in fatores_num2:
        fatores_comuns.append(fator)
        fatores_num2.remove(fator)

mdc = 1
for fator in fatores_comuns:
    mdc *= fator

# console.log do js
print(f"Fatores: {fatores_comuns}")
print(f"MDC: {mdc}")