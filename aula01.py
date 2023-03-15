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
"""
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
"""
""" 
#format com indice
a = 'A'
b = 'B'
c = 14.2
formato = 'a={0} a={0} b={1} c={2:.2f}' .format(a, b, c)

print(formato)

"""
"""
#parametro nomeado
a = 'A'
b = 'B'
c = 14.2
string = 'a={0} a={0} b={1} c={nome3:.2f}'
#tudo que vier depois de um parametro nomeado precisa tambem ser um parametro nomeado
formato =  string.format(
    a, b, nome3=c)

print(formato)
"""
"""
nome = input('qual seu nome:')
n1 = float(input('seu peso: '))
n2 = float(input('altura: '))
imc = n1 / (n2 * n2)
agua = n1 * 0.035
print(f'olá {nome} tudo bem? o seu IMC é {imc:.2f} e voce precisa beber {agua:.2f}L por dia.')
"""
"""
#codigo copiado para estudar
import healthtools

def calcular_imc(nome, peso, altura):
    
    Calcula o IMC e a quantidade diária recomendada de água para beber com base no peso e altura do usuário.
    
    if peso <= 0 or altura <= 0:
        raise ValueError("O peso e a altura devem ser maiores que zero.")
    
    imc = healthtools.BmiCalculator().calculate(peso, altura)
    agua_recomendada = peso * 0.035
    
    mensagem = f"Olá {nome}, seu IMC é {imc:.2f} e você precisa beber {agua_recomendada:.2f} L de água por dia."
    return mensagem

nome = input("Qual é o seu nome? ")
peso = float(input("Qual é o seu peso em kg? "))
altura = float(input("Qual é a sua altura em metros? "))

try:
    mensagem = calcular_imc(nome, peso, altura)
    print(mensagem)
except ValueError as error:
    print(f"Erro: {error}")
"""
"""
def calcular_imc(nome, peso, altura):
    
    #Calcula o IMC e a quantidade diária recomendada de água para beber com base no peso e altura do usuário.
  
    if peso <= 0 or altura <= 0:
        raise ValueError("O peso e a altura devem ser maiores que zero.")
    
    imc = peso / (altura * altura)
    agua_recomendada = peso * 0.035
    
    mensagem = f"Olá {nome}, seu IMC é {imc:.2f} e você precisa beber {agua_recomendada:.2f} L de água por dia."
    return mensagem

nome = input("Qual é o seu nome? ")
peso = float(input("Qual é o seu peso em kg? "))
altura = float(input("Qual é a sua altura em metros? "))

try:
    mensagem = calcular_imc(nome, peso, altura)
    print(mensagem)
except ValueError as error:
    print(f"Erro: {error}")
  """
#cifra de cesar
def encrypt(text, shift):
    """
    Função que criptografa uma mensagem usando a cifra de César.

    Argumentos:
    text -- a mensagem a ser criptografada
    shift -- o número de posições a serem puladas no alfabeto

    Retorna:
    A mensagem criptografada
    """
    result = ""
    # percorre cada caractere da mensagem
    for char in text:
        # verifica se o caractere é uma letra do alfabeto
        if char.isalpha():
            # converte o caractere para minúscula e calcula o novo índice
            new_index = (ord(char.lower()) - 97 + shift) % 26
            # converte o índice de volta para uma letra e adiciona ao resultado
            result += chr(new_index + 97)
        else:
            # se o caractere não for uma letra, adiciona ao resultado sem criptografar
            result += char
    return result

# pede ao usuário para digitar uma mensagem
text = input("Digite uma frase para criptografar: ")

# criptografa a mensagem com uma chave de deslocamento de 1 posição
encrypted_text = encrypt(text, 1)

# imprime a mensagem criptografada
print("Mensagem criptografada: " + encrypted_text)

#test