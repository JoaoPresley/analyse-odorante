from analise import Analise

# Inicializa
anal = Analise()

# Trata os dados aplicando os filtros e NumPy concatenates
anal.transform_data()

# Gera e salva tanto a planilha quanto a imagem PNG na pasta /data
anal.outputload()