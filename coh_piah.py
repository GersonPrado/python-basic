import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    traco_linguistico = []
    index = 0
    if as_a == as_b:
        return 0
    while index < len(as_a):
        traco_linguistico.append(abs(as_a[index] - as_b[index]))
        index = index + 1
    
    soma_diferencas = sum(traco_linguistico) / 6
    assinatura_texto = sum(as_a) / 6

    return assinatura_texto - soma_diferencas

def calcula_assinatura(texto):
    lista_sentencas = separa_sentencas(texto)
    lista_frases = frases(lista_sentencas)
    lista_palavras = palavras(lista_frases)
    quantidade_total_palavras = len(lista_palavras)
    wal_media_palavras = tamanho_medio_palavras(lista_palavras)
    ttr_type_token = n_palavras_diferentes(lista_palavras) / quantidade_total_palavras
    hlr_hapax_legomana = n_palavras_unicas(lista_palavras) / quantidade_total_palavras
    sal_tamanho_medio_sentenca = calcula_media(lista_sentencas)
    sac_complexidade_sentenca = len(lista_frases) / len(lista_sentencas)
    pal_tamanho_medio_frase = calcula_media(lista_frases)
    
    return [wal_media_palavras, ttr_type_token, hlr_hapax_legomana, sal_tamanho_medio_sentenca, sac_complexidade_sentenca, pal_tamanho_medio_frase]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    textos_avalidados = []
    numero_texto = 1
    
    for texto in textos:
        textos_avalidados.append([compara_assinatura(calcula_assinatura(texto), ass_cp),numero_texto])
        numero_texto = numero_texto + 1
    
    textos_avalidados.sort()
    return textos_avalidados[0][1]

def calcula_media(lista):
    '''A função receba uma lista e retorna a média das frases ou sentencas contidas na lista'''
    soma_numero_caracteres = 0
    for media in lista:
        if media != " ":
            soma_numero_caracteres = soma_numero_caracteres + len(media)
    return soma_numero_caracteres / len(lista)

def tamanho_medio_palavras(lista_palavras):
    '''A função receba uma lista de palavras e o tamanho médio das palavras'''
    soma_tamanho_das_palavras = 0
    numero_total_palavras = 0

    for palavra in lista_palavras:                
        soma_tamanho_das_palavras = soma_tamanho_das_palavras + len(palavra)
        numero_total_palavras = numero_total_palavras + 1

    return soma_tamanho_das_palavras / numero_total_palavras

def frases(sentencas):
    '''A função receba uma lista de sentenças e retorna uma lista de frases'''
    frases = []
    lista_frase = []
    for sentenca in sentencas:
        frases.append(separa_frases(sentenca))
    
    for frase in frases:
        for resultado in frase:
            lista_frase.append(resultado)
    
    return lista_frase

def palavras(lista_frases):
    '''A função receba uma lista de frases e retorna uma lista de palavras contidas na frase'''
    lista_palavras_na_frase = []
    lista_palavras = []
    
    for frases in lista_frases:
        lista_palavras_na_frase.append(separa_palavras(frases))
    
    for palavras in lista_palavras_na_frase:
        for resultado in palavras:
            lista_palavras.append(resultado)

    return lista_palavras

assinatura = le_assinatura()
textos = le_textos()
avaliados = avalia_textos(textos,assinatura)
print("O autor do texto", avaliados, "está infectado com COH-PIAH")