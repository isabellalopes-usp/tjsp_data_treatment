import pandas as pd
from google.colab import drive
drive.mount('/content/drive')


planilhas=[]
todos = pd.read_excel("/content/drive/termos_utilizados.xlsx")
t_total = todos['termo']
for t in t_total:
  if os.path.exists('/content/drive/com-acordaos-'+t+'.xlsx'):
    planilhas.append(t)
    
def salva():
  #atualiza colunas
  tabela = p_new
  tabela['processo'] = lista_new

  final = pd.DataFrame(tabela)
  (final.sort_values(by='relator')).to_excel('/content/drive/com-acordaos-',index = False);
  
 for a in planilhas:
  lista_new=[]
  p_old = pd.read_excel('/content/drive/com-acordaos-'+a+'.xlsx')
  p_new = pd.read_excel('/content/drive/com-acordaos-'+a+'.xlsx')
  todos = pd.read_excel("/content/drive/termos_utilizados.xlsx")
  p1 = p_old['processo']
  p2 = p_new['processo']
  print(len(p1))
  print(len(p2))
  for i in range (len(p1)):
    p1[i] = str(p1[i])
  for i in range (len(p2)):
    p2[i] = str(p2[i])

  tem = 0
  num = ''
  for i in p2:
    for j in p1:
      if i == j:
        tem = 1
        num = j
    if(tem==0):
      lista_new.append('*'+i)
    else:
      lista_new.append(num)
      tem = 0
      num = ''
  salva()
