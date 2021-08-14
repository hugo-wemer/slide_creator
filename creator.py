import os
from pptx import Presentation

def start():
    print("*********************************************")
    print("**Bem-vindo ao script de criação dos slides**")
    print("*********************************************")

def files_verification():
    print("Coloque a música que deseja na mesma pasta desse script. Tecle 'Enter' ao finalizar")
    status = input("")

def archive_list():
    global files, dir
    dir = os.getcwd()
    dir = dir + "/songs/"
    for root, dirs, files in os.walk(dir):
        songs = [files]
    return files

def select_song():
    global selected_file, complete_dir_file
    print("Selecione a música:")
    index = 0
    for i in files:
        print("({0}) - {1}".format(index, files[index]))
        index += 1
    selected_index = int(input(""))
    selected_file = files[selected_index]
    print("Você selecionou a música: {}". format(selected_file))
    complete_dir_file = dir + selected_file

def read_lyrics():
    lyric = open(complete_dir_file, 'r')
    index = 0
    prs = Presentation()
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    title.text = selected_file
    subtitle.text = "python-pptx was here!"

    pptx_name = selected_file + ".pptx"
    prs.save(pptx_name)

    for line in lyric:
        print(line.strip('\n'))




start()
files_verification()
archive_list()
select_song()
read_lyrics()