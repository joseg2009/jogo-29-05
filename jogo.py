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
        "habilidades": {},
    }
}



while True: 
    print("Comandos: [a] ATACAR | [d] DEFENDER | [s] SAIR \n")
    comando = input("⬆️ Digite um dos comandos acima ⬆️").strip() .lower()
    if comando in ["a", "atacar", "ATACAR", "ataca"]:
        acao = "a"
    elif comando in ["d", "defender", "defende","defesa" ]:
        acao = "d"
    elif comando in ["s", "sair","sai","saia"]:
        acao = "s"
    else:
        comando = "invalido"

    match acao:

        case "a":
            
            print(f"Opção: pistola para um disparo rapido | cassetete para ataques rapidos consecutivos")
            escolha = input("Escolha sua habilidade: ").strip().lower()
            
        




print(f"personagem: {personagem}")