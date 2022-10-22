import time
from dataclasses import dataclass
from typing import Optional, Union

import vlc
from youtube_music import YoutubeMusic

from utils.helper import is_valid_track_number, print_playlist, remove_command
from utils.playlist import Playlist, PlaylistIsEmpty
from utils.track import Track


@dataclass
class Player:
    playlist: Playlist
    youtube_music_search: YoutubeMusic
    media_player: Optional[vlc.MediaPlayer] = None
    instance: Optional[vlc.Instance] = None
    current_track: Optional[Track] = None

    @property
    def state(self) -> Union[vlc.State, None]:
        if not self.media_player:
            return None
        return self.media_player.get_state()

    def create_new_player(self) -> None:
        self.instance = vlc.Instance("--verbose 0")
        self.media_player = self.instance.media_player_new()

    def show_playlist(self) -> None:
        if not self.playlist.is_empty() and not self.current_track:
            print("Playlist is Empty.")
        else:
            print_playlist(self.playlist.get_tracks_in_string())

    def play(self):
        try:
            track = self.playlist.play_next_track()
            self.current_track = track
            self.media_player = self.instance.media_player_new()
            media = self.instance.media_new(track.audio_url)
            media.get_mrl()
            self.media_player.set_media(media)
            self.media_player.play()

            time.sleep(5)
            event_manager = self.media_player.event_manager()
            event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.end_callback)
        except PlaylistIsEmpty:
            print("Playlist is empty.")

    def end_callback(self, _):
        self.play()

    def add_music(self, name: str) -> None:
        track = self.youtube_music_search.search_and_get_track(name)
        if track is None:
            print("Please, type correct/specific music name.")
            return

        self.playlist.add_track_in_playlist(track)

        if self.state in (vlc.State.NothingSpecial, vlc.State.Stopped):
            self.play()

    def stop_music(self) -> None:
        if not self.media_player:
            print("No media player found.")
            return

        print("stopping music...")
        self.media_player.stop()

    def remove_music(self) -> None:
        if self.playlist.is_empty():
            print("Playlist is empty.")
            return

        remove_command(self.playlist.get_tracks_in_string())
        track_number = input("Enter track number: ")

        if not track_number.isdigit():
            print("Track number is not number.")
            return

        if not is_valid_track_number(int(track_number), len(self.playlist.playlist)):
            print("Please type valid track number.")
            return

        self.playlist.remove_track(int(track_number) - 1)

    def next_music(self) -> None:
        if self.state is not vlc.State.NothingSpecial:
            self.stop_music()
        self.play()

    def pause_music(self) -> None:
        if not self.media_player:
            print("No media player found.")
            return

        print("pausing music...")
        self.media_player.pause()

    def play_music(self) -> None:
        if not self.media_player:
            print("No media player found.")
            return

        if self.state == vlc.State.Paused:
            print("playing/resuming music...")
            self.media_player.play()
