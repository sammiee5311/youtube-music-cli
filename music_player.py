import time

import vlc

from config.track import Track


class MusicPlayer:
    def __init__(self):
        self.instance = vlc.Instance("--verbose 0")
        self.player = self.instance.media_player_new()
        self.current_music = None

    def play(self, url: str):
        media = self.instance.media_new(url)
        media.get_mrl()
        self.player.set_media(media)
        self.player.play()

        time.sleep(5)
        event_manager = self.player.event_manager()
        event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.end_callback)

    def youtube_player(self, track: Track):
        self.play(track.audio_url)

    def end_callback(self, event):
        self.youtube_player()

    def next_song(self):
        self.youtube_player()

    def set_vlc_volume(self, level):
        self.player.audio_set_volume(level)

    def get_vlc_volume(self):
        return self.player.audio_get_volume()

    def mute_vlc(self, status=True):
        return self.player.audio_set_mute(status)

    def stop_vlc(self):
        print("stopping vlc")
        self.player.stop()

    def pause_vlc(self):
        print("pausing vlc")
        self.player.pause()

    def play_vlc(self):
        if self.player.get_state() == vlc.State.Paused:
            print("playing/resuming vlc")
            self.player.play()

    def is_vlc_playing(self):
        return self.player.is_playing()

    def state(self):
        return self.player.get_state()
