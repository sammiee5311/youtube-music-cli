from dataclasses import dataclass


@dataclass
class Track:
    video_title: str
    video_id: str
    video_url: str
    audio_url: str
