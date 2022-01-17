import time
from dataclasses import dataclass
from typing import Optional

import vlc
from youtube_music import YoutubeMusic

from utils.playlist import Playlist
from utils.track import Track


@dataclass
class Player:
    playlist: Playlist
    youtube_music_search: YoutubeMusic
    media_player: Optional[vlc.MediaPlayer] = None
    instance: Optional[vlc.Instance] = None
    current_track: Optional[Track] = None

    @property
    def state(self) -> vlc.State:
        return self.media_player.get_state()

    def create_new_player(self) -> None:
        self.instance = vlc.Instance("--verbose 0")
        self.media_player = self.instance.media_player_new()

    def play(self):
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

    def end_callback(self, event):
        self.play()

    def add_music(self, name: str) -> None:
        track = self.youtube_music_search.search_and_get_track(name)
        self.playlist.add_track_in_playlist(track)

        if self.state in (vlc.State.NothingSpecial, vlc.State.Stopped):
            self.play()

    def stop_music(self) -> None:
        print("stopping music...")
        self.media_player.stop()

    def next_music(self) -> None:
        if self.state is not vlc.State.NothingSpecial:
            self.stop_music()
        self.play()

    def pause_music(self) -> None:
        print("pausing music...")
        self.media_player.pause()

    def play_music(self) -> None:
        if self.state is vlc.State.Paused:
            print("playing/resuming music...")
            self.media_player.play()
