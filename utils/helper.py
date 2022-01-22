import re

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
###  Select Track Number  ###"""

MATCH_TEXT_SET = {"lyrics", "audio", "official explicit audio", "official audio"}


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


def remove_command() -> None:
    print(REMOVE_MUSIC_TEXT)
