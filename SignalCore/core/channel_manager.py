from core.channel_stats import ChannelStats

_channels = {}


def get_channel(event):

    cid = event.chat_id

    if cid not in _channels:

        name = ""

        if event.chat:
            name = getattr(event.chat, "title", "") or ""

        _channels[cid] = ChannelStats(
            channel_id=cid,
            channel_name=name
        )

    return _channels[cid]