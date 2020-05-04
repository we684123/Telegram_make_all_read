# Telegram_make_all_read
一個可以全已讀 Telegram 訊息的東東。
對不起了肝肝 但我真的需要這個酷功能QQ

Can make Telegram all as read.
sorry to my liver, but i need this method. QQ

----

# 注意事項
目前docker-compose化、新功能、... 我決定搞定期中考後再說
然後 "頻道加入白名單" 的部分也是下次再加入

----

# 使用方式

## 示範
點下面的 GIF 可至 youtube 觀看。
[![示範的GIF(YT)](https://github.com/we684123/Telegram_make_all_read/blob/master/%E5%9C%96%E5%BA%8A/out.gif?raw=true)](https://www.youtube.com/watch?v=4Lj9fFYYqj4)

## 指令
 - ```!allread``` or ```!ar```
 全部對話標示為已讀
 (make all read)
 僅在"[儲存的訊息](https://imgur.com/1ET9ThI)" 內有效
 (only in "Save Messages" is can be use)
 ![儲存的訊息](https://imgur.com/1ET9ThI.png)

 - ```!stop```
 強制停止程式
 (force stop program)
 僅在"[儲存的訊息](https://imgur.com/1ET9ThI)" 內有效
 (only in **"Save Messages"** is can be use)

 - ```!add_white``` or ```!aw```
 加入白名單
 (add to white list)
 僅在 **個人、群組、超級群組** 有效
 (only in **user、group、supergroup** is can be use)

 - ```!rm_white``` or ```!rw```
 移除白名單
 (remove from white list)
 僅在 **個人、群組、超級群組** 有效
 (only in **user、group、supergroup** is can be use)

 - ```!list_white``` or ```!lw```
 列出白名單
 (print white list)
 僅在"[儲存的訊息](https://imgur.com/1ET9ThI)" 內有效
 (only in **"Save Messages"** is can be use)

 - ```!allread_igron_white``` or ```!ariw```
 全部對話(忽略白名單)標示為已讀
 (make all read, but if in white list br not)
 (only in **"Save Messages"** is can be use)
 僅在"[儲存的訊息](https://imgur.com/1ET9ThI)" 內有效




----
# 如何部屬(安裝?)

  1. 登入 [telegram](https://my.telegram.org/auth)
  2. 點 API development tools，並申請一個應用程式
  3. 拿到你的 'App api_id'、'App api_hash'(對了 這個能申請一次)
  4. 進到 cinfig/base.py 把步驟三的東西貼上
  5. (可選 Optional)看看要不要修改 cinfig/base.py 中的 Language
  (目前只有"zh-tw" 和 "en"，如果要新增的話要自己去 cinfig/word.py 按照格式新增)
  6. (可選 Optional)看不要修改 cinfig/command.py 中的指令
  7. 執行 ```pip install -r requirements.txt``` 跟 ```python main.py```
  8. 按照指示輸入手機(台灣的記得最前面+886 然後09的0不用 直接+8869xxx)
  9. 去 telegram 上收驗證碼後登入
  10. 沒了 就享受這功能吧~~~

----
