import asyncio
from telethon import events

from bot.functions import white_list


def run(client, logger, lg, ct, cw):
    my_entity = client.get_me()

    @client.on(events.NewMessage(
        outgoing=True,
        chats=my_entity,
        pattern=ct['list_white']['pattern_str']
    ))
    async def handler(event):
        logger.info(event)
        logger.debug(ct['list_white'])
        try:
            txt = ""
            white_list_all = white_list.list_all()
            logger.debug("white_list_all = ")
            logger.debug(white_list_all)
            # white_list_all == [{'id': 207, 'name': "逆流"}, ...]
            if white_list_all == []:
                m = await event.respond(cw['white_is_empty'][lg])
            else:
                for i in white_list_all:
                    txt += cw['list_white'][lg].format(i['name'], i['id'])
                # m = await event.respond(txt)
                logger.debug(txt)
                m = await client.send_message('me', txt, parse_mode='md')

            if ct['list_white']['auto_delete']:
                await asyncio.sleep(ct['list_white']['second'])
                await client.delete_messages(event.chat_id, [event.id, m.id])
        except Exception as e:
            logger.error(e)
            await event.respond(e)
