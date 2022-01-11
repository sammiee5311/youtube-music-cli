import click

from utils import init_command
from youtube_music import YoutubeMusic


@click.option("--maximum", help="Maximum Queue for music(default: 10)")
def main() -> None:
    youtube_music = YoutubeMusic()

    init_command()

    while True:
        command = input("Enter command: ")
        if command == "1":
            music = input("Enter music name: ")
            youtube_music.search_and_add_to_playlist(music)
        elif command == "2":
            if not youtube_music.current_track:
                print("No track in playlist.")
                continue
            print("[C] %s" % youtube_music.current_track.video_title)
            for track in youtube_music.playlist[1:]:
                print(f"{track.video_title}")
        elif command == "3":
            pass
        elif command == "4":
            pass
        elif command == "5":
            pass
        elif command == "6":
            print("BYE")
            break


if __name__ == "__main__":
    main()
