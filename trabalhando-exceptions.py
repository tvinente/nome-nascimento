def calcular_idade(ano_nascimento):   
    try:
      ano_nascimento = int(ano_nascimento)
    except ValueError:
      raise Exception ("Valor inserido incorretamente, por favor insira um número inteiro. EX. 1957")

    if ano_nascimento < 1922 or ano_nascimento > 2021:
      raise Exception(("Digite o ano de nascimento entre 1922 e 2021: "))
    return ano_nascimento

nome_usuario = input("Por favor, informenome completo: ")
ano_nascimento = input("Por favor, informe o ano de nascimento entre 1922 e 2021: ")

while True:
    try:
      ano_nascimento = calcular_idade(ano_nascimento)
      break
    except Exception as e:
      print(e)
      ano_nascimento = input("Por favor, informe o ano de nascimento entre 1922 e 2021: ")

idade = 2022 - ano_nascimento
print(f"{nome_usuario} tem/terá {idade} em 2022")