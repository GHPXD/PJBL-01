#Biblioteca do 2º projeto de CAE
import pandas as pd
#Função para ler o arquivo exel com o pandas 
def learquivo(caminho):
    dados = pd.read_csv (caminho,sep=';')
    datas_df = dados ['Data']
    hora_df = dados ['Hora']
    temp_df = dados ['Temperatura']
    return datas_df,hora_df,temp_df
#Função para calcular a temperatura média com horários específicos 
def TempMediaE(datas,hora,temp,horario,mesA,mesB):
    soma = 0
    i = 0
    result = 0
    for h in range (len(hora)):
        for m in range (len(datas)):
            if int(hora[h]) == horario:
                if mesA <= datas[m][3:5] <= mesB:                    
                    soma = soma + temp[h]
                    i = i + 1
    result = soma / i  
    return result
#Função para calcular a temperatura média a partir de todos horários 
def TempMediaT(datas,hora,temp,mesA,mesB):
    medidia = 0
    i = 0
    result = 0
    for m in range (len(datas)):
        if mesA <= datas[m][3:5] <= mesB:
            for h in range (len(hora)):
                soma = 0
                if hora[h] == 0:
                    soma = soma + temp[h]
                elif hora[h] == 12:
                    soma = soma + temp[h]
                else:
                    soma = soma + temp[h]
                medidia = medidia + (soma / 3)
                i = i + 1
    result = medidia / i
    return result
#Função para calcular a temperatura mínima com horários específicos  
def TempMinimaE(datas,hora,temp,horario,mesA,mesB):
    i = 1
    menor = 0
    for m in range (len(datas)):
        if mesA <= datas[m][3:5] <= mesB:
            for h in range (len(hora)):
                if int(hora[h]) == horario:
                    if i == 1:
                        menor = temp[h]
                    elif menor > temp[h]:
                        menor = temp[h]
                    i = i + 1
    return menor
#Função para calcular a temperatura mínima a partir de todos horários 
def TempMinimaT(datas,hora,temp,mesA,mesB):
    medidia = 0
    i = 1
    menor = 0
    for m in range (len(datas)):
        if mesA <= datas[m][3:5] <= mesB:
            for h in range (len(hora)):
                soma = 0
                if hora[h] == 0:
                    soma = soma + temp[h]
                elif hora[h] == 12:
                    soma = soma + temp[h]
                else:
                    soma = soma + temp[h]
                medidia = medidia + (soma / 3)
                if i == 1:
                    menor = medidia
                elif menor > medidia:
                    menor = medidia
                i = i + 1
    return menor
#Função para calcular a temperatura máxima a partir de horários específicos 
def TempMaximaE(datas,hora,temp,horario,mesA,mesB):
    i = 1
    maior = 0
    for m in range (len(datas)):
        if mesA <= datas[m][3:5] <= mesB:
            for h in range (len(hora)):
                if int(hora[h]) == horario:
                    if i == 1:
                        maior = temp[h]
                    elif maior < temp[h]:
                        maior = temp[h]
                    i = i + 1
    return maior
#Função para calcular a temperatura máxima a partir de todos horários
def TempMaximaT(datas,hora,temp,mesA,mesB):
    medidia = 0
    i = 1
    maior = 0
    for m in range (len(datas)):
        if mesA <= datas[m][3:5] <= mesB:
            for h in range (len(hora)):
                soma = 0
                if hora[h] == 0:
                    soma = soma + temp[h]
                elif hora[h] == 12:
                    soma = soma + temp[h]
                else:
                    soma = soma + temp[h]
                medidia = medidia + (soma / 3)
                if i == 1:
                    maior = medidia
                elif maior < medidia:
                    maior = medidia
                i = i + 1
    return maior                 
#Função para imprimir o resultado da pesquisa na tela                 
def ImprimeResultado(periodo,media,maxima,minima):
    if periodo == 1:
        print ('*'*45)
        print ('Resultado')
        print ('A temperatura mínima do período foi de', round(minima,2), 'ºC.')
        print ('A temperatura máxima do período foi de', round(maxima,2), 'ºC.')
        print ('A temperatura média do período foi de', round(media,2), 'ºC.')
    else: 
        print ('*'*45)
        print ('Resultado')
        print ('A temperatura mínima do período foi de', round(minima,2), 'ºC.')
        print ('A temperatura máxima do período foi de', round(maxima,2), 'ºC.')
        print ('A temperatura média do período foi de', round(media,2), 'ºC.')
 #Função para gravar o resultado da pesquisa em arquivo de texto               
def GravaArquivo(periodo,regiao,caminho,mesA,mesB,media,minima,maxima):
    arq = open (caminho, 'w')
    if periodo == 1:
        texto = ('*'*46)
        arq.write (texto)
        if regiao == 1:
            arq.write ('\nResultado para o período de 2018 em Curitiba')
        elif regiao == 2:
            arq.write ('\nResultado para o período de 2018 em Londrina')
        else:
            arq.write ('\nResultado para o período de 2018 em Paranaguá')
        texto2 = '\n\nA temperatura mínima do período foi de ' + str(round(minima,2)) + 'ºC.\n\n'
        arq.write (texto2)
        texto3 = '\n\nA temperatura máxima do período foi de ' + str(round(maxima,2)) + 'ºC.\n\n'
        arq.write (texto3)
        texto4 = '\n\nA temperatura média do período foi de ' + str(round(media,2)) + 'ºC.\n\n'
        arq.write (texto4)
        texto5 = ('*'*46)
        arq.write (texto5)
    else: 
        texto = ('*'*46)
        arq.write (texto)
        if regiao == 1:
            texto2 = '\n\nResultado para o período de ' + mesA +  ' a ' + mesB + ' em Curitiba.\n\n'
            arq.write (texto2)
        elif regiao == 2:
            texto2 = '\n\nResultado para o período de ' + mesA + ' a ' + mesB + ' em Londrina.\n\n'
            arq.write (texto2)
        else:
            texto2 = '\n\nResultado para o período de ' + mesA + ' a ' + mesB + ' em Paranaguá.\n\n'
            arq.write (texto2)
        texto3 = '\n\nA temperatura mínima do período foi de ' + str(round(minima,2)) + 'ºC.\n\n'
        arq.write (texto3)
        texto4 = '\n\nA temperatura máxima do período foi de ' + str(round(maxima,2)) + 'ºC.\n\n'
        arq.write (texto4)
        texto5 = '\n\nA temperatura média do período foi de ' + str(round(media,2)) + 'ºC.\n\n'
        arq.write (texto5)
        texto6 = ('*'*46)
        arq.write (texto6)
    arq.close()
#Função para imprimir o menu de região 
def MenuRegiao():
    print ('*'*45)
    print ('Escolha a região para realização da pesquisa:')
    print ('(1) Curitiba')
    print ('(2) Londrina')
    print ('(3) Paranaguá')
    print ('(0) Encerrar programa')
#Função para imprimir o menu de período 
def MenuPeriodo():
    print ('*'*58)
    print ('Informe um período de datas:')
    print ('(1) Ao ano.')
    print ('(2) De um mês inicial até um mês final dentro do mesmo ano.')
#Função para imprimir o menu de opção de horários específicos ou todos horários     
def MenuOpcao():
    print ('*'*68)
    print ('Informe o que deseja ser considerado em relação aos horários:')
    print ('(1) Um horário específico da leitura, podendo ser às 0h – 12h – 18h.')
    print ('(2) Todos os horários (0h,12h e 18h) e a impressão de um valor médio\n    de leitura diária.')
#Função para imprimir o menu de opção de resultados 
def MenuResultado():
    print ('*'*63)
    print ('Escolha o modo de exibição do resultado')
    print ('(1) Impressão do resultado na tela')
    print ('(2) Gravar resultado em arquivo de texto')
    print ('(3) Impressão do resultado na tela e gravar em arquivo de texto')