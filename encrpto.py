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
