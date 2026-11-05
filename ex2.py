
nome_usuario = input("Digite seu nome")
print(f"Meu nome e {nome_usuario}")
idade_usuario = input("Digite sua idade")
print(f"O usuario {nome_usuario} possui {idade_usuario} anos de idade")


nome_usuario2 = input("Digite seu nome")
idade2 = input("Digite sua idade")
print(f"O usuario {nome_usuario2} possui {idade2} anos de idade")

soma = int(idade_usuario) + int(idade2)
print(f"A soma das idades e {soma}")

salario1 = input("Digite o salario do funcionario 1")
salario2 = input("Digite o salario do funcionario 2")
resultado1 = float(salario1) + float(salario2)
resultado2 = float(salario1) - float(salario2)
resultado3 = float(salario1) * float(salario2)
resultado4 = float(salario1) / float(salario2)
resultado5 = float(salario1) % float(salario2)
resultado6 = float(salario1) ** float(salario2)
resultado7 = float(salario1) // float(salario2)

print(f"A soma dos salarios e {resultado1}")
print(f"A subtracao dos salarios e {resultado2}")
print(f"A multiplicacao dos salarios e {resultado3}")
print(f"A divisao dos salarios e {resultado4}")
print(f"O resto da divisao dos salarios e {resultado5}")
print(f"A potencia dos salarios e {resultado6}")
print(f"A divisao inteira dos salarios e {resultado7}")

soma_test1 = 2 + 3 * 4 # = 14
soma_test2 = (2 + 3) * 4 # = 20
print(f"O resultado da expressao 2 + 3 * 4 e {soma_test1}")
print(f"O resultado da expressao (2 + 3) * 4 e {soma_test2}")
# a primeira expressao segue a ordem de precedencia das operacoes, multiplicacao antes da soma
# a segunda expressao, os parenteses alteram a ordem de precedencia, fazendo a soma ser realizada antes da multiplicacao

