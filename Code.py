import biblioteca as bib    #Importa a biblioteca 
#*** Programa principal ***
caminho = 'Curitiba.csv'            #Variável para ler caminho de Curitiba
caminho2 = 'Londrina.csv'           #Londrina
caminho3 = 'Paranagua.csv'          #Paranaguá
 
#*** Entrada de Dados ***
#Impressao do menu e inicialização da variável de região(regiao)
while True:
    bib.MenuRegiao()
    regiao = int (input ('Informe a região desejada:'))
    while regiao < 0 or regiao > 3:
        print ('Valor inválido!')
        regiao = int (input ('Informe a região desejada:'))
    if regiao == 0:
        print ('O programa está sendo encerrado...')
        break
    else:
        if regiao == 1:
            [datas,hora,temp] = bib.learquivo(caminho)
        elif regiao == 2:
            [datas,hora,temp] = bib.learquivo(caminho2)
        else:
            [datas,hora,temp] = bib.learquivo(caminho3) 
#Impressão do menu de datas e inicialização da variável de período(periodo)
    bib.MenuPeriodo()
    periodo = int (input ('Informe o período desejado:'))
    while periodo <1 or periodo > 2:
        print ('Valor inválido!')
        periodo = int (input ('Informe o período desejado:')) 
    if periodo == 1:                                     #Estrutura para período de ano
        ano = int (input ('Digite o ano (2018):'))
        while ano != 2018:
            print ('Valor inválido!')
            ano = int (input ('Digite o ano (2018):'))
        mesA = '01'
        mesB = '12'     
    else:                                                #Estrutura para período de mês inicial e mês final
        mesA = int (input ('Digite o mês inicial:'))
        while mesA < 1 or mesA > 11:
            print ('Valor inválido!!')
            mesA = int (input ('Digite o mês inicial:'))
        mesB = int (input ('Digite o mês final:'))
        while mesB < 2 or mesB > 12 or mesB <= mesA:
            print ('Valor inválido!')
            mesB = int (input ('Digite o mês final:'))
        if mesA <= 9:
            mesA = '0'+ str (mesA)
        else:
            mesA = str (mesA)
        if mesB <= 9:
            mesB = '0'+ str (mesB)
        else:
            mesB = str (mesB)             
#Impressão do menu de horários e inicialização da variável de opção de horários(opcao)
    bib.MenuOpcao()
    opcao = int (input ('Informe a opção desejada:'))
    while opcao < 1 or opcao > 2:
        print ('Valor inválido!')
        opcao = int (input ('Informe a opção desejada:'))     
    if opcao == 1:          #Estrutura para receber o valor do horário específico
        print ('*'*53)
        horario = int (input ('Informe o horário específico desejado (0 , 12 ou 18):'))
        while horario != 0 and horario != 12 and horario != 18:
            print ('Valor inválido!')
            horario = int (input ('Informe o horário específico desejado (0 , 12 ou 18):')) 
            
#*** Cálculos *** 
    if opcao == 1:   #Estrutura para calcular as temperaturas mínimas médias e máximas com horário específico
        media = bib.TempMediaE(datas,hora,temp,horario,mesA,mesB)
        minima = bib.TempMinimaE(datas,hora,temp,horario,mesA,mesB)
        maxima = bib.TempMaximaE(datas,hora,temp,horario,mesA,mesB)
    else:            #Estrutura para calcular as temperaturas mínimas médias e máximas com todos horários                    
        media = bib.TempMediaT(datas,hora,temp,mesA,mesB)
        minima = bib.TempMinimaT(datas,hora,temp,mesA,mesB)
        maxima = bib.TempMaximaT(datas,hora,temp,mesA,mesB)

#*** Saída de Dados ***     
#Impressão do menu de escolha de modo de obtenção dos resultados e inicialização da variável de modo de exibição(modo)
    bib.MenuResultado()
    modo = int (input ('Informe a opção desejada:'))
    while modo < 1 or modo > 3:
        print ('Valor inválido!')
        modo = int (input ('Informe a opção desejada'))
    if modo == 1:      #Imprime o resultado na tela
        bib.ImprimeResultado(periodo,media,maxima,minima)
    else:           #Grava o resultado em arquivo
        caminho = 'Resultados.txt'
        bib.GravaArquivo(periodo,regiao,caminho,mesA,mesB,media,minima,maxima)
        print ('*'*41)
        print ('Resultado gravado em arquivo com sucesso!')
        if modo == 3:                    #Imprime na tela depois de gravar em arquivo o resultado
                bib.ImprimeResultado(periodo,media,maxima,minima)