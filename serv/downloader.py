from pytube import YouTube as yt
from pytube.streams import Stream
import pathlib

MIME_VIDEO = "video"
MIME_AUDIO = "audio"

class Downloader():
    _streams: list[Stream]
    _title:str
    
    def __init__(self) -> None:
        self._streams = [Stream]
        
    @property
    def get_title(self)->str:
        return self._title
        
    def get_streams(self, link: str, mime_type: str) -> list[dict]:
        print(f"Looking for link {link}")
        url = yt(link)
        self._streams = url.streams.filter(only_audio=(mime_type == MIME_AUDIO),
                                           only_video=(mime_type == MIME_VIDEO))
        self._title = url.title
        stream_text : list[dict]
        stream_text = []
        # self._streams = [stream for stream in url.streams if mime_type == stream.type]
        for stream in url.streams:            
            if stream.type == mime_type:
                if stream.type == MIME_AUDIO:
                    stream_text.append(self.audio_dict(stream))
                else:
                    stream_text.append(self.video_dict(stream))
        
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
        # video["codec"] = stream.video_codec
        return video        

    def download(self, itag: str, path:str)-> None:
        # stream = [i for i in self._streams if i.itag == itag]
        stream = [i for i in self._streams if i.itag == int(itag)]
        
        if len(stream) != 0:
            file = stream[0].download(output_path=path)
            print(f"Saved to {file}")
            
            if stream[0].type == MIME_AUDIO:
                # change extension to mp3
                file_path = pathlib.Path(file)
                new_path = file_path.with_suffix(".mp3")
                try:
                    renamed = file_path.rename(new_path)
                    print(f"Renamed to: {renamed}")
                except Exception as e:
                    print(e)
                