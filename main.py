from collections import deque

import click

from utils.helper import init_command
from utils.player import Player
from utils.playlist import Playlist
from youtube_music import YoutubeMusic


@click.option("--maximum", help="Maximum Queue for music(default: 10)")
def main() -> None:
    youtube_music = YoutubeMusic()

    playlist = Playlist(playlist=deque())
    player = Player(playlist=playlist, youtube_music_search=youtube_music)

    player.create_new_player()

    init_command()

    while True:
        command = input("Enter command: ")
        if command == "1":
            music = input("Enter music name: ")
            player.add_music(music)
            player.play_music()
        elif command == "2":
            if not player.playlist.is_empty() and not player.current_track:
                print("Playlist is Empty.")
            else:
                print(f"[C] {player.current_track.video_title}")
                for i, track in enumerate(player.playlist.playlist):
                    print(f"[{i+1}] {track.video_title}")
        elif command == "3":
            player.pause_music()
        elif command == "4":
            player.stop_music()
        elif command == "5":
            player.play_music()
        elif command == "6":
            player.next_music()
        elif command == "7":
            init_command()
        elif command == "8":
            print("BYE")
            break


if __name__ == "__main__":
    main()
