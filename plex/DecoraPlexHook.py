import os

from leviton import LevitonDecora
from .PlexHook import PlexHook


class DecoraPlexHook(PlexHook):

    def __init__(self):
        super().__init__()
        activities = (
            'PLEX_CLIP_ACTIVITY',
            'PLEX_END_ACTIVITY',
            'PLEX_PLAY_ACTIVITY',
            'PLEX_PAUSE_ACTIVITY',
            'PLEX_STOP_ACTIVITY'
        )
        self.activity = False
        self.switch = os.environ.get('DECORA_SWITCH')
        self.decora_api = LevitonDecora(decora_email=os.environ.get('DECORA_USER'),
                                        decora_pass=os.environ.get('DECORA_PASS'),
                                        decora_residence=os.environ.get('DECORA_RESIDENCE'))

        # Check if any activity variable is defined
        for activity in activities:
            if os.environ.get(activity, None):
                self.activity = True
                break

    def run_activity(self, activity, brightness=0):
        if self.activity:
            self.decora_api.run_activity(activity)
        else:
            self.decora_api.control_switch(self.switch, brightness=brightness)
        self.decora_api.log_out()

    def clip_action(self):
        self.run_activity(os.environ.get('PLEX_CLIP_ACTIVITY'), int(os.environ.get('PLEX_CLIP_BRIGHTNESS')))

    def end_action(self):
        self.run_activity(os.environ.get('PLEX_END_ACTIVITY'), int(os.environ.get('PLEX_END_BRIGHTNESS')))

    def play_action(self):
        self.run_activity(os.environ.get('PLEX_PLAY_ACTIVITY'), int(os.environ.get('PLEX_PLAY_BRIGHTNESS')))

    def pause_action(self):
        self.run_activity(os.environ.get('PLEX_PAUSE_ACTIVITY'), int(os.environ.get('PLEX_PAUSE_BRIGHTNESS')))

    def stop_action(self):
        self.run_activity(os.environ.get('PLEX_STOP_ACTIVITY'), int(os.environ.get('PLEX_STOP_BRIGHTNESS')))
