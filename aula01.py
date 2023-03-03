"""
{
    "liveServer.settings.donotShowInfoMsg": true,
    "explorer.compactFolders": false,
    "code-runner.clearPreviousOutput": true,
    "code-runner.runInTerminal": true,
    "code-runner.executorMap": {
        "python": "cls ; python -u",
    },
    "code-runner.ignoreSelection": true,
    "workbench.colorTheme": "OM Theme (Default Dracula Italic)",
    "workbench.iconTheme": "material-icon-theme",
    "python.defaultInterpreterPath": "python",
}
lembrar de alterar o executorMap de acordo com o sistema operacional
"""
"""
#separador
print (12, "teste", sep='-')
print (12, "teste",12, sep='-')

#escape
print("teste de \"escape\"")

#inverter aspas
print ('tesde de "aspas"')

#type
print( type('teste'))
print( type(True))
#converter tipo
print(int ('1')+2)
"""
"""
#f-strings
peso = 143
litro = 0.035
calculo = f'{peso*litro:.2f}' 

print(calculo)
"""
"""
#format
a = 'A'
b = 'B'
c = 14.2
formato = 'a={} b={} c={:.2f}' .format(a, b, c)

print(formato)
"""
#teste
Vetor1 = []
Vetor2 = []
Soma = []
soma = 0

for i in range(3):
    Vetor1.append(int(input(f'Informe um valor para o Vetor1[{i+1}]: ')))
    Vetor2.append(int(input(f'Informe um valor para o Vetor2[{i+1}]: ')))
    Soma.append(int(Vetor1[i] + Vetor2[i]))

for i in range(3):
    soma = soma+Soma[i]
    print(soma)
