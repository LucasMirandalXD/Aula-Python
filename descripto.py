def decrypt(text, shift):
    """
    Função que descriptografa uma mensagem criptografada usando a cifra de César.

    Argumentos:
    text -- a mensagem criptografada
    shift -- o número de posições que foram puladas no alfabeto

    Retorna:
    A mensagem original descriptografada
    """
    result = ""
    # percorre cada caractere da mensagem criptografada
    for char in text:
        # verifica se o caractere é uma letra do alfabeto
        if char.isalpha():
            # converte o caractere para minúscula e calcula o índice original
            orig_index = (ord(char.lower()) - 97 - shift) % 26
            # converte o índice de volta para uma letra e adiciona ao resultado
            result += chr(orig_index + 97)
        else:
            # se o caractere não for uma letra, adiciona ao resultado sem descriptografar
            result += char
    return result

# pede ao usuário para digitar uma mensagem criptografada
encrypted_text = input("Digite a mensagem criptografada para descriptografar: ")

# descriptografa a mensagem com uma chave de deslocamento de 1 posição
decrypted_text = decrypt(encrypted_text, 1)

# imprime a mensagem descriptografada
print("Mensagem descriptografada: " + decrypted_text)
