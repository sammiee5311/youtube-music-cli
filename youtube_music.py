import collections
import os
from typing import Dict, List, Optional, Union

import pafy
from googleapiclient.discovery import build
from pyasn1.type.univ import Any

import config.helper as config
from config.track import Track
from utils import is_text_contained

config.load_env()

DEVELOPER_KEY = os.environ["DEVELOPER_KEY"]
YOUTUBE_API_SERVICE_NAME = os.environ["YOUTUBE_API_SERVICE_NAME"]
YOUTUBE_API_VERSION = os.environ["YOUTUBE_API_VERSION"]
YOUTUBE_URL = "https://www.youtube.com/watch?v=%s"


class YoutubeMusic:
    def __init__(self, maximum: int = 10):
        self.maximum = maximum
        self.current_track: Optional[Track] = None
        self.playlist: List[Track] = []
        self.youtube_client = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    def get_audio_url_from_youtube_video(self, video_url: str) -> str:
        video = pafy.new(video_url)
        best_audio = video.getbestaudio()
        audio_streaming_link: str = best_audio.url

        return audio_streaming_link

    def add_track_to_playlist(self, video_title: str, video_id: str, video_url: str, audio_url: str) -> None:
        track = Track(video_title, video_id, video_url, audio_url)
        if not self.current_track:
            self.current_track = track

        self.playlist.append(track)

    def handle_search_result(self, search_result: Dict[str, Dict[str, str]]) -> None:
        video_id = search_result["id"]["videoId"]
        video_title = search_result["snippet"]["title"]

        if is_text_contained(video_title.split()):
            video_url = YOUTUBE_URL % video_id
            audio_url = self.get_audio_url_from_youtube_video(video_url)

            self.add_track_to_playlist(video_title, video_id, video_url, audio_url)

    def search_and_add_to_playlist(self, query: str) -> None:
        search_response = self.youtube_client.search().list(q=query, part="id, snippet").execute()

        for search_result in search_response.get("items", []):
            if (self.playlist and self.current_track.video_id == self.playlist[-1].video_id) or self.maximum < len(
                self.playlist
            ):
                return
            if search_result["id"]["kind"] == "youtube#video":
                self.handle_search_result(search_result)

                print(f"Added {self.current_track.video_title} to playlist.")


if __name__ == "__main__":
    youtube_music = YoutubeMusic()
    youtube_music.search_and_add_to_playlist(query="drake")
