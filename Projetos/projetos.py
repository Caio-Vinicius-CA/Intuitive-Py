## Script que pede ao usuário para digitar um número inteiro, informando se este número é par ou ímpar.
"""
entrada = input("Digite um número inteiro: ")

if not entrada.lstrip("-").isdigit():
    print("ERRO! Digite um número inteiro.")
else:
    n1 = int(entrada)
    par_impar = n1 % 2 == 0
    if par_impar:
        print(f"O número: {n1} é par.")
    else:
        print(f"O número: {n1} é impar.")
"""

## Script que pergunta a hora ao usuário e, baseando-se no horário descrito, exibe a saudação apropriada.
"""
entrada = input("Digite a hora atual: (Não inclua os minutos e segundos.)")

try: #if hora.isdigit():
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print("Bom dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 24:
        print("Boa noite!")
    else:
        print("ERRO!")
except: #else:
    print("ERRO! Digite um número inteiro.")
"""

## Script que pede o primeiro nome do usuário e classifica se o nome é curto ou longo.

"""
nome = input("Digite seu primeiro nome: ")
if nome.isalpha():
    if len(nome) <= 4:
        print("Seu nome é curto.")
    elif len(nome) >= 4 and len(nome) <= 6:
        print("Seu nome é normal.")
    elif len(nome) > 6:
        print("Seu nome é muito grande.")
    else:
        print("ERRO!")
else:
    print("ERRO! Digite seu nome corretamente.")
"""

## Calculadora com While
"""
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    try:
        print("BEM VINDO A NOSSA CALCULADORA!!!")
        entrada_n1 = input("Digite o primeiro número: ")
        entrada_n2 = input("Digite o segundo número: ")
        print("Por favor escolha uma operação: \n+ para soma\n- para subtração\n* para multiplicação\n/ para divisão\n** para potenciação")
        sinal = input("Digite: ")
        n1 = float(entrada_n1)
        n2 = float(entrada_n2)
        if sinal == "+":
            print(f"{n1 + n2:.1f}")
        elif sinal == "-":
            print(f"{n1 - n2:.1f}")
        elif sinal == "*":
            print(f"{n1 * n2:.1f}")
        elif sinal == "/":
            if n2 == 0:
                print("ERRO! Não é possivel divisão por 0.")
            else:
                print(f"{n1 / n2:.1f}")
        elif sinal == "**":
            print(f"{n1 ** n2:.1f}")
        else:
            print("Operação inválida. Por favor escolha uma operação válida.")
            continue
        repeat = input("Deseja fazer outra operação? [S]im / [N]ão\n").lower()
        if repeat == "s" or repeat == "sim":
            limpar_tela()
            continue
        else:
            limpar_tela()
            break
        
    except ValueError:
        print("ERRO! Entrada inválida.")
"""

## Contador de letras
"""
import string
frase = input("Digite uma frase: ")

contagem_de_letra = 0
letra_max = ""
i = 0
while i < len(frase):
    letra_atual = frase[i].lower()
    contagem_geral = frase.count(letra_atual)
    
    if letra_atual == " ":
        i += 1
        continue
    if letra_atual in string.punctuation:
        i += 1
        continue

    if contagem_de_letra <= contagem_geral:
        contagem_de_letra= contagem_geral
        letra_max = letra_atual

    print(letra_atual, contagem_geral)
    i += 1
print("A letra que mais apareceu foi: "
f"A letra '{letra_max}', "
f"que apareceu {contagem_de_letra} vezes")
"""

## Jogo de adivinhação de plavras
"""
import os

palavra_secreta = "chamuscar".upper()
tamanho = len(palavra_secreta)
palavra_cript = tamanho*"*"
palavra_cript_list = list(palavra_cript)
tentativas = 0
letra_atual = ""

print('Bem vindo ao meu MiniGame "Adivinhe a palavra"\nTe desejo sorte! ;)')
while True:
    if "*" in palavra_cript_list:
        letra_atual = input("Digite uma letra: ").upper()
        tentativas += 1

        if len(letra_atual) > 1 or letra_atual.isalpha() == False:
            print("Digite apenas uma letra!!!".upper())
            continue

        for letra in range(tamanho):
            if palavra_secreta[letra] == letra_atual:
                palavra_cript_list[letra] = letra_atual

    else:
        os.system("cls")
        print("Parabén você conseguiu concluir o jogo!")
        print("O que você ganhou? Férias de mim! ADIOS")
        print(f"Número de tentativas: ", tentativas)
        break
    
    print("".join(palavra_cript_list))
    continue
"""

## Imprimir os indices junto aos nomes da lista
"""
lista = ["Maria", "João", "Cláudia"]
lista.append("Joana")

for a, b in enumerate(lista):
    print(a, b)
"""

## Lista de compras
"""
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

compras = []
print("Bem vindo a sua lista de compras.")
while True:
    quantidade_de_itens = len(compras)
    opcao = input("Selecione uma opção-\n[I]nserir [A]pagar [L]istar: ").upper()

    if opcao == "I" or opcao == "INSERIR":
        adicionar_item = input("Qual item você quer adicionar à lista?\n").upper()
        if adicionar_item.isalpha() == True:
            if adicionar_item not in compras:
                compras.append(adicionar_item)
                limpar_tela()
                print(f"Item adicionado: {adicionar_item}")
            else:
                limpar_tela()
                print("Este item já está presente na lista.")
        else:
            limpar_tela()
            print("Por favor, digite itens válidos!")
    elif opcao == "A" or opcao == "APAGAR":
        apagar_item = input("Escolha um item para apagar: ").upper()
        if quantidade_de_itens == 0 or apagar_item not in compras:
            limpar_tela()
            print("Não foi possível apagar este item.")
        else:
            limpar_tela()
            print(f"{apagar_item.capitalize()} foi retirado da lista.")
            compras.remove(apagar_item)

    elif opcao == "L" or opcao == "LISTAR":
        if quantidade_de_itens == 0:
            limpar_tela()
            print("Sua lista de compras está vazia.")
        else:
            limpar_tela()
            for indice, item in enumerate(compras):
                print(f"{indice} {item}")

    else:
        limpar_tela()
        print("Por favor, escolha uma das opções indicadas.")
        continue
"""

## Validador de CPF
"""
import string
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    print("Verificador de CPF")
    cpf = input("Digite seu cpf: ")
    print("")

    if any(char in string.punctuation for char in cpf):
        cpf_nmb = cpf.replace(".", "").replace("-", "")
    else:
        cpf_nmb = cpf

    if len(cpf_nmb) == 11:
        cpf_nove = cpf_nmb[:9]
        cpf_dez = cpf_nmb[:10]
        cpf_verificador = cpf_nmb[9:]

        contador_d1 = 10
        contador_d2 = 11
        soma_total_d1 = 0
        soma_total_d2 = 0

        for i in cpf_nove:
            soma_total_d1 += int(i) * contador_d1
            contador_d1 -=1

        resultado_d1 = (soma_total_d1 * 10) % 11

        if resultado_d1 >= 10:
            primeiro_digito = 0
        else:
            primeiro_digito = resultado_d1

        for i in cpf_dez:
            soma_total_d2 += int(i) * contador_d2
            contador_d2 -=1

        resultado_d2 = (soma_total_d2 * 10) % 11

        if resultado_d2 >= 10:
            segundo_digito = 0
        else:
            segundo_digito = resultado_d2

        print(f"Primeiro dígito verificador: {primeiro_digito}")
        print(f"Segundo dígito verificador: {segundo_digito}\n")

        resultado_total = str(resultado_d1) + str(resultado_d2)

        if resultado_total == cpf_verificador:
            print("O CPF informado é valido.")
            
        else:
            print("O CPF informado é invalido.")
        
        repeat = input("\nDeseja repetir a operação? [S]im / [N]ão\n").lower()
        if repeat == "s" or repeat == "sim":
            limpar_tela()
            continue
        else:
            limpar_tela()
            break
    else:
        print("CPF inválido informado, tente novamente.")
        continue
"""

## Pequeno Quiz
"""
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta_certa': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta_certa': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta_certa': '5',
    },
]

# Variáveis
contador_alt = 0 # Contador para as alternativas
pontos = 0 # Contagem de pontos
n_pergunta = 0 # Controla a ordem das perguntas
qttd_perguntas = len(perguntas) # Quantidade total de perguntas no quiz
lista_atual_alternativas = [] # Armazena as opções da pergunta atual
alternativas = ["a","b","c","d"]  # Alternativas que represemtam as opções

print("Bem vindo ao meu pequeno quiz!")

# for pra iterar pelas perguntas (enumerate para usar o 'i' no código)
for i, (chave, valor) in enumerate(perguntas[n_pergunta].items()):
    lista_atual_alternativas = perguntas[n_pergunta]['Opções'] # Armazena as opções da pergunta atual

    if i < qttd_perguntas: # Condição para não passar do número de perguntas
        print(f"Pergunta: {perguntas[n_pergunta]['Pergunta']}")

        for x in perguntas[n_pergunta]['Opções']: # for para exibir as alternativas e opções
            print(f"{alternativas[contador_alt]}) {x}")
            contador_alt += 1
    contador_alt= 0

    # Encontra o índice da resposta correta na lista de opções
    local = lista_atual_alternativas.index(perguntas[n_pergunta]['Resposta_certa']) 
    resposta = input("Escolha uma alternativa: ")

    # Compara se a resposta do usuário é o valor da resposta certa ou da alternativa certa, se sim, pontua.
    if resposta == lista_atual_alternativas[local] or resposta == alternativas[local]: 
        print("Parabens! Você acertou 👍\n")
        pontos += 1
    else:
        print("Você errou ❌\n")

    # Incremeta para passar para a próxima pergunta
    i+=1
    n_pergunta+=1

print(f"Você acertou {pontos}\nde {qttd_perguntas} perguntas\n")
"""