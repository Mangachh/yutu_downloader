from pytube import YouTube as yt
from pytube.streams import Stream
# from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import pathlib
import os
import ffmpeg
import subprocess

MIME_VIDEO = "video"
MIME_AUDIO = "audio"

class Downloader():
    
    def __init__(self) -> None:
        self._streams = [Stream]
        
    @property
    def get_title(self)->str:
        return self._title
        
    def get_streams(self, link: str, mime_type: str, on_complete_search) -> (str, list[dict]):
        """
        Gets all the streams filtered by the mime

        Args:
            link (str): link where the stream are
            mime_type (str): desired type

        Returns:
            list[dict]: dictionary with all the streams
        """
        print(f"Looking for link {link}")
        try:
            url = yt(link)
        except Exception as e:
            print("Wrong link")
            on_complete_search()
            return "",[]
        
        # save all the streams in our list, this way
        # when downloading video will
        
        stream_text : list[dict]
        stream_text = []
        
        # self._streams = [stream for stream in url.streams if mime_type == stream.type]
    
        for stream in url.streams.filter(only_audio=(mime_type == MIME_AUDIO),
                                        only_video=(mime_type == MIME_VIDEO)).all():            
            if stream.type == mime_type:
                if stream.type == MIME_AUDIO:
                    stream_text.append(self.audio_dict(stream))
                else:
                    stream_text.append(self.video_dict(stream))
        
        
        
        
        # print(stream_text)
        on_complete_search()
        return (url.title, stream_text)
    
    def audio_dict(self, stream: Stream) -> dict[str, str]:
        """
        Converts an AUDIO stream to a dictionary

        Args:
            stream (Stream): stream to convert

        Returns:
            dict[str, str]: dictionary 
        """
        audio = {}
        audio["itag"] = stream.itag
        audio["qual"] = stream.abr
        audio["file"] = stream.mime_type.strip("audio/")
        audio["codec"] = stream.audio_codec
        return audio
    
    def video_dict(self, stream: Stream) -> dict[str, str]:
        """
        Converts a VIDEO stream to a dictionary

        Args:
            stream (Stream): video stream

        Returns:
            dict[str, str]: video dictionary
        """
        video = {}
        video["itag"] = stream.itag
        video["res"] = stream.resolution
        video["fps"] = stream.fps
        video["video"] = stream.mime_type.strip("video/")
        # video["codec"] = stream.video_codec
        return video        

    def download(self, link:str, itag: str, path:str, on_complete)-> None:
        """
        Downloads a stream to a desired path. If the stream has audio type, 
        converts it to .mp3"

        Args:
            link (str): link for the video/audio
            itag (str): itag of the stream to download
            path (str): path to dowload
        """
        # get the stream
        print("Downloader method")
        url = yt(link)
        
        try:
            stream = url.streams.get_by_itag(int(itag))
        except Exception as e:
            print(e)
            on_complete
            return
            
        file = stream.download(output_path=path, filename_prefix="tmp_")
        print(f"Saved to {file}")
        
        # TODO: tidy up all of this
        # remove moviePy
        # subscribe to events to show progress
        # methods for audio and video
        #fuck, is harder than i thought
        if stream.type == MIME_AUDIO:
            # change extension to mp3
            file_path = pathlib.Path(file)
            new_path = file_path.with_suffix(".mp3")
            try:
                renamed = file_path.rename(new_path)
                print(f"Renamed to: {renamed}")
            except Exception as e:
                print(e)
        else: # if is video
            if stream.is_adaptive: # and adaptative, download the first audio and merge
                audio = url.streams.filter(file_extension="mp4", only_audio=True).desc().first()
                try:
                    audio_file = audio.download(output_path=path, filename_prefix="audio_")
                    new_path = pathlib.Path(audio_file).with_suffix(".mp3")
                    try:
                        audio_file = pathlib.Path(audio_file).rename(new_path)
                        print(f"Renamed to: {audio_file}")
                    except Exception as e:
                        print(e)
                        
                    # this is slow
                    # video_clip = ffmpeg.input(file)
                    # audio_clip = ffmpeg.input(audio_file)
                    # ffmpeg.concat(video_clip, audio_clip, v=1, a=1).output(f"{path}/{url.title}_.mp4").run(overwrite_output=True)
                    
                    # this is fastest
                    # like a lot
                    subprocess.run(f"ffmpeg -i \"{file}\" -i \"{audio_file}\" -c copy \"{path}/{url.title}_.mp4\"")
                    os.remove(audio_file)
                    os.remove(file)
                                   
                except Exception as e:
                    print(e)
                pass
            
            
            # if video, download the audio pfffff
            # and merge
        print("completed")
        on_complete()