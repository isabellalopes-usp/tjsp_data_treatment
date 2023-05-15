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
    
def busca_ocorrencias (termo, i, parada):

  final = ""
  termo = termo.upper()
  texto = acordaos[i].upper()
  texto = normalize('NFKD', texto).encode('ASCII','ignore').decode('ASCII')
  numero = 1

  tamanho = len(texto)
  while((termo in texto)):
    start = int(texto.index(str(termo)))
    letra = str(acordaos[i][start])
    substituir = acordaos[i][start]
    novo= ""

    j = 1
    while (letra!=str(parada) and (start+j)!=tamanho):
      novo = str(novo)+str(letra)
      letra = str(acordaos[i][start+j])
      if (j<len(termo)):
        substituir = substituir + acordaos[i][start+j]
      j+=1
    novo = str(novo)+str(letra)

    letra = str(acordaos[i][start-1])
    j = 2
    while (letra!=str(parada)):
      novo = str(letra)+str(novo)
      letra = str(acordaos[i][start-j])
      j+=1

    texto = texto.replace(termo,"", 1)
    final = str(final) + str("OCORRENCIA ") + str(numero)+ str(": ") + str(novo)+str('\n')+str('\n')
    numero+=1

    
  return final


def busca_mencoes(i,num):

    num = str(num)
    n_processo0 = num

    n_processo1=""
    for k in range (7):
      if(k<=len(num)):
        n_processo1 = n_processo1 + num[k]
    n_processo1 = n_processo1 + "-"

    for k in range (7,9):
      if(k<=len(num)):
        n_processo1 = n_processo1 + num[k]
    n_processo1 = n_processo1 + "."

    for k in range (9,13):
      if(k<len(num)):
        n_processo1 = n_processo1 + num[k]
    n_processo1 = n_processo1 + "."

    for k in range (13,14):
      if(k<len(num)):
        n_processo1 = n_processo1 + num[k]
    n_processo1 = n_processo1 + "."

    for k in range (14,16):
      if(k<len(num)):
        n_processo1 = n_processo1 + num[k]
    n_processo1 = n_processo1 + "."

    for k in range (16,20):
      if(k<len(num)):
        n_processo1 = n_processo1 + num[k]

    m = ""
    
    for l in range (0, len(acordaos)):
      if(processo[l]!=processo[i] and (str(n_processo1) in str(acordaos[l]))):
        acordaos[l] = acordaos[l].replace(n_processo1,n_processo0, 1)
        t = str(busca_ocorrencias(n_processo0,l,'.'))
        m += str("PROCESSO: ") + str(processo[l]) + str("\n") +str("ASSUNTO: ") + str(assunto[l]) + str("\n") + str("TRECHOS: \n") + t + str("\n\n")
        
    return m

  
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
  
  #procura ocorrencias do termo nos acordaos
  coluna_trechos = []
  for i in range (0, len(acordaos)):
    coluna_trechos.insert(i, busca_ocorrencias(z,i, '.'))

  #procura mencoes de acordaos em outros acordaos
  coluna_mencoes = []
  for i in range (0, len(acordaos)):
    coluna_mencoes.insert(i, busca_mencoes(i,processo[i]))

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
    
