from cryptography.fernet import Fernet

with open('chave.key', 'rb') as filekey:
    chave = filekey.read()

fernet = Fernet(chave)   

with open('arquivo.txt', 'rb') as arquivo:
    conteudo_arquivo = arquivo.read()

criptografado = fernet.encrypt(conteudo_arquivo)

with open('arquivo.txt','wb') as arquivo_criptografado:
    arquivo_criptografado.write(criptografado)