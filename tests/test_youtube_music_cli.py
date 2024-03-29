import os
from collections import deque

import pytest
from googleapiclient.errors import HttpError

import config.env as config
from utils.player import Player
from utils.playlist import Playlist
from youtube_music import YoutubeMusic

config.load_env()

DEVELOPER_KEY = os.environ["DEVELOPER_KEY"]
YOUTUBE_API_SERVICE_NAME = os.environ["YOUTUBE_API_SERVICE_NAME"]
YOUTUBE_API_VERSION = os.environ["YOUTUBE_API_VERSION"]


def test_search_query_success() -> None:
    youtube_music = YoutubeMusic(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, DEVELOPER_KEY)

    result = youtube_music.youtube_client.search().list(q="test", part="id, snippet").execute()

    assert result is not None


def test_search_query_ail() -> None:
    with pytest.raises(HttpError):
        youtube_music = YoutubeMusic(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, "fail")

        youtube_music.youtube_client.search().list(q="test", part="id, snippet").execute()


def test_player_youtube_search() -> None:
    youtube_music = YoutubeMusic(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, DEVELOPER_KEY)

    playlist = Playlist(playlist=deque())
    player = Player(playlist=playlist, youtube_music_search=youtube_music)

    assert player.youtube_music_search.search_and_get_track("test") is None
