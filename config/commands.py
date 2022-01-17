from typing import Protocol


class MusicPlayer(Protocol):
    def __init__(self, recv):
        ...

    def execute(self):
        ...


class AddTrack:
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        self.recv.add_track_in_playlist()
