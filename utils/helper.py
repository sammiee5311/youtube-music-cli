from __future__ import annotations

import re
from typing import TYPE_CHECKING

from utils.logger import logger

if TYPE_CHECKING:
    from utils.player import Player

INIT_TEXT = """
##### YOUTUBE MUSIC CLI #####
[1] - add music in playlist
[2] - show playlist
[3] - pause music
[4] - stop music
[5] - remove music
[6] - resume music
[7] - next music
[8] - help
[0] - exit
#############################
"""

REMOVE_MUSIC_TEXT = """
##### YOUTUBE MUSIC CLI #####
###  Select Track Number  ###
%s
#############################"""

PLAYLIST_TEXT = """
##### YOUTUBE MUSIC CLI #####
######### Playlist ##########
%s
#############################"""

MATCH_TEXT_SET = {"lyrics", "audio", "official explicit audio", "official audio"}


def start_player(player: Player) -> None:
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


def is_text_contained(title: str) -> bool:
    for text in title:
        text = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`'…》]", "", text)
        if text.lower() in MATCH_TEXT_SET:
            return True

    return False


def is_valid_track_number(track_number: int, maximum_track_number) -> bool:
    return 0 < track_number <= maximum_track_number


def init_command() -> None:
    print(INIT_TEXT)


def remove_command(playlist) -> None:
    print(REMOVE_MUSIC_TEXT % playlist)


def print_playlist(playlist) -> None:
    print(PLAYLIST_TEXT % playlist)
