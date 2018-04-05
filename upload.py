from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os import listdir

gauth = GoogleAuth()
auth_url = gauth.CommandLineAuth() # Url para autenticação, o usuário precisa visitar uma vez

# Cria uma instância autenticadaa do GoogleDrive
drive = GoogleDrive(gauth)

# Cria uma lista com todos os arquivos do google drive
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

# Looping que percorre e apaga todos os arquivos
for file2 in file_list:
    file2.Delete()

# Função para upload de arquivos informando o caminho
def upload_arq(caminho):
    lista_arq = listdir(caminho)
    for arquivo in lista_arq:
        file1 = drive.CreateFile()
        # Lê o arquivos e seta o conteúdo para a instância
        file1.SetContentFile(caminho + '\\' + arquivo)
        file1['title'] = arquivo
        file1.Upload() # Faz o upload do arquivo.
        print('title: %s, mimeType: %s' % (file1['title'], file1['mimeType']))

upload_arq('arquivos')