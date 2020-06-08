def base():
    return {
        "api_id": "123456",
        "api_hash": "123xxx",
        "logging_level": "DEBUG", #DEBUG #INFO #ERROR
        "log_file_path": './data/logs/tmar',
        "log_format": '%(asctime)s - %(levelname)s : %(message)s',
        "db_path": './data/data.db',
        "plugins_path": 'bot/plugins',
        "Language":"zh-tw", # or "en"
    }
