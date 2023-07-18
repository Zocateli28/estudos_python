## Calcula media dos alunos ##
nota_1 = float(input("Digite a 1° nota: "))
nota_2 = float(input("Digite a 2° nota: "))
nota_3 = float(input("Digite a 3° nota: "))
nota_4 = float(input("Digite a 4° nota: "))


def media(nota_1,nota_2,nota_3,nota_4):
    calculo = (nota_1+nota_2+nota_3+nota_4)/4
    return calculo

resultado = media(nota_1,nota_2,nota_3,nota_4)

if resultado >= 7:
    situacao = "aprovado"
elif resultado > 5 and resultado <7:
    situacao = "de recuperação"
else:
    situacao = "reprovado"
print(f" A media do aluno é: ", resultado, "e ele está", situacao)



    

