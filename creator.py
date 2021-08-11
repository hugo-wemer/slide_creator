import os
def start():
    print("*********************************************")
    print("**Bem-vindo ao script de criação dos slides**")
    print("*********************************************")

def files_verification():
    print("Coloque a música que deseja na mesma pasta desse script. Digite 'OK' ao finalizar")
    status = input("").upper
    if status == "OK":
        files_verification()

def archive_list():
    dir = os.getcwd()
    dir = dir + "/songs/"
    for root, dirs, files in os.walk(dir):
        songs = [files]
    print(files)
start()
files_verification()
archive_list()