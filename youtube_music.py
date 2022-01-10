import collections
import os
from typing import Dict

import pafy
from googleapiclient.discovery import build

import config.helper as config
from utils import is_text_contained

config.load_env()

DEVELOPER_KEY = os.environ["DEVELOPER_KEY"]
YOUTUBE_API_SERVICE_NAME = os.environ["YOUTUBE_API_SERVICE_NAME"]
YOUTUBE_API_VERSION = os.environ["YOUTUBE_API_VERSION"]


class YoutubeMusic:
    def __init__(self, maximum: int = 10):
        self.maximum = maximum
        self.is_existed_playlist = False
        self.track_number = 0
        self.youtube_client = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    def youtube_stream_link(self, playlist: Dict[int, str], len_of_playlist) -> Dict[int, str]:
        self.track_number = len_of_playlist
        while self.track_number < len_of_playlist + len(playlist):
            self.track_number += 1
            url = "https://www.youtube.com/watch?v=" + str(playlist[self.track_number][0][-11:])
            video = pafy.new(url)
            best_audio = video.getbestaudio()
            audio_streaming_link = best_audio.url
            playlist[self.track_number].append(audio_streaming_link)

        return playlist

    def search(self, query: str, len_of_playlist: int = 0) -> str:
        search_response = self.youtube_client.search().list(q=query, part="id, snippet").execute()

        playlist = collections.defaultdict(list)

        if not self.is_existed_playlist:
            self.track_number = 0

        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                if is_text_contained(search_result["snippet"]["title"].split()):
                    self.track_number += 1
                    playlist[self.track_number].append(
                        "%s %s" % (search_result["snippet"]["title"], search_result["id"]["videoId"])
                    )
                if self.maximum == self.track_number:
                    break

        if len(playlist) != 0:
            audio_streaming_link = self.youtube_stream_link(playlist, len_of_playlist)
            return audio_streaming_link


if __name__ == "__main__":
    youtube_music = YoutubeMusic()
    youtube_music.search(query="drake")
