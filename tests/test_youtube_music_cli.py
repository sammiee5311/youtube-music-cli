import os
from collections import deque

import config.helper as config
import pytest
from googleapiclient.errors import HttpError
from utils.player import Player
from utils.playlist import Playlist
from youtube_music import YoutubeMusic

config.load_env()

DEVELOPER_KEY = os.environ["DEVELOPER_KEY"]
YOUTUBE_API_SERVICE_NAME = os.environ["YOUTUBE_API_SERVICE_NAME"]
YOUTUBE_API_VERSION = os.environ["YOUTUBE_API_VERSION"]


def test_search_query_success():
    youtube_music = YoutubeMusic(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, DEVELOPER_KEY)

    result = youtube_music.youtube_client.search().list(q="test", part="id, snippet").execute()

    assert result is not None


def test_search_query_ail():
    with pytest.raises(HttpError):
        youtube_music = YoutubeMusic(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, "fail")

        youtube_music.youtube_client.search().list(q="test", part="id, snippet").execute()


def test_add_track_in_playlist():
    youtube_music = YoutubeMusic(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, DEVELOPER_KEY)

    playlist = Playlist(playlist=deque())
    player = Player(playlist=playlist, youtube_music_search=youtube_music)
    player.create_new_player()
    player.add_music("drake")
