print('olá, seja bem-vindo ao DETRAN!')
print('Vamos verificar se você é maior de idade para poder dirigir.')
idade = input('Digite sua idade: ')
idade = int(idade)
if idade >= 18:
    print('Você é maior de idade, então pode dirigir!')
else:
    print('Você não é maior de idade, vai precisar esperar um pouco mais para poder dirigir.')
