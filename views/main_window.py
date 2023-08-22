import tkinter as tk
from tkinter import Label
from tkinter import Button

DEF_LINK = "https://www.youtube.com/watch?v=o4qroNA05xs&list=RDyNcdVuPVXR0&index=16"

class MainWindow(tk.Tk):   
    
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        # default settings
        self.link = tk.StringVar()
        self.download_button: Button
        # self.link_enter tk.Entry
        self.mime_var = tk.StringVar()
        self.on_click_methods = []
        
    @staticmethod
    def init_default_window() -> tk.Tk:
        window = MainWindow()
        window.geometry('500x500')
        window.create_search_frame()        
        
        return window
    
    
    def create_search_frame(self) -> None:
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        frame = tk.Frame(self, background="red", width=500, height=400)
        frame.grid(row=0, column=0, sticky="nw")
        frame.grid_propagate(False)
        
        # labels
        lbl_title = tk.Label(frame, anchor="n", text="Yutú Downloader", font="arial 22 bold")
        lbl_link = tk.Label(frame, anchor="w", text="Yutú Link:", font="arial 14")
        lbl_title.place(relx=0.5, rely=0.2, anchor="center")
        lbl_link.place(relx=0.1, rely=0.37, anchor='w')        
        
        # input
        ent_input = tk.Entry(frame, font="arial 14", width=37, textvariable=self.link)          
        ent_input.place(relx=0.1, rely=0.47, anchor='w')
        
        # radio
        rd_video = tk.Radiobutton(frame, text="Video", variable=self.mime_var, value="video", command=self.sel)
        rd_audio = tk.Radiobutton(frame, text="Audio", variable=self.mime_var, value="audio", command=self.sel)
        self.mime_var.set("video")
        rd_video.place(relx=0.1, rely=0.55, anchor="w")
        rd_audio.place(relx=0.3, rely=0.55, anchor="w")
        
        # search button
        btn_search = tk.Button(frame, text="SEARCH", command=self.on_click_search, font="arial 18 bold")
        btn_search.place(relx=0.5, rely=0.75, anchor="center")
        
    
    def sel(self)->None:
        selection = "Option " + self.mime_var.get()
        print(selection)
    
    def on_click_search(self) -> None:
        print("Click!")
        print(f"Link: {self.link.get()}\nMime: {self.mime_var.get()}")
        # aquí ira la func que queremos
        for m in self.on_click_methods:
            try:
                m(self.link.get(), self.mime_var.get())
            except Exception as e:
                print(e)
    
    def subscribe_on_click(self, fun) -> None:
        print(type(fun))
        if(fun not in self.on_click_methods):
            self.on_click_methods.append(fun)
            
    def unsubscribe_on_click(self, fun) -> None:
        self.on_click_methods.remove(fun)
    