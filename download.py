from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
auth_url = gauth.CommandLineAuth() # Url para autenticação, o usuário precisa visitar uma vez

# Cria uma instância autenticadaa do GoogleDrive
drive = GoogleDrive(gauth)

# Cria uma lista com todos os arquivos do google drive
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
# Looping que percorre os arquivos da lista e faz download
for file1 in file_list:
    download_mimetype = None
    mimetypes = ''
    if file1['mimeType'] in mimetypes:
        download_mimetype = mimetypes[file1['mimeType']]

    file1.GetContentFile(file1['title'], mimetype=download_mimetype)