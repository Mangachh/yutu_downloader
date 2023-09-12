from serv.downloader import Downloader
from views.main_window import MainWindow
from threading import Thread

import asyncio

class DownController():
    _main_window: MainWindow
    _downloader: Downloader
    
       
    def __init__(self):
        print("init")
        # create main window
        self._main_window = MainWindow.init_default_window()
        
        # create downloader
        self._downloader = Downloader()
        # add events and so...
        
    def _on_click_search(self, link:str, mime:str, on_complete_search) -> None:
        """
        Event raised when clicking search

        Args:
            link (str): Link of the video/audio
            mime (str): Type of the link
        """
        print("OnClick controller")
        print(f"Link: {link}\tMime: {mime}")
        # get the list
        
        Thread(target=self._streams_thread, args=(link, mime, on_complete_search)).start()
    
    def _streams_thread(self, link, mime, on_complete_search) -> None:
        title, streams_text = self._downloader.get_streams(link, mime) 
        self._main_window.populate_list(title, streams_text)
        on_complete_search()
        
          
    def _on_download(self, link: str, itag:str, path:str, on_completed) -> None:
        """
        Event raised when download is clicked

        Args:
            link (str): link to download
            itag (str): itag to download
            path (str): path to download
        """
        # self._downloader.download(link, itag, path)
        # asyncio.run(self._downloader.download(link, itag, path, on_completed))
        print("Before thread")
        Thread(target=self._downloader.download, args=(link, itag, path, on_completed)).start()
        
        print("After thread")
    
    
    def start(self) -> None:
        """
        Start the controller
        """
        self._main_window.subscribe_on_click_search(self._on_click_search)
        self._main_window.subscribe_on_click_download(self._on_download)
        self._main_window.mainloop()