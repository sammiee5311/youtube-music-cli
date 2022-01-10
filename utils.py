import re


def is_text_contained(title: str) -> bool:
    for text in title:
        text = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`'…》]", "", text)
        if text.lower() in ["lyrics", "audio"]:
            return True

    return False
