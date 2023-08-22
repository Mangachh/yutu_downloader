import tkinter as tk
from tkinter import Label
from tkinter import Button

DEF_LINK = "https://www.youtube.com/watch?v=o4qroNA05xs&list=RDyNcdVuPVXR0&index=16"

class MainWindow(tk.Tk):   
    
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        # default settings
        self.link: tk.StringVar
        self.download_button: Button
        self.link_enter: tk.Entry
        self.int_var: tk.IntVar
        
    @staticmethod
    def init_default_window(func_to_download) -> tk.Tk:
        window = MainWindow()
        # window.geometry('500x300')
        # window.resizable(0,0)
        # window.title("Youtube Downloader")
        # # window
        # window = MainWindow()
        # window.geometry('500x300')
        # window.resizable(0,0)
        # window.title("Youtube Downloader")
        # 
        # # labels
        # tk.Label(window, text= 'Youtube Video Downloader', font ='arial 20 bold').pack()
        # window.link = tk.StringVar()
        # window.link.set = DEF_LINK
        # Label(window, text= 'Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
        # window.link_enter = tk.Entry(window, width = 70, textvariable=window.link).place(x=32, y= 90)
        # 
        # # video-audio 
        # window.int_var = tk.IntVar()
        # rd_audio = tk.Radiobutton(window, text="Audio", value=0, variable=window.int_var, command=window.sel).pack()
        # rd_video = tk.Radiobutton(window, text="Video", value=1, variable=window.int_var, command=window.sel).pack()
        # 
        # # search button
        # window.download_button = Button(
        #                             window, 
        #                             text = 'SEARCH', 
        #                             font = 'arial 15 bold', 
        #                             bg = 'pale violet red', 
        #                             padx = 2, 
        #                             command = lambda: func_to_download(str(window.link.get()))
        #                             ).place(x=180 ,y = 150)
        # return window
    
    def sel(self)->None:
        selection = "Option " + str(self.int_var.get())
        print(selection)
    
    def set_event_to_button(self, fun) -> None:
        self.download_button.configure(command=fun)
    
    