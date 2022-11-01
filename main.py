import tabula
import zipfile

# Converter o anexo.pdf em CSV
tabula.convert_into("Anexo1.pdf", "Anexo1.csv", pages = "all", output_format = "csv")

# Substituir os nomes das tabelas OD e AMB
def replaceData(infos, data):
    for a, b in data.items():
        infos = infos.replace(a, b)
    return infos

# Legendas a serem substituidas
od_data = {'OD':'Seg. Odontológica'}
amb_data = {'AMB':'Seg. Ambulatorial'}
# lendo o arquivo para as substituições
with open('Anexo1.csv') as r:
   infos = r.read()
# criando o arquivo com os dados formatados
   with open('Anexo1.csv', 'w') as c:
      infos = replaceData(infos, od_data)
      infos = replaceData(infos, amb_data)
      c.write(infos)

# Compactar os arquivos em .zip
with zipfile.ZipFile("Teste_{Viniccius_Neves}.zip", "w") as myfiles:
   myfiles.write("Anexo1.csv")
   myfiles.close()
