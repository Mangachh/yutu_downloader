from pytube import YouTube as yt
from pytube.streams import Stream

MIME_VIDEO = "video"
MIME_AUDIO = "audio"

class Downloader():
    _streams: list[Stream]
    
    def __init__(self) -> None:
        self._streams = [Stream]
        
    def get_streams(self, link: str, mime_type: str) -> list[str]:
        print(f"Looking for link {link}")
        url = yt(link)
        self._streams.clear()
        self._streams = [stream for stream in url.streams if mime_type == stream.type]
        
        # convert to a list of strings...
        print(self._streams)
        return []
    

def downloader(link: str)-> None:
    print(link)
    url = yt(link)
    for stream in url.streams:
        # vamos a printear los videos
        if("video" in stream.mime_type):
            print(f"Video Stream: {stream}")
        # print(stream)
        # print(type(stream))
    #video = url.streams.first()
    #video.download()