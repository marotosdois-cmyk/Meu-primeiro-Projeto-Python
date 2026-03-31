"""
Character Creator
Basic Python project using functions and input validation.

Author: Rafael Dias
"""
ponto_cheio = '●'
ponto_vazio = '○'
nome = input("Digite o nome do personagem: ")
raça = ["Humano", "Elfo", "Anão", "Orc", "Goblin", "Troll", "Vampiro", "Lobisomem", "Zumbi", "Fantasma"]
idade = int(input("Digite a idade do personagem: "))
altura = float(input("Digite a altura do personagem (em metros): "))
raça_escolhida = input("Escolha a raça do personagem (Humano, Elfo, Anão, Orc, Goblin, Troll, Vampiro, Lobisomem, Zumbi, Fantasma): ")
while raça_escolhida not in raça:
    print("Raça inválida. Por favor, escolha uma das seguintes opções:")
    print(", ".join(raça))
    raça_escolhida = input("Escolha a raça do personagem (Humano, Elfo, Anão, Orc, Goblin, Troll, Vampiro, Lobisomem, Zumbi, Fantasma): ")
print('Agora defina seus status:')
print('Observação: A quantidade de pontos para distribuir é 20. Cada status deve receber um valor entre 0 e 10.')
força = int(input("Força (0-10): "))
destreza = int(input("Destreza (0-10): "))
inteligência = int(input("Inteligência (0-10): "))
sabedoria = int(input("Sabedoria (0-10): "))
carisma = int(input("Carisma (0-10): "))
vitalidade = int(input("Vitalidade (0-10): "))
total_pontos = força + destreza + inteligência + sabedoria + carisma + vitalidade
while total_pontos > 20:
    print("Você excedeu o limite de pontos. Por favor, distribua os pontos novamente.")
    força = int(input("Força (0-10): "))
    destreza = int(input("Destreza (0-10): "))
    inteligência = int(input("Inteligência (0-10): "))
    sabedoria = int(input("Sabedoria (0-10): "))
    carisma = int(input("Carisma (0-10): "))
    vitalidade = int(input("Vitalidade (0-10): "))
    total_pontos = força + destreza + inteligência + sabedoria + carisma + vitalidade
if raça_escolhida == "Humano":
    destreza -= 1
    inteligência += 1
    carisma += 1
    vitalidade -= 1
    print("O personagem é um Humano. Destreza -1, Inteligência +1, Carisma +1, Vitalidade -1.")
elif raça_escolhida == "Elfo":
    força -= 1
    destreza += 2
    inteligência += 1
    sabedoria += 1
    vitalidade -= 1
    print("O personagem é um Elfo. Força -1, Destreza +2, Inteligência +1, Sabedoria +1, Vitalidade -1.")
elif raça_escolhida == "Anão":
    força += 2
    destreza -= 1
    inteligência -= 1
    sabedoria += 1
    vitalidade += 1
    print("O personagem é um Anão. Força +2, Destreza -1, Inteligência -1, Sabedoria +1, Vitalidade +1.")
elif raça_escolhida == "Orc":
    força += 3
    destreza -= 2
    inteligência -= 2
    sabedoria -= 1
    carisma -= 1
    vitalidade += 2
    print("O personagem é um Orc. Força +3, Destreza -2, Inteligência -2, Sabedoria -1, Carisma -1, Vitalidade +2.")
elif raça_escolhida == "Goblin":
    força -= 2
    destreza += 2
    inteligência += 1
    sabedoria -= 1
    carisma -= 1
    vitalidade -= 1
    print("O personagem é um Goblin. Força -2, Destreza +2, Inteligência +1, Sabedoria -1, Carisma -1, Vitalidade -1.")
elif raça_escolhida == "Troll":
    força += 4
    destreza -= 3
    inteligência -= 3
    sabedoria -= 2
    carisma -= 2
    vitalidade += 3
    print("O personagem é um Troll. Força +4, Destreza -3, Inteligência -3, Sabedoria -2, Carisma -2, Vitalidade +3.")
elif raça_escolhida == "Vampiro":
    força += 2
    destreza += 1
    inteligência += 2
    sabedoria -= 1
    carisma += 2
    vitalidade -= 2
    print("O personagem é um Vampiro. Força +2, Destreza +1, Inteligência +2, Sabedoria -1, Carisma +2, Vitalidade -2.")
elif raça_escolhida == "Lobisomem":
    força += 3
    destreza += 1
    inteligência -= 1
    sabedoria -= 1
    carisma -= 1
    vitalidade += 2
    print("O personagem é um Lobisomem. Força +3, Destreza +1, Inteligência -1, Sabedoria -1, Carisma -1, Vitalidade +2.")
elif raça_escolhida == "Zumbi": 
    força += 1
    destreza -= 2
    inteligência -= 3
    sabedoria -= 2
    carisma -= 3
    vitalidade += 4
    print("O personagem é um Zumbi. Força +1, Destreza -2, Inteligência -3, Sabedoria -2, Carisma -3, Vitalidade +4.")
elif raça_escolhida == "Fantasma":
    força -= 2
    destreza += 1
    inteligência += 2
    sabedoria += 1
    carisma -= 1
    vitalidade -= 3
    print("O personagem é um Fantasma. Força -2, Destreza +1, Inteligência +2, Sabedoria +1, Carisma -1, Vitalidade -3.")
print('A sua vida máxima é igual a sua vitalidade divida por 2, arredondada para baixo.')
print("                    \n--- Ficha do Personagem ---")
print(f"Nome: {nome}")
print(f"Raça: {raça_escolhida}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} metros")
print('                    \n--- Status ---')
print(f"Força: {força} {ponto_cheio * força}{ponto_vazio * (15 - força)}")
print(f"Destreza: {destreza} {ponto_cheio * destreza}{ponto_vazio * (15 - destreza)}")
print(f"Inteligência: {inteligência} {ponto_cheio * inteligência}{ponto_vazio * (15 - inteligência)}")
print(f"Sabedoria: {sabedoria} {ponto_cheio * sabedoria}{ponto_vazio * (15 - sabedoria)}")
print(f"Carisma: {carisma} {ponto_cheio * carisma}{ ponto_vazio * (15 - carisma)}")
print(f"Vitalidade: {vitalidade} {ponto_cheio * vitalidade}{ponto_vazio * (15 - vitalidade)}")
print(f"Vida Máxima: {vitalidade // 2}")
vida_maxima = vitalidade // 2
print('Agora escolheremos sua classe.')
armas = ["Espada", "Arco", "Machado", "Lança", "Adaga", "Cajado", "Martelo", "Foice", "Clava", "Chicote"]
armaduras = ["Armadura de Couro", "Armadura de Malha", "Armadura de Placas", "Armadura Pesada"]
classes = ["Guerreiro", "Arqueiro", "Mago", "Ladino", "Clérigo", "Bárbaro", "Paladino", "Feiticeiro", "Druida", "Assassino"]
classe_escolhida = input("Escolha a classe do personagem (Guerreiro, Arqueiro, Mago, Ladino, Clérigo, Bárbaro, Paladino, Feiticeiro, Druida, Assassino): ")
while classe_escolhida not in classes:
    print("Classe inválida. Por favor, escolha uma das seguintes opções:")
    print(", ".join(classes))
    classe_escolhida = input("Escolha a classe do personagem (Guerreiro, Arqueiro, Mago, Ladino, Clérigo, Bárbaro, Paladino, Feiticeiro, Druida, Assassino): ")
print(f"O personagem é um {classe_escolhida}")
atributo_principal = ""
print('Seu principal status é:')
if classe_escolhida == "Guerreiro":
    print("Força") 
    atributo_principal = força
elif classe_escolhida == "Arqueiro":
    print("Destreza")
    atributo_principal = destreza
elif classe_escolhida == "Mago":
    print("Inteligência")
    atributo_principal = inteligência
elif classe_escolhida == "Ladino":
    print("Destreza")
    atributo_principal = destreza
elif classe_escolhida == "Clérigo":
    print("Sabedoria")
    atributo_principal = sabedoria
elif classe_escolhida == "Bárbaro": 
    print("Força")
    atributo_principal = força
elif classe_escolhida == "Paladino":
    print("Força")
    atributo_principal = força
elif classe_escolhida == "Feiticeiro":
    print("Inteligência")
    atributo_principal = inteligência
elif classe_escolhida == "Druida":
    print("Sabedoria")
    atributo_principal = sabedoria
elif classe_escolhida == "Assassino":
    print("Destreza")
    atributo_principal = destreza
print('Agora escolha sua arma e armadura.')
arma_escolhida = input("Escolha a arma do personagem (Espada, Arco, Machado, Lança, Adaga, Cajado, Martelo, Foice, Clava, Chicote): ")
while arma_escolhida not in armas:
    print("Arma inválida. Por favor, escolha uma das seguintes opções:")
    print(", ".join(armas))
    arma_escolhida = input("Escolha a arma do personagem (Espada, Arco, Machado, Lança, Adaga, Cajado, Martelo, Foice, Clava, Chicote): ")
armadura_escolhida = input("Escolha a armadura do personagem (Armadura de Couro, Armadura de Malha, Armadura de Placas, Armadura Pesada): ")
while armadura_escolhida not in armaduras:
    print("Armadura inválida. Por favor, escolha uma das seguintes opções:")
    print(", ".join(armaduras))
    armadura_escolhida = input("Escolha a armadura do personagem (Armadura de Couro, Armadura de Malha, Armadura de Placas, Armadura Pesada): ")
print(f"Arma escolhida: {arma_escolhida}")
print(f"Armadura escolhida: {armadura_escolhida}")
print('\n Agora sua classe, arma e armadura são:')
print(f"""Classe: {classe_escolhida}
Arma: {arma_escolhida}
Armadura: {armadura_escolhida}""")

#                                             =====FUNÇÕES DE SISTEMA=====

def mostrar_status():
    return f"""--- Status do Personagem ---
Nome: {nome}
Raça: {raça_escolhida}
Idade: {idade} anos
Altura: {altura} metros
Força: {força}
Destreza: {destreza}
Inteligência: {inteligência}
Sabedoria: {sabedoria}
Carisma: {carisma}
Vitalidade: {vitalidade}
Vida Máxima: {vida_maxima} """

def mostrar_equipamento():
    return f"""--- Equipamento do Personagem ---
Classe: {classe_escolhida}
Arma: {arma_escolhida}
Armadura: {armadura_escolhida}"""

def calcular_dano():
    if arma_escolhida in ['Espada','Machado','Lança','Martelo','Clava']:
        atributo_principal += 2
    elif arma_escolhida in ['Arco','Adaga','Foice','Chicote']:
        atributo_principal += 1
    elif arma_escolhida in ['Cajado']:
        atributo_principal += 3
    return f"O dano causado pelo personagem é: {atributo_principal}"

