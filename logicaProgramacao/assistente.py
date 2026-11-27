print(' Olá, eu sou a sua assistente, Pythrina. O que você quer fazer hoje? ')

comando = input('Digite o comando desejado: ')

match comando:
    case 'oi' | 'olá':
        print('Olá! Como você está?')
    case 'tchau' | 'sair' | 'bye':
        print('Tchau! Até a próxima!')
    case 'piada':
        print('Por que o livro de matemática se sentiu triste?')
        print('Porque tinha muitos problemas!')
    case 'clima' | 'tempo' | 'previsão do tempo':
        print('Hoje o clima está ensolarado e agradável!')
    case _:
        print('Desculpe, não entendi o que você quis dizer.')
