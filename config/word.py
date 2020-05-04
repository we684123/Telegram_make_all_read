# 這裡要可以同時設定 命令 和 語言 但目前沒效果
def text():
    return {  # 說明、屬助姓文字
        "help": {
            "zh-tw": f"使用方法如下{0}",
            "en": "how to use this bot"
        },
        "pong": {
            "zh-tw": "!pong",
            "en": "!pong"
        },
        "allread_ing":{
            "zh-tw": "全已讀ing...",
            "en": "all read ing..."
        },
        "allread_ed":{
            "zh-tw": "已全已讀!",
            "en": "all read success"
        },
        "allread_igron_white_ing":{
            "zh-tw": "全已讀(忽略白名單)ing...",
            "en": "all read(igron white) ing..."
        },
        "allread_igron_white_ed":{
            "zh-tw": "已全已讀(忽略白名單)!",
            "en": "all read(igron white) success"
        },
        "stop": {
            "zh-tw": "已終止bot!",
            "en": "bot stop!"
        },
        "add_white_ed": {
            "zh-tw": "成功加入白名單",
            "en": "add to white success"
        },
        "add_white_fail": {
            "zh-tw": "加入白名單失敗",
            "en": "add to white fail"
        },
        "rm_white_ed": {
            "zh-tw": "成功移除白名單",
            "en": "remove from white success"
        },
        "rm_white_fail": {
            "zh-tw": "移除白名單失敗",
            "en": "remove from white fail"
        },
        "list_white": { # 這個會被陣列包覆! [list_white,list_white...]
            "zh-tw": "{0} - https://t.me/c/{1}/1\n", #{0}=名稱 #{1}=id
            "en": "{0} - https://t.me/c/{1}/1\n", #{0}=name #{1}=id
        },
        "white_is_empty": {
            "zh-tw": "白名單內沒有群組",
            "en": "white is empty"
        },
        "assemble_name":{
            "zh-tw": "{1}{0}", #{0} = first_name ,#{1} = last_name
            "en": "{1}{0}"
        }

    }
