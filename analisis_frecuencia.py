from collections import Counter

# Texto cifrado
texto_cifrado = "NLDIXALALNLSLZMNBKLDLAPIMAHIMFXKUHILAJLFXULDLSKAJLNEMAMDIKNLLIKULRPFKSLKNFLIAKKVHKUSXLLUHKKNJMFMPUFLUHMMAJPIMCIPZXKUHKJLSLMNLSKGLDLPUILAHIMKABPFMAMLUHKASKIKHXILIAKSKOMILUSMNLMIXNNLBMJMLBMJMAKUHXLKNQIXMAPDXIBMIAPABXKIULABKIMUMAKSKHKUXLAPABLAMAKILUNKUHMABKALSMAJMFMAXLNZMXUOXAXDNKHXILILSKKNRLJXLKNRMIXEMUHKXUQXUXHMLNMNKGMAPULNPESKDXNBLIBLSKLDLKUKNLZPLQNMHLUSMAXUFMOKIAKLBKALISKNMNKLGKXUHKUHMXZUMILINLBKIMLNZMSKUHIMSKKNNMMDNXZLDLLLJKIJLIAKKNNLHXSMSKAPJMILEMUAKOMNOXMXIIKZPNLIFXKUHILAKNLZPLNKJPDIXLNLAIMSXNNLANPKZMNLJXUHPILNLIKABXILJXMUAKKUHIKJMIHMJPLUSMKNQIXMNKNNKZMLNBKJRMBKIMAXZPXMLOLUELUSMXUJLBLESKIKAXAHXIAKJLSLOKEFLAJKIJLJLSLOKEFLABIMQPUSMJPLUSMKAHPOMLPUBLAMSKNLNPEKVHKUSXMNLFLUMCKUKAKXUAHLUHKNLOXMPUMAMGMAAXUDIXNNMKFKIZXKIMUSKNLAAMFDILADLGMKNLZPLPUIMAHIMBLNXSMCLGLSMNMMDAKIOLDLSKASKNLABIMQPUSXSLSKAAXUHXMPUHXIMUKUNMAHMDXNNMACLUHKASKTPKBPSXKILZIXHLIKNFLINMSKOMIMAXUSKGLIILAHIMAMNMNLNPETPKSMQNMHLUSMKABKILUSMLMHIMOXLGKIMAMNXHLIXM"

# Texto descifrado
texto_descifrado = ""

# Frecuencias en español
frec_esp = ["E", "A", "O", "S", "R", "N", "I", "D", "L", "C", "T", "U", "M", "P", "B", "G", "V", "Y", "Q", "H", "F", "Z", "J", "X", "K", "W"]

# Contar frecuencia de cada letra
contador = Counter(texto_cifrado)

contador_ordenado = sorted(contador.items(), key=lambda x: x[1], reverse=True)

diccionario_frec= {}
for letra, frecuencia in contador_ordenado:
    print(f"{letra}: {frecuencia}, {(frecuencia*100/len(texto_cifrado)):.3f}%")
    diccionario_frec[letra] = None
 
for letra_esp, letra_cif in zip(diccionario_frec.keys(), frec_esp):
    diccionario_frec[letra_esp] = letra_cif
print(diccionario_frec)
    
for letra in texto_cifrado:
    if letra in diccionario_frec:
        texto_descifrado += diccionario_frec[letra]
    else:
        texto_descifrado += letra.lower()  # En caso de que la letra no esté en el diccionario, la dejamos igual pero en minúscula para que se note
print(texto_descifrado)

    

    
    
    
