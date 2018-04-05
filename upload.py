from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
auth_url = gauth.CommandLineAuth() # Url para autenticação, o usuário precisa visitar uma vez

# Cria uma instância autenticadaa do GoogleDrive
drive = GoogleDrive(gauth)

# Cria uma lista com todos os arquivos do google drive
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

# Looping que percorre e apaga todos os arquivos
for file2 in file_list:
    file2.Delete()

file1 = drive.CreateFile()
# Lê o arquivos e seta o conteúdo para a instância
file1.SetContentFile('upload_arq.txt')
file1.Upload() # Faz o upload do arquivo.
print('title: %s, mimeType: %s' % (file1['title'], file1['mimeType']))