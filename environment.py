from configs import PropertiesHolder


class Environment:
    __settings = {}

    def is_notag_mode(self, channel_id: int):
        notag = self.__settings.get("notag")
        channel_notag = notag.get(channel_id) if notag is not None else None
        return (
            channel_notag
            if channel_notag is not None
            else PropertiesHolder.get_default_notag_mode()
        )

    def update_notag_mode(self, channel_id: int, value: bool):
        self.__settings.update({"notag": {channel_id: value}})


ENV = Environment()
