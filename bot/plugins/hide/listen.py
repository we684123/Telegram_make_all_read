import asyncio
from telethon import events


def run(client, logger, lg, ct, cw):
    my_entity = client.get_me()

    @client.on(events.NewMessage(
        chats=my_entity,
    ))
    async def handler(event):
        logger.debug(event)
