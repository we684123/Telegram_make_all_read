import asyncio
from telethon import events


def run(client, logger, lg, ct, cw):
    my_entity = client.get_me()

    @client.on(events.NewMessage(
        outgoing=True,
        chats=my_entity,
        pattern=ct['ping']['re_str']
    ))
    async def handler(event):
        logger.info(event)
        logger.debug(ct['ping'])
        logger.debug(cw['pong'][lg])
        m = await event.respond(cw['pong'][lg])
        if ct['ping']['auto_delete']:
            await asyncio.sleep(ct['ping']['second'])
            await client.delete_messages(event.chat_id, [event.id, m.id])
