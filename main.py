# # criando um arquivo .txt
arquivo = open("palavras.txt", "a") 

arquivo.write("ameixa\n")

# arquivo.close() # sempre fechar o arquivo após a execução
# arquivo = open("palavras.txt", "a") #Para abrir e adicionar uma nova informação usamos a função a, de appended


# Modificadores de acesso:
# # r - leitura 
# arquivo = open("palavras.txt", "r")
# arquivo.read()

# # a - inclusão 
# arquivo = open("palavras.txt", "a")

# # w - escrita
# arquivo = open("palavras.txt", "w")

# # b - binarios

# # rb - abrir imagens 
# imagem = open("foto.jpg", "rb")

# # wb - criar copias de imagens
# logo = open('python-logo.png', 'rb')
# data = logo.read()
# logo.close()

# logo2 = open('python-logo2.png', 'wb')
# logo2.write(data)
# logo2.close()
