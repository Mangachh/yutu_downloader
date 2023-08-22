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
        
    def _on_click_search(self) -> None:
        # get the settings:
            # - mime
            # - link
            
        # pass the list to the view
            # - show data
            # - show miniature
        pass
    
    def _on_download(self) -> None:
        # download the video
        # TODO: with custom path?
        pass
    
    def start(self) -> None:
        self._main_window.mainloop()