import asyncio
from telethon import events


def run(client, logger, lg, ct, cw):
    my_entity = client.get_me()
    @client.on(events.NewMessage(
        outgoing=True,
        chats=my_entity,
        from_users=my_entity,
        pattern=ct['stop']['pattern_str']
    ))
    async def handler(event):
        logger.info(event)
        logger.debug(ct['stop'])
        await event.reply(cw['stop'][lg])
        try:
            await client.disconnect()
            logger.info("client disconnect!")
        except Exception as e:
            logger.error("client disconnect error")
            logger.error(e)
