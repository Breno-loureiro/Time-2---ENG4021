from divide import divide 
from multiplica import multiplica
from soma import soma 
from subtrai import subtrai 

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Escolha uma operação: ")

if operacao == "1":
  resultado = soma(n1,n2)
elif operacao == "2":
  resultado = subtrai(n1,n2)
elif operacao == "3":
  resultado = multiplica (n1,n2)
elif operacao == "4":
  resultado = divide (n1,n2)

print (resultado)
