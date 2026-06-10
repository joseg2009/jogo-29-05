import random

def exibir_barra_hp(nome, hp, hp_max):
    porcentagem = int((hp / hp_max) * 10)  # Calcula a porcentagem de HP
    barra = "█" * porcentagem + "░" * (10 - porcentagem)  # Monta a barra
    print(f"{nome}: [{barra}] {hp}/{hp_max}")  # Exibe barra e valores

personagem = {
    "nome": "JT",
    "hp_max": 100,
    "hp_atual": 100,
    
    "habilidades": {
        "cassetete": {
            "dano": 10,
            "tipo": "contudente",
        },  # <-- Adicionada a vírgula aqui
        "pistola": {
            "dano": 25,
            "mun_max": 12,
            "mun_atual": 12,
            "tipo": "perfurante",
        },
    },
}

bestiario = {
    "bot1": {
        "nome": "vítima 1",
        "hp_max": 75,
        "hp_atual": 75,
        "habilidades": {
            1: {"ataque":"apunhalar", "dano" : 12},
            2: {"ataque":"Ecos da Escuridão", "dano" : 17},
            3: {"ataque":"Cansaço", "dano" : 0}
        },
    }
}


nome = personagem["nome"]


while True: 
    print("Comandos: [a] ATACAR | [d] DEFENDER | [f] SAIR \n")
    comando = input("⬆️ Digite um dos comandos acima ⬆️").strip() .lower()
    if comando in ["a", "atacar", "ATACAR", "ataca"]:
        acao = "a"
    elif comando in ["d", "defender", "defende","defesa" ]:
        acao = "d"
    elif comando in ["f", "fuga","fugir"]:
        acao = "f"
    else:
        comando = "invalido"

    if personagem["hp_atual"] <= 0:
        break
    if bestiario["bot1"]["hp_atual"] <= 0:
        break
    match acao:

        case "a":
            
            print(f"Opção: pistola para um disparo rapido | cassetete para ataques rapidos consecutivos")
            escolha = input("Escolha sua habilidade: ").strip().lower()
            
            match escolha:

                case "pistola" : 
                    pistola = personagem["habilidades"]["pistola"]
                    print(pistola)
                
                case "cassetete" :
                    cassetete = personagem["habilidades"]["cassetete"]
                    print(cassetete)
        case "d": 
            r = random.randint(1,3)
            personagem["hp_atual"] -= bestiario["bot1"]["habilidades"][r]["dano"] * 0.5

            print(bestiario["bot1"]["habilidades"][r]["ataque"], bestiario["bot1"]["habilidades"][r]["dano"])
            exibir_barra_hp(nome,personagem["hp_atual"],personagem["hp_max"])

        case "f":
            r = random.randint(1,3)
            personagem["hp_atual"] -= bestiario["bot1"]["habilidades"][r]["dano"] 

            print(bestiario["bot1"]["habilidades"][r]["ataque"], bestiario["bot1"]["habilidades"][r]["dano"])
            exibir_barra_hp(nome,personagem["hp_atual"],personagem["hp_max"])
            print("voce faliu ao fugir")



# print(f"personagem: {personagem}")