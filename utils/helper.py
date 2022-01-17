import re

INIT_TEXT = """
##### YOUTUBE MUSIC CLI #####
[1] - add music in playlist
[2] - show playlist
[3] - pause music
[4] - stop music
[5] - resume music
[6] - next music
[7] - help
[8] - exit
#############################
"""

MATCH_TEXT_SET = {"lyrics", "audio", "official explicit audio", "official audio"}


def is_text_contained(title: str) -> bool:
    for text in title:
        text = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`'…》]", "", text)
        if text.lower() in MATCH_TEXT_SET:
            return True

    return False


def init_command() -> None:
    print(INIT_TEXT)
