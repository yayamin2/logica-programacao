nota = input('Digite a nota do aluno: ')
nota = int(nota)

if nota >= 7:
    print('Parabéns! Você foi aprovado!')
elif nota < 5:
    print('Você está reprovado!')
else:
    print('Você está de recuperação!')
