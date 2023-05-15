#importa pacotes e bibliotecas
import pandas as pd
import numpy as np
import re
import os
from unicodedata import normalize
from google.colab import drive
drive.mount('/content/drive')

lista=[]
todos = pd.read_excel("/content/drive/Shareddrives/Inteligência Artificial: Regulação Jurídica e Políticas Públicas/etapa_1/termos_utilizados.xlsx")
t_total = todos['termo']
for t in t_total:
  if os.path.exists("/content/drive/Shareddrives/Inteligência Artificial: Regulação Jurídica e Políticas Públicas/etapa_1/TJSP/Raspagem/arquivos_finais/com-acordaos-"+t+".xlsx"):
    lista.append(t)

def retira_termos():
  #retirando termos
  acordaos=acordaos_originais
  for i in range (0, len(acordaos)): #para cada acordao
    for j in termos:
      acordaos[i] = re.sub(j,'',str(acordaos[i]), flags = re.IGNORECASE)

    #identifica e retira o nome do relator
    relator = df['relator'][i]
    if (relator in str(acordaos[i])):
      acordaos[i] = acordaos[i].replace(relator, "")

    #identifica e retira o nome do relator, se estiver em letra maiuscula
    relator1 = relator.upper()
    if (relator1 in str(acordaos[i])):
      acordaos[i] = acordaos[i].replace(relator1, "") 
      
termos=['TRIBUNAL.+JUSTI.A.+PAULO','TRIBUNAL.+JUSTI.A','PODER\sJ.+O','AS.+ELETR.NICA','ac.rd.o\n','\s\srelator(a)\n','\s\s\srelator\n','apel.+\s.+\d','reg.+\d','voto.+\d','decl.+\d','s.o.+\sde\s.+\sde\s20[0-2][0-5]','c.mara\n','c.mara:','.*c.mara.+justi.a\n','.*c.mara.+paulo\n','fl.*\d','\n..\n','\n.\n','\n\s*\n','\s\B']

#para cada termo do resultado
for z in lista:
  #abre planilha
  caminho = "/content/drive/Shareddrives/Inteligência Artificial: Regulação Jurídica e Políticas Públicas/etapa_1/TJSP/Raspagem/arquivos_finais/com-acordaos-"+z+".xlsx"
  df = pd.read_excel(caminho)

  #cria vetores
  acordaos = df['acordao']
  acordaos_originais = df['acordao']
  processo = df['processo']
  assunto = df['assunto']

  #faz limpeza
  retira_termos()

  #atualiza colunas
  tabela = {'classe': df['classe'],
          'assunto': df['assunto'],
          'relator': df['relator'],
          'comarca': df['comarca'],
          'orgao_julgador': df['orgao_julgador'],
          'data_julgamento':df['data_julgamento'],
          'data_publicacao':df['data_publicacao'],
          'processo': df['processo'], 
          'idacordao': df['idacordao'], 
          'acordao': acordaos,
          'trechos': coluna_trechos,
          'mencoes': coluna_mencoes,}

    
  #salva no drive
  final = pd.DataFrame(tabela)
  (final.sort_values(by='relator')).to_excel(caminho,index = False);
    

