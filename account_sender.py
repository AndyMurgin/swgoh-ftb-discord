import requests

from urls import UrlMaker


class OwnerAccountSender:
    def __init__(self, authorization_token):
        self.authorization_token = authorization_token

    def send_message(self, channel_id, message):
        payload = {"content": message}

        headers = {"authorization": self.authorization_token}

        requests.post(
            UrlMaker.post_message_url(channel_id), data=payload, headers=headers
        )

    def command(self):
        payload = {
            "type": 2,
            "application_id": 752366060312723546,
            "channel_id": 1144745341514698845,
            "guild_id": 1144745341514698842,
            "session_id": "71910d296e31bf85e00502980d04a295",
            "data": {
                "version": 1135049866154885207,
                "id": 1135049865307635792,
                "name": "tb",
                "type": 1,
                "options": [{"type": 1, "name": "status", "options": []}],
            },
        }

        headers = {"authorization": self.authorization_token}

        response = requests.post(
            UrlMaker.post_command_url(), json=payload, headers=headers
        )
        if not response.ok:
            print(response.json())
        else:
            print("Command has been sent")
