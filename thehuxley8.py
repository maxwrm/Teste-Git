dicionario = dict()
gabarito = input()
listaDeNotas = []
nota = 0

aluno = input()
while aluno != '9999':
    alunoNum, respostas = aluno.split()
    dicionario[alunoNum] = str(respostas)
    for i in range(len(gabarito)):
        if respostas[i] == gabarito[i]:
            nota += 1
    listaDeNotas.append(nota)
    print(f'{alunoNum} {nota:.1f}')
    aluno = input()
    nota = 0

aprovado = 0
for i in range(len(listaDeNotas)):
    if listaDeNotas[i] >= 6:
        aprovado += 1
    quantidadeDeAlunos = len(listaDeNotas)
print(f'{((aprovado/quantidadeDeAlunos)*100):.1f}%')
notaComum = max(listaDeNotas, key=listaDeNotas.count)
print(f'{notaComum:.1f}')


