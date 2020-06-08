def command():
    # 目前用這個方式看看，如果要換其他方式的話，這裡也算是做好了分層
    return {  # 放命令類別 #用正則表達式! # use re format
        "ping": {  # <-這個別改 給程式識別用
            "pattern_str": "^ping$", # <-如果不懂請 google "正則表達示"
            # 推薦這個影片 https://www.youtube.com/watch?v=rCd8zdnWMgk
            "auto_delete": True, # <-要不要刪掉這則樳 True or False
            "second": 5, # <- 延遲刪除的時間，只能 >=0
        },
        "stop": {
            "pattern_str": "^stop$",
            # 這個沒有自動刪，因為不可能。
        },
        "allread": {
            # !allowed or !ar
            "pattern_str": "^(allread|ar)$",
            "auto_delete": True,
            "second": 5,
        },
        "add_white": {
            "pattern_str": "^add_white|aw$",
            "auto_delete": True,
            "second": 5,
        },
        "add_white_by_message": {
            "pattern_str": "^add_white_by_message|awbi$",
            "auto_delete": True,
            "second": 5,
        },
        "rm_white": {
            "pattern_str": "^rm_white|rw$",
            "auto_delete": True,
            "second": 5,
        },
        "list_white": {
            "pattern_str": "^list_white|lw$",
            "auto_delete": False,
            "second": 5,
        },
        "allread_igron_white": {
            # !allowed or !ar
            "pattern_str": "^allread_igron_white|ariw)$",
            "auto_delete": True,
            "second": 5,
        },
    }
