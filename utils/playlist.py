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

    def play_next_track(self) -> Track:
        if len(self.playlist) == 0:
            raise PlaylistIsEmpty
        self.current_track = self.playlist.popleft()

        return self.current_track

    def is_empty(self) -> bool:
        return len(self.playlist) == 0
