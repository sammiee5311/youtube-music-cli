import os
from collections import deque

import click

import config.helper as config
from utils.helper import init_command
from utils.logger import logger
from utils.player import Player
from utils.playlist import Playlist
from youtube_music import YoutubeMusic

config.load_env()

DEVELOPER_KEY = os.environ["DEVELOPER_KEY"]
YOUTUBE_API_SERVICE_NAME = os.environ["YOUTUBE_API_SERVICE_NAME"]
YOUTUBE_API_VERSION = os.environ["YOUTUBE_API_VERSION"]


@click.option("--maximum", help="Maximum Queue for music(default: 10)")
def main() -> None:
    youtube_music = YoutubeMusic(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, DEVELOPER_KEY)

    playlist = Playlist(playlist=deque())
    player = Player(playlist=playlist, youtube_music_search=youtube_music)

    logger.info("Creating vlc player.")
    player.create_new_player()

    init_command()

    while True:
        command = input("Enter command: ")
        if command == "1":
            music = input("Enter music name: ")
            player.add_music(music)
            player.play_music()
        elif command == "2":
            player.show_playlist()
        elif command == "3":
            player.pause_music()
        elif command == "4":
            player.stop_music()
        elif command == "5":
            player.remove_music()
        elif command == "6":
            player.play_music()
        elif command == "7":
            player.next_music()
        elif command == "8":
            init_command()
        elif command == "0":
            logger.info("Disconnect to music player.")
            break


if __name__ == "__main__":
    main()
