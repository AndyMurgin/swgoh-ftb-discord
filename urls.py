class UrlMaker:
    def post_message_url(channel_id):
        return f"https://discord.com/api/v9/channels/{channel_id}/messages"

    def post_command_url():
        return "https://discord.com/api/v9/interactions"
