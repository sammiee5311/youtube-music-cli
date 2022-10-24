from __future__ import annotations

import re
from typing import TYPE_CHECKING, Callable

from utils.logger import logger

if TYPE_CHECKING:
    from utils.player import Player
    from utils.playlist import Playlist

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

is_player_stop = False


def add_music_in_playlist(player: Player) -> None:
    music = input("Enter music name: ")
    player.add_music(music)
    player.play_music()


def show_playlist(player: Player) -> None:
    player.show_playlist()


def pause_music(player: Player) -> None:
    player.pause_music()


def stop_music(player: Player) -> None:
    player.stop_music()


def remove_music(player: Player) -> None:
    player.remove_music()


def resume_music(player: Player) -> None:
    player.play_music()


def next_music(player: Player) -> None:
    player.next_music()


def help(player: Player) -> None:
    init_command()


def exit(player: Player) -> None:
    global is_player_stop
    logger.info("Disconnect to music player.")
    is_player_stop = True


player_commands = {
    "1": add_music_in_playlist,
    "2": show_playlist,
    "3": pause_music,
    "4": stop_music,
    "5": remove_music,
    "6": resume_music,
    "7": next_music,
    "8": help,
    "0": exit,
}


def start_player(player: Player) -> None:
    while not is_player_stop:
        command = input("Enter command: ")
        player_command: Callable[[Player], None] | None = player_commands.get(command)

        if not player_command:
            print("Please, select exisit command.")
            continue

        player_command(player)


def is_text_contained(title: str) -> bool:
    for text in title:
        text = re.sub("[-=+,#/?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`'…》]", "", text)
        if text.lower() in MATCH_TEXT_SET:
            return True

    return False


def is_valid_track_number(track_number: int, maximum_track_number: int) -> bool:
    return 0 < track_number <= maximum_track_number


def init_command() -> None:
    print(INIT_TEXT)


def remove_command(playlist: Playlist) -> None:
    print(REMOVE_MUSIC_TEXT % playlist)


def print_playlist(playlist: Playlist) -> None:
    print(PLAYLIST_TEXT % playlist)
