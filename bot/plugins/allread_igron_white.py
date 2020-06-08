import asyncio
import logging.handlers
from telethon import events

from bot.functions import mark_read, white_list


def run(client, logger, lg, ct, cw):
    my_entity = client.get_me()

    @client.on(events.NewMessage(
        outgoing=True,
        chats=my_entity,
        from_users=my_entity,
        pattern=ct['allread_igron_white']['pattern_str']
    ))
    async def handler(event):
        logger.info(event)
        logger.debug(ct['allread_igron_white'])
        m = await event.reply(cw['allread_igron_white_ing'][lg])
        logger.debug(m)
        # 先排除沒有新的訊息的，並把需要已讀的對象加到 unread_count_dialog
        unread_count_dialog = []
        dialogs = await client.get_dialogs()
        # logger.debug(dialogs)

        w_list_id = []
        for i in white_list.list_all():
            w_list_id.append(i["amis_peer_id"])
        logger.debug("w_list_id ==")
        logger.debug(w_list_id)

        for dialog in dialogs:
            if dialog.unread_count != 0:  # 有新訊息，可能需要已讀
                # 這裡過濾白名單
                logger.debug("dialog.id in w_list_id")
                logger.debug(str(dialog.id))
                logger.debug(str(dialog.id) in w_list_id)
                if str(dialog.id) in w_list_id:
                    logger.debug("continue！！！")
                    continue

                logger.debug(dialog)
                ucd = await client.get_entity(dialog.entity)
                unread_count_dialog.append(ucd)
        logger.debug(f"unread_count_dialog = \n{unread_count_dialog}")

        if unread_count_dialog == []:  # 如果不需要就早點結束
            await event.reply(cw['allread_igron_white_ed'][lg])
            await client.delete_messages(event.chat_id, [m.id])
            return True  # <-目前沒有意義，隨便回傳，能中斷就好

        allowed_types = [
            "<class 'telethon.tl.types.Chat'>",
            "<class 'telethon.tl.types.User'>",
            "<class 'telethon.tl.types.Channel'>"
        ]
        try:
            logger.debug(">>> unread_count_dialog == ")
            logger.debug(unread_count_dialog)
            task = asyncio.create_task(
                mark_read.aims_read(client, unread_count_dialog, allowed_types)
            )
            await task
            # "zh-tw": "已全已讀!"
            await client.delete_messages(my_entity, m.id)
            await event.reply(cw['allread_igron_white_ed'][lg])
        except Exception as e:
            logger.error('by mark_read.aims_read(...)')
            logger.error(e)
