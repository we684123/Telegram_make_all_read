import asyncio
from telethon import events

from bot.functions import white_list


def run(client, logger, lg, ct, cw):
    my_entity = client.get_me()
    logger.debug(ct['rm_white'])
    logger.debug(ct['rm_white']['re_str'])

    @client.on(events.NewMessage(
        outgoing=True,
        chats=my_entity,
        blacklist_chats=True,
        pattern=ct['rm_white']['re_str']
    ))
    async def handler(event):
        logger.info(event)
        logger.debug(ct['rm_white'])
        logger.debug(event.message.to_id)

        try:
            # 先偵測
            amis_type = ""
            try:
                amis_id = event.message.to_id.user_id
                amis_type = "PeerUser"
            except Exception as e:
                pass
            try:
                amis_id = event.message.to_id.chat_id
                amis_type = "PeerChat"
            except Exception as e:
                pass
            try:
                amis_id = event.message.to_id.channel_id
                amis_type = "PeerChannel"
            except Exception as e:
                pass

            # 再分流
            if amis_type == "PeerUser":
                amis_id = event.message.to_id.user_id
            elif amis_type == "PeerChat":
                amis_id = event.message.to_id.chat_id
            elif amis_type == "PeerChannel":
                amis_id = event.message.to_id.channel_id
            else:
                raise('amis_type is not allow')

            try:
                logger.debug("by rm_white, amis_id = {amis_id}")
                white_list.rm_from_white(amis_id)
                logger.info("white_list.rm_from_white({amis_id}) ed")
            except Exception as e:
                logger.error(e)

            m = await event.respond(cw['rm_white_ed'][lg])
            await asyncio.sleep(5)
            await client.delete_messages(event.chat_id, [event.id, m.id])
        except Exception as e:
            logger.error(e)
            await event.respond(cw['rm_white_fail'][lg])
