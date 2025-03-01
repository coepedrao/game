import random

# Dicionário de temas e palavras
temas = {
    "Animais": ["elefante", "girafa", "cachorro", "gato", "tigre"],
    "Frutas": ["banana", "morango", "abacaxi", "uva", "melancia"],
    "Países": ["brasil", "canada", "japao", "alemanha", "portugal"],
    "Objetos": ["computador", "telefone", "cadeira", "mesa", "luminaria"]
}

# Escolher um tema e palavra aleatoriamente
tema = random.choice(list(temas.keys()))
palavra = random.choice(temas[tema])

# Configuração do jogo
tentativas = len(palavra) + 3  # Número de tentativas
palavra_oculta = ["_"] * len(palavra)  # Palavra oculta

print(f"Tema: {tema}")
print(f"A palavra tem {len(palavra)} letras.")
print(f"Você tem {tentativas} tentativas para adivinhar.")

while tentativas > 0 and "_" in palavra_oculta:
    print("\nPalavra: " + " ".join(palavra_oculta))
    tentativa = input("Digite uma letra ou tente adivinhar a palavra: ").lower()

    if len(tentativa) == 1:  # Se for uma única letra
        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    palavra_oculta[i] = tentativa
            print("Letra correta!")
        else:
            print("Letra errada.")
            tentativas -= 1

    elif len(tentativa) == len(palavra):  # Se for um palpite completo
        if tentativa == palavra:
            palavra_oculta = list(palavra)
            break
        else:
            print("Palavra errada!")
            tentativas -= 2  # Penalidade maior por errar a palavra inteira

    else:
        print("Entrada inválida. Tente novamente.")

    print(f"Tentativas restantes: {tentativas}")

# Resultado final
if "_" not in palavra_oculta:
    print(f"\nParabéns! Você acertou a palavra: {palavra}")
else:
    print(f"\nFim de jogo! A palavra era: {palavra}")
