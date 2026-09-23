print("Olá, nós da TudoWeb, iremos realizar uma pesquisa de satisfação")
excelente = 0
bom = 0
ruim = 0
for i in range(50):
 nome = input("Digite o seu nome: ")
 idade = int(input("Digite sua idade: "))
 Qualidade = input("Sendo 1=excelente, 2=Bom, e 3=Ruim, qual seria a sua nota para o atendimento? ")
 if Qualidade == "1":
  excelente += 1
 elif Qualidade == "2":
  bom += 1
 elif Qualidade == "3":
  ruim += 1
 print("Quantidade de avaliações: ")
 print("Excelente: ", excelente)
 print("Bom: ", bom)
 print("Ruim: ", ruim)