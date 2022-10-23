from __future__ import annotations

import pafy
from googleapiclient.discovery import build

from utils.helper import is_text_contained
from utils.logger import logger
from utils.track import Track

YOUTUBE_URL = "https://www.youtube.com/watch?v=%s"


class TrackDoesNotFound(Exception):
    def __init__(self, message: str = "Requested music does not found."):
        super().__init__(message)


class YoutubeMusic:
    def __init__(self, service_name: str, api_version: str, developer_key: str):
        self.current_track: Track | None = None
        self.playlist: list[Track] = []
        self.youtube_client = build(service_name, api_version, developerKey=developer_key)

    def get_audio_url_from_youtube_video(self, video_url: str) -> str:
        logger.info("Getting audio url form youtube video.")
        video = pafy.new(video_url)
        best_audio = video.getbestaudio()
        audio_streaming_link: str = best_audio.url

        return audio_streaming_link

    def handle_search_result(self, search_result: dict[str, dict[str, str]]) -> Track:
        video_id = search_result["id"]["videoId"]
        video_title = search_result["snippet"]["title"]

        if is_text_contained(video_title.split()):
            video_url = YOUTUBE_URL % video_id
            audio_url = self.get_audio_url_from_youtube_video(video_url)
            track = Track(video_title, video_id, video_url, audio_url)

            print(f"Added {video_title} to playlist.")

            return track

        raise TrackDoesNotFound

    def search_and_get_track(self, query: str) -> Track:
        search_response = self.youtube_client.search().list(q=query, part="id, snippet").execute()

        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                try:
                    return self.handle_search_result(search_result)
                except TrackDoesNotFound as error:  # TODO: need to implement
                    continue
