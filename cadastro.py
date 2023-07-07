nome = str(input('DIGITE SEU NOME COMPLETO : ')).upper().strip()

ano = int(input('DIGITE O ANO QUE VOCÊ NASCEU : '))
idade = 2023 - ano

print('SEU NOME É : {} E O ANO QUE VOCÊ NASCEU FOI : {} E SUA IDADE È : {} ANOS '.format(nome, ano, idade))

while nome or idade != ' ':
    nome = str(input('DIGITE SEU NOME COMPLETO : ')).upper().strip()

    ano = int(input('DIGITE O ANO QUE VOCÊ NASCEU : '))
    idade = 2023 - ano

    print('SEU NOME É : {} E O ANO QUE VOCÊ NASCEU FOI : {} E SUA IDADE È : {} ANOS '.format(nome, ano, idade))
