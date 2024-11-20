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

## Imprimir os indices junto aos nomes da lista
"""
lista = ["Maria", "João", "Cláudia"]
lista.append("Joana")

for a, b in enumerate(lista):
    print(a, b)
"""

## Ordenador de listas
"""
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Lista com preço alterado para +10%
novos_produtos = copy.deepcopy(produtos)

print("Alteração dos valores")
print("Produto".ljust(15), "Preço".rjust(10))
print("-"*31)

for n in novos_produtos:
    print(f"{n["nome"].ljust(20)} R$ {n["preco"]}")
    n['preco'] = round(n['preco'] * 1.1, 2)
    print(f"{n["nome"].ljust(20)} R$ {n["preco"]:.2f}\n")

print(f"\nNova lista com valores editados")
for n in novos_produtos:
    print(n)

# Lista ordenada por nome decrescente
produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda x: x["nome"], reverse=True)
print(f"\nNova lista ordenada por nome")
for produto in produtos_ordenados_por_nome:
    print(produto)

# Lista ordenada por preço crescente
produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda x: x["preco"])
print(f"\nNova lista ordenada por preço")
for produto in produtos_ordenados_por_preco:
    print(produto)
"""