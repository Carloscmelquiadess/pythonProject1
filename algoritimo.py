nota1 = float(input('DIGITE A SUA MEDIA : '))
nota2 = float(input('DIGITE A SUA MEDIA : '))
nota3 = float(input('DIGITE A SUA MEDIA : '))


media = (nota1 + nota2 + nota3) / 3
if media < 7:
    print('VOCE REPROVOU SUA MEDIA FOI {:.2}'.format(media))
if media >= 7:
    print('VOCÊ FOI APROVADO SUA MEDIA FOI {:.2}'.format(media))
if media >= 9:
    print('VOCÊ FOI APROVADO SUA MEDIA FOI EXELENTE {:.2}'.format(media))

while input != '':
    nota1 = float(input('DIGITE A SUA MEDIA : '))
    nota2 = float(input('DIGITE A SUA MEDIA : '))
    nota3 = float(input('DIGITE A SUA MEDIA : '))

    media = (nota1 + nota2 + nota3) / 3
    if media < 4:
        print('VOCE REPROVOU SUA MEDIA FOI {:.2}'.format(media))
    if media <= 4:
        print('VOCE ESTA APTO A PROVA DE REPOSIÇÃO {:.2}'.format(media))

    if media >= 7:
        print('VOCÊ FOI APROVADO SUA MEDIA FOI {:.2}'.format(media))
    if media >= 9:
        print('VOCÊ FOI APROVADO SUA MEDIA FOI EXELENTE {:.2}'.format(media))