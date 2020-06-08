import asyncio
from telethon import events

from bot.functions import white_list


def run(client, logger, lg, ct, cw):
    my_entity = client.get_me()
    logger.debug(ct['add_white'])
    logger.debug(ct['add_white']['pattern_str'])

    @client.on(events.NewMessage(
        outgoing=True,
        chats=my_entity,
        blacklist_chats=True,
        pattern=ct['add_white']['pattern_str']
    ))
    async def handler(event):
        logger.info(event)
        logger.debug(ct['add_white'])
        logger.debug(event.message.to_id)

        try:
            # 先偵測
            amis_type = ""
            try:
                amis_id = event.message.to_id.user_id
                amis_type = "PeerUser"
            except Exception as e:
                logger.debug(e)
            try:
                amis_id = event.message.to_id.chat_id
                amis_type = "PeerChat"
            except Exception as e:
                logger.debug(e)
            try:
                amis_id = event.message.to_id.channel_id
                amis_type = "PeerChannel"
            except Exception as e:
                logger.debug(e)
            logger.debug("amis_type = {amis_type}")

            try:
                # 再分流
                if amis_type == "PeerUser":
                    logger.debug('amis_type == "PeerUser"')
                    amis_id = event.message.to_id.user_id
                    aims_entity = await client.get_entity(amis_id)
                    name = cw['assemble_name'][lg].format(
                        aims_entity.first_name, aims_entity.last_name)
                elif amis_type == "PeerChat":
                    logger.debug('amis_type == "PeerChat"')
                    amis_id = event.message.to_id.chat_id
                    aims_entity = await client.get_entity(amis_id)
                    name = aims_entity.title
                elif amis_type == "PeerChannel":
                    logger.debug('amis_type == "PeerChannel"')
                    amis_id = event.message.to_id.channel_id
                    aims_entity = await client.get_entity(amis_id)
                    name = aims_entity.title
                else:
                    raise('amis_type is not allow')
                logger.debug(f'name == {name}')
                amis_peer_id = await client.get_peer_id(aims_entity)
                logger.debug('amis_id = client.get_peer_id(aims_entity)')
                logger.debug(amis_peer_id)
            except Exception as e:
                logger.error('by amis_type == "XXX"')
                logger.error(e)
                raise e

            try:
                logger.debug(f"amis_id = {amis_id},name = {name}")
                white_list.add_to_white(amis_id, amis_peer_id, name)
                logger.info(f"white_list.add_to_white({amis_id}, {name}) ed")
            except Exception as e:
                logger.error(e)

            m = await event.respond(cw['add_white_ed'][lg])
            await asyncio.sleep(ct['add_white']['second'])
            await client.delete_messages(event.chat_id, [event.id, m.id])
        except Exception as e:
            logger.error(e)
            await event.respond(cw['add_white_fail'][lg])
