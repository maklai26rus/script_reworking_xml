from tkinter import *
from tkinter import filedialog as fd
import os

import xml.etree.ElementTree as ET


class WinPrograms:

    def __init__(self, master):
        self.master = master
        self.top = TopWindow(self.master)
        self.top.doc_but['command'] = self.select_folder

        self.save_path = SaveXmlPath(self.master)
        self.save_path.doc_but['command'] = self.folder_save

        self.run_but = Frame(master)
        self.but_run = Button(self.run_but, text="Сохраним файлы", command=self.save_data)

        self.run_but.pack()
        self.but_run.pack(padx=25, pady=25)

    def save_data(self):
        start_path = str(self.top.doc_folder.get(1.0, END)).rstrip()
        for dirpath, dirnames, filenames in os.walk(start_path):
            for filename in filenames:  # перебираем все файлы
                path_xml = os.path.join(dirpath, filename)
                self.my_doc_xml(path_xml, filename)

    def my_doc_xml(self, path_xml, filename):
        my_doc = ET.parse(path_xml)
        root = my_doc.getroot()  # тут что то с выбором xml
        finish_path = str(self.save_path.doc_folder.get(1.0, END)).rstrip() + "/" + filename
        for i in root.iter('Sample'):  # ищем все стеки Sample
            rank = i.find('Targets/Target/Code').text  # погружаемся по нему вглубь и ищем '20.200'
            if rank == '20.200':  # сравниваем наш поиск
                biomaterialcode = i.find('BiomaterialCode').text = '369'  # меняем строчку 303 на 369
                code = i.find('Targets/Target/Code').text = '20.100'  # меняем строчку '20.200' на '20.100'
                my_doc.write(f'{finish_path}', encoding='utf-8')  # сохранения

    def select_folder(self, ):
        """
        Выбирает папку и вносит его в тектовое поля выбора
        :return:
        """
        filename = fd.askdirectory()
        self.top.doc_folder.delete(1.0, END)
        self.top.doc_folder.insert(1.0, filename)

    def folder_save(self, ):
        """
        Выбирает папку для сохранения
        :return:
        """
        filename = fd.askdirectory()
        self.save_path.doc_folder.delete(1.0, END)
        self.save_path.doc_folder.insert(1.0, filename)


class TopWindow:

    def __init__(self, master):
        self.top = Frame(master)
        self.top = LabelFrame(text="Выбор папки с исходным материалом")
        self.doc_folder = Text(self.top, width=50, height=1)
        self.doc_but = Button(self.top, text="...", )
        self.doc_folder.pack(side=LEFT, padx=5, pady=5)
        self.doc_but.pack(side=LEFT, padx=5, pady=5)
        self.top.pack()


class SaveXmlPath:

    def __init__(self, master):
        self.save = Frame(master)
        self.save = LabelFrame(text="Выбор папки для сохранения")
        self.doc_folder = Text(self.save, width=50, height=1)
        self.doc_but = Button(self.save, text="...", )
        self.doc_folder.pack(side=LEFT, padx=5, pady=5)
        self.doc_but.pack(side=LEFT, padx=5, pady=5)
        self.save.pack()


root = Tk()
root.minsize(width=500, height=150)
root.title('Меняем номер пробирки')


def main():
    run = WinPrograms(master=root)
    root.mainloop()


if __name__ == "__main__":
    main()
