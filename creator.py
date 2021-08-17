import os
from pptx import Presentation
from pptx.util import Pt


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
    print("Você selecionou a música: {}".format(selected_file))
    complete_dir_file = dir + selected_file


def read_lyrics():
    lyric = open(complete_dir_file, 'r')
    prs = Presentation()
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    title.text = selected_file.replace(".txt", "").replace("-", " ").upper()
    i = 0
    par = []

    for line in lyric:
        line = line.strip('\n')
        if(line != ""):
            if(i == 0):
                paragraphy = line
            else:
                paragraphy = paragraphy + "\n" + line
        else:
            par.append(paragraphy)
            paragraphy = ""

        i += 1

    par.append(paragraphy)

    for ls in par:
        #print(ls)
        lyric_slide = prs.slide_layouts[0]
        slide = prs.slides.add_slide(lyric_slide)
        title = slide.shapes.title
        title.text = ls
        print(ls)

    #print(par)
    pptx_name = selected_file + ".pptx"
    pptx_name = pptx_name.replace(".txt", "")
    prs.save(pptx_name)



start()
files_verification()
archive_list()
select_song()
read_lyrics()
