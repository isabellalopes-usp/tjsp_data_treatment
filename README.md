# tjsp_data_treatment

Coleta de termos relevantes e limpeza de acórdãos do TJSP

Antes de utilizar as funções disponibilizadas, é necessário ter feito a raspagem de dados no TJSP de acordo com um determinada lista de termos. Estas funções têm o objetivo de facilitar a análise e a visualização das decisões raspadas.

O arquivo **"cleaning.py" **contém um programa que limpa espaços em branco e termos repetitivos dos acórdãos;

O código em **"collection.py"** aloca, em uma nova coluna das planilhas, os trechos de cada acórdão que contém o termo buscado, e também destaca menções entre processos diferentes;

Por fim, com **"mark_new_results.py"**, as planilhas de raspagem são comparadas com suas versões anteriores, e os novos processos encontrados são marcados com o caractere "*".
