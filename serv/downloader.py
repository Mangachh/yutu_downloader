from pytube import YouTube as yt
from pytube.streams import Stream

MIME_VIDEO = "video"
MIME_AUDIO = "audio"

class Downloader():
    _streams: list[Stream]
    
    def __init__(self) -> None:
        self._streams = [Stream]
        
    def get_streams(self, link: str, mime_type: str) -> list[dict]:
        print(f"Looking for link {link}")
        url = yt(link)
        self._streams.clear()
        stream_text : list[dict]
        stream_text = []
        # self._streams = [stream for stream in url.streams if mime_type == stream.type]
        for stream in url.streams:
            
            if stream.type == mime_type:
                if stream.type == MIME_AUDIO:
                    stream_text.append(self.audio_dict(stream))
                else:
                    stream_text.append(self.video_dict(stream))
                    
                    
                self._streams.append(stream)       
        
        # convert to a list of strings...
        print(self._streams)
        print(stream_text)
        return stream_text
    
    def audio_dict(self, stream: Stream) -> dict[str, str]:
        audio = {}
        audio["itag"] = stream.itag
        audio["qual"] = stream.abr
        audio["file"] = stream.mime_type.strip("audio/")
        audio["codec"] = stream.audio_codec
        return audio
    
    def video_dict(self, stream: Stream) -> dict[str, str]:
        video = {}
        video["itag"] = stream.itag
        video["res"] = stream.resolution
        video["fps"] = stream.fps
        video["video"] = stream.mime_type.strip("video/")
        video["codec"] = stream.video_codec
        return video        

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