class UrlMaker:
    @staticmethod
    def post_message_url(channel_id):
        return f"https://discord.com/api/v9/channels/{channel_id}/messages"

    @staticmethod
    def post_command_url():
        return "https://discord.com/api/v9/interactions"
