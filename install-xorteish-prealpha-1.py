import requests 
import zipfile
import os
archive_url = "https://github.com/drarixdev/xorteish/archive/pre-alpha1.zip"
name_archive = "pre-alpha1.zip"
print("Installing please wait")


r = requests.get(archive_url) 

with open(name_archive,'wb') as f: 
  
 
    f.write(r.content) 

with zipfile.ZipFile(name_archive, 'r') as zip_ref:
    zip_ref.extractall()
os.remove(name_archive)
