import re
from dataclasses import InitVar

INIT_TEXT = """
##### YOUTUBE MUSIC CLI #####
[1] - add music in playlist
[2] - show playlist
[3] - stop music
[4] - resume music
[5] - help
[6] - exit
#############################
"""


def is_text_contained(title: str) -> bool:
    for text in title:
        text = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`'…》]", "", text)
        if text.lower() in {"lyrics", "audio", "official"}:
            return True

    return False


def init_command() -> None:
    print(INIT_TEXT)