def ignora_acento(palavra):
    nova_palavra = ""
    for letra in palavra:
        letra = {
            "Á": "A",
            "À": "A",
            "Ã": "A",
            "Â": "A",
            "É": "E",
            "Ê": "E",
            "Í": "I",
            "Ó": "O",
            "Õ": "O",
            "Ô": "O",
            "Ú": "U"
        }.get(letra, letra)
        nova_palavra += letra
    return nova_palavra
