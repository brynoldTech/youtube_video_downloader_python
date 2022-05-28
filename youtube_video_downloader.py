"""" welcome to my channel"""
"""" this video i'm gonna create"""
""" Youtube video downloader .."""
"""" this project i'm using tkinter and pytube packages ..."""
"""" lets start....! """

""" import packages """
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title(" Youtube video downloader- brynold")
root.config(bg='#2F8F9D')

Label(root, text='Youtube video downloader', font='arial 20 bold', bg='#2F8F9D').pack()

""" link entry .."""
link = StringVar()
Label(root, text='Please paste your link here', font='arial 20 bold', bg='#2F8F9D', fg='#B3e8e5').place(x=140, y=70)
link_enter = Entry(root, width=40, textvariable=link).place(x=55, y=110)

""" lets create function to download  """


def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text="DOWNLOADED", font='arial 20 bold',bg='#2F8F9D').place(x=180, y=250)


Button(root, text='DOWNLOAD', font='arial 20 bold', bg='#2F8F9D', fg='#2F8F9D', padx=2, command=download).place(x=180, y=150)

root.mainloop()
