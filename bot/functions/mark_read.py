import asyncio
async def aims_read(client, aims_entity, allowed_types):
    '''
    client = client
    aims_entity = entity or [entity]
    會已讀所有"實體"
    如果有傳入的參數中有不應許的 type，則不會已讀
    allowed_types = [
        "<class 'telethon.tl.types.Chat'>",
        "<class 'telethon.tl.types.User'>",
        "<class 'telethon.tl.types.Channel'>"
    ]
    output = True or False
    '''

    # 檢查型態
    # allowed_types = [
    #     "<class 'telethon.tl.types.Chat'>",
    #     "<class 'telethon.tl.types.User'>",
    #     "<class 'telethon.tl.types.Channel'>"
    # ]
    # print(type(aims_entity))
    if type(aims_entity) != list:  # 先強制變list方便檢查和後續作業
        # print("aims_entity = [aims_entity]")
        aims_entity = [aims_entity]
        # print(type(aims_entity))
    for entity in aims_entity:
        if not (str(type(entity)) in allowed_types):
            j=str(type(entity))
            j2 = f'{j} is not allowed type'
            print(f'{j2} is not allowed type')
            raise(j2)

    # 開始已讀
    try:
        for entity in aims_entity:
            await client.send_read_acknowledge(entity)
    except Exception as e:
        return e

    return True
