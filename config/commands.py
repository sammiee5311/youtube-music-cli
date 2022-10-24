from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from utils.playlist import Playlist


class MusicPlayer(Protocol):
    def __init__(self, recv: Playlist):
        ...

    def execute(self) -> None:
        ...


class AddTrack:
    def __init__(self, recv: Playlist):
        self.recv = recv

    def execute(self) -> None:
        self.recv.add_track_in_playlist()
