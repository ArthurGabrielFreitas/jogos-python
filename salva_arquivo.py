arquivo1 = open("resultado.txt", "r")
arquivo2 = open("cidades.txt", "w", -1, "cp1252")

for linha in arquivo1:
    if len(linha) > 125:
        continue
    if "<td><b><a" in linha:
        numero_linha = linha.find("title")
        numero_linha = linha.find(">", numero_linha)
        linha_aux = ""
        for letra in range(numero_linha+1, len(linha) - 9):
            linha_aux += linha[letra]
        arquivo2.write("{}\n".format(linha_aux))
    else:
        numero_linha = linha.find("title")
        numero_linha = linha.find(">", numero_linha)
        linha_aux = ""
        for letra in range(numero_linha + 1, len(linha) - 5):
            linha_aux += linha[letra]
        linha = str(linha)
        arquivo2.write("{}\n".format(linha_aux))
arquivo1.close()
arquivo2.close()
