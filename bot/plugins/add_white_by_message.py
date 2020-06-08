import asyncio
from telethon import events

from bot.functions import white_list


def run(client, logger, lg, ct, cw):
    my_entity = client.get_me()
    logger.debug(ct['add_white_by_message'])
    logger.debug(ct['add_white_by_message']['pattern_str'])

    @client.on(events.NewMessage(
        outgoing=True,
        chats=my_entity,
        from_users=my_entity,
        pattern=ct['add_white_by_message']['pattern_str']
    ))
    async def handler(event):
        logger.info(event)
        logger.debug(ct['add_white_by_message'])

        try:
            reply_to_msg_id = event.reply_to_msg_id
            logger.debug(f'reply_to_msg_id = {reply_to_msg_id}')
            message_by_id = await client.get_messages(my_entity, ids=reply_to_msg_id)
            logger.debug(f'message_by_id = {message_by_id}')
            saved_from_peer = message_by_id.fwd_from.saved_from_peer
            logger.debug(f'saved_from_peer = {saved_from_peer}')

            # 先偵測
            amis_type = ""
            try:
                amis_id = message_by_id.fwd_from.user_id
                amis_type = "PeerUser"
            except Exception as e:
                logger.debug(e)
            try:
                amis_id = message_by_id.fwd_from.chat_id
                amis_type = "PeerChat"
            except Exception as e:
                logger.debug(e)
            try:
                amis_id = message_by_id.fwd_from.channel_id
                amis_type = "PeerChannel"
            except Exception as e:
                logger.debug(e)
            logger.debug(f"amis_type = {amis_type}")

            aims_entity = aims_entity = await client.get_entity(saved_from_peer)
            logger.debug(f'aims_entity == {aims_entity}')


            if amis_type == "PeerUser":
                logger.debug('amis_type == "PeerUser"')
                name = cw['assemble_name'][lg].format(
                    aims_entity.first_name, aims_entity.last_name)
            elif amis_type == "PeerChat":
                logger.debug('amis_type == "PeerChat"')
                name = aims_entity.title
            elif amis_type == "PeerChannel":
                logger.debug('amis_type == "PeerChannel"')
                name = aims_entity.title
            else:
                raise('amis_type is not allow')


            amis_peer_id = await client.get_peer_id(aims_entity)
            logger.debug(f'amis_peer_id = {amis_peer_id}')

            try:
                logger.debug(
                    f"amis_id = {amis_id},amis_peer_id = {amis_peer_id},name = {name}")
                white_list.add_to_white(amis_id, amis_peer_id, name)
                logger.info(f"white_list.add_to_white({amis_id}, {name}) ed")
            except Exception as e:
                logger.error(e)

            m = await event.respond(cw['add_white_ed'][lg])
            await asyncio.sleep(ct['add_white']['second'])
            await client.delete_messages(event.chat_id, [event.id, m.id])
        except Exception as e:
            logger.error('add_white_by_message error')
            logger.error(e)
            await event.reply('add_white_by_message error')
            await event.reply(e)
