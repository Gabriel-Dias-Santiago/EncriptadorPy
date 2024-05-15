from cryptography.fernet import Fernet

with open('chave.key', 'rb') as filekey:
    chave = filekey.read()

fernet = Fernet(chave)   

with open('arquivo.txt', 'rb') as arquivo:
    criptografado = arquivo.read()

decriptografado = fernet.decrypt(criptografado)

with open('arquivo.txt','wb') as arquivo_criptografado:
    arquivo_criptografado.write(decriptografado)