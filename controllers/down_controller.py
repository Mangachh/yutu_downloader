from serv.downloader import Downloader
from views.main_window import MainWindow

class DownController():
   
    
       
    def __init__(self):
        print("init")
        # create main window
        self._main_window = MainWindow.init_default_window()
        
        # create downloader
        self._downloader = Downloader()
        # add events and so...
        
    def _on_click_search(self, link:str, mime:str) -> None:
        print("OnClick controller")
        print(f"Link: {link}\tMime: {mime}")
        # get the list
        self._downloader.get_streams(link, mime) #TODO: list
                    
        # pass the list to the view
            # - show data
            # - show miniature
            
    def _on_download(self) -> None:
        # download the video
        # TODO: with custom path?
        pass
    
    def start(self) -> None:
        self._main_window.subscribe_on_click(self._on_click_search)
        self._main_window.mainloop()