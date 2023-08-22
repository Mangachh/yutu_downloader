from views.main_window import MainWindow
import controllers.down_controller as dw  
    
     
     
if __name__ == "__main__":    
    window = MainWindow.init_default_window(dw.downloader)
    window.mainloop()
    