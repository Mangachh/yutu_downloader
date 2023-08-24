import tkinter as tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

DEF_LINK = "https://www.youtube.com/watch?v=o4qroNA05xs&list=RDyNcdVuPVXR0&index=16"

class MainWindow(tk.Tk):   
    
    _COLOR_BACK = "#0E2E47"
    _COLOR_FONT = "white"
    _WIN_HEIGHT = 600
    _WIN_WIDTH = 1100
    
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        # default settings
        self.link = tk.StringVar()
        self.btn_search: Button
        # self.link_enter tk.Entry
        self.mime_var = tk.StringVar()
        self.on_click_search_methods = []
        self.on_click_download_methods = []
        self.list_frame: tk.Frame
        self.itag_selection = tk.StringVar()
        self.radio_list_buttons = [tk.Radiobutton]
        self.btn_download = tk.Button
        
    @staticmethod
    def init_default_window() -> tk.Tk:
        """
        Creates a main window

        Returns:
            tk.Tk: main window
        """
        window = MainWindow()
        window.geometry(f'{window._WIN_WIDTH}x{window._WIN_HEIGHT}')
        window.title("Yutú Downloader :D")
        window.config(bg=window._COLOR_BACK)
        window.create_search_frame()        
        window.create_video_audio_frame()
        window.resizable(width=False, height=False)
        photo = tk.PhotoImage(file="./data/youtube_icon.png")
        window.iconphoto(False, photo)
        return window
    
    
    def create_search_frame(self) -> None:
        """
        Creates the search frame with all the widgets
        """
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        frame = tk.Frame(self, background= self._COLOR_BACK, width=700, height=self._WIN_HEIGHT)
        frame.grid(row=0, column=0)
        frame.grid_propagate(False)
        frame.pack_propagate(False)
        
        # labels
        lbl_title = tk.Label(frame, anchor="n", text="Yutú Downloader", font="arial 22 bold", bg=self._COLOR_BACK, foreground=self._COLOR_FONT)
        lbl_link = tk.Label(frame, anchor="w", text="Yutú Link:", font="arial 14", bg=self._COLOR_BACK, fg=self._COLOR_FONT)
        lbl_title.place(relx=0.5, rely=0.1, anchor="center")
        lbl_link.place(relx=0.1, rely=0.25, anchor='w')        
        
        # delete text button
        tk.Button(frame, text="DEL TEXT", command=lambda: self.link.set(""), font="arial 12 bold").place(relx=0.8, rely=0.25, anchor="center")

        # input
        ent_input = tk.Entry(frame, font="arial 14", width=50, textvariable=self.link)   
        # self.link.set("https://www.youtube.com/watch?v=bkk59ARFv80")       
        ent_input.place(relx=0.1, rely=0.32, anchor='w')
        
        # radio
        rd_video = tk.Radiobutton(frame, text="Video", variable=self.mime_var, value="video", command=self.on_select_radio, bg=self._COLOR_BACK, font="arial 12 bold", fg=self._COLOR_FONT, selectcolor=self._COLOR_BACK)
        rd_audio = tk.Radiobutton(frame, text="Audio", variable=self.mime_var, value="audio", command=self.on_select_radio, bg=self._COLOR_BACK, font="arial 12 bold", fg=self._COLOR_FONT, selectcolor=self._COLOR_BACK)
        self.mime_var.set("video")
        rd_video.place(relx=0.1, rely=0.37, anchor="w")
        rd_audio.place(relx=0.3, rely=0.37, anchor="w")
        
        # search button
        self.btn_search = tk.Button(frame, text="SEARCH", command=self.on_click_search, font="arial 18 bold")
        self.btn_search.place(relx=0.5, rely=0.5, anchor="center")
        
        # download button
        self.btn_download = tk.Button(frame, text="DOWNLOAD", command=self.on_click_download, font="arial 18 bold")
        
        self.btn_download.place_forget()
      
    def create_video_audio_frame(self) -> None:
        """
        Creates the video-audio frame with all the widgets
        """
        self.list_frame = tk.Frame(self, bg=self._COLOR_BACK, width=430, height=self._WIN_HEIGHT)
        self.list_frame.grid(row=0, column=1, sticky=tk.W+tk.N)
        self.list_frame.grid_propagate(False)
        self.list_frame.pack_propagate(False)
        
        
    
        
    
    def on_select_radio(self)->None:
        """
        A simple event that shows the selection of the radio button
        """
        selection = "Option " + self.mime_var.get()
        print(selection)
    
    def on_click_search(self) -> None:
        """
        Event raised when btn_search is clicked
        """
        print("Click!")
        print(f"Link: {self.link.get()}\nMime: {self.mime_var.get()}")
        self.btn_search.config(text="SEARCHING")
        self.update_idletasks()
        # aquí ira la func que queremos
        for m in self.on_click_search_methods:
            try:
                m(self.link.get(), self.mime_var.get())
            except Exception as e:
                print(e)
        self.btn_search.config(text="SEARCH")
        
        # Download button
        if self.itag_selection.get():
            self.btn_download.place(relx=0.5, rely=0.6, anchor="center")
        
    def on_click_download(self) -> None:
        """
        Event raised when btn_download is clicked
        """
        print("Donwloading")
        path = filedialog.askdirectory(title="Select Folder")
        self.btn_download.config(text="DOWNLOADING")
        self.update_idletasks()
        for f in self.on_click_download_methods:
            try:
                f(self.itag_selection.get(), path)
            except Exception as e:
                print(e)
        self.btn_download.config(text="DOWNLOAD")
        
        
    def subscribe_on_click_search(self, fun) -> None:
        """_summary_
        Subscribes to the event raised when the button btn_search is clicked
        Args:
            fun (function [str]): function to raise,
        """
        print(type(fun))
        if(fun not in self.on_click_search_methods):
            self.on_click_search_methods.append(fun)
    
    
    def subscribe_on_click_download(self, fun) -> None:
        """
        Subscribe to the event raised when btn_download is clicked

        Args:
            fun (function[str, str]): _description_
        """
        print(type(fun))
        if(fun not in self.on_click_download_methods):
            self.on_click_download_methods.append(fun)
            
    def unsubscribe_on_click(self, fun) -> None:
        self.on_click_search_methods.remove(fun)
    
    
        
        
    def populate_list(self, title:str, link_list: list[dict]) -> None:
        """
        Populates the list with the values of the dictionary. Each stream is a radiobutton with
        the "itag" value of the dict.

        Args:
            title (str): Title of the video/audio
            link_list (list[dict]): List of streams dictionary. To properly show each dictionary has
            to have a "itag" key used as a value to identify.

        
        """
        text: str        
        self.list_frame.destroy()        
        self.create_video_audio_frame()
        # video title
        tk.Label(self.list_frame, bg=self._COLOR_BACK, fg=self._COLOR_FONT, text=title, font="arial 15 bold", wraplength=400, justify="left").pack()
        # first sort the list
        
        def t(e) -> int:
            """
            Method to sort the list with the quality of each 
            member.

            Args:
                e (dict): current value

            Returns:
                int: _description_
            """
            if('res' in e):
                return int(e['res'][:-1])
            else:
                return int(e['qual'][:-4])
        
        link_list.sort(reverse=True, key=t)
        
        for st in link_list:
            text = ""                     
            for k,v in st.items():
                if(k == "itag"):
                    continue
                
                print(f"{k} -> {v}")
                text += f"{k}: {v} \t"
            
            # TODO: put this radios into a list to delete all  
            radio_sel = tk.Radiobutton(
                self.list_frame,
                value=st["itag"],
                variable=self.itag_selection,
                command=self.on_select_radio,
                text=text,
                bg=self._COLOR_BACK,
                font="arial 10 bold",
                fg=self._COLOR_FONT,
                selectcolor=self._COLOR_BACK,
                justify="left"
            )
            
            radio_sel.pack(anchor="nw")
        
        self.itag_selection.set(link_list[0]["itag"])