from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
auth_url = gauth.CommandLineAuth() # Create authentication url user needs to visit

# Create GoogleDrive instance with authenticated GoogleAuth instance.
drive = GoogleDrive(gauth)

file1 = drive.CreateFile()
# Read file and set it as a content of this instance.
file1.SetContentFile('upload_arq.txt')
file1.Upload() # Upload the file.
print('title: %s, mimeType: %s' % (file1['title'], file1['mimeType']))