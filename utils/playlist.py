from dataclasses import dataclass, field
from typing import Deque, Optional

from utils.track import Track


class PlaylistIsEmpty(Exception):
    def __init__(self, message="Playlist is Empty"):
        super().__init__(message)


@dataclass
class Playlist:
    current_track: Optional[Track] = None
    playlist: Deque[Track] = field(default_factory=Deque)

    def add_track_in_playlist(self, track: Track) -> None:
        self.playlist.append(track)

    def get_tracks_in_string(self) -> str:
        tracks_string = f"[C] {self.current_track.video_title}\n"
        for i, track in enumerate(self.playlist):
            tracks_string += f"[{i+1}] {track.video_title}\n"

        return tracks_string[:-1]

    def play_next_track(self) -> Track:
        if len(self.playlist) == 0:
            raise PlaylistIsEmpty
        self.current_track = self.playlist.popleft()

        return self.current_track

    def remove_track(self, track_number) -> None:
        track = self.playlist[track_number]
        del self.playlist[track_number]
        print(f"{track.video_title} is removed.")

    def is_empty(self) -> bool:
        return len(self.playlist) == 0
