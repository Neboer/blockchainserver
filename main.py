from sanic import Sanic
from sanic.response import json
from database import getDataBase
from read_config import get_config
from datetime import datetime

app = Sanic()


@app.route("/")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    config = get_config()
    dataBase, userTable, recordTable = getDataBase(config["mysql"])  # 这里我觉得record似乎更合适
    dataBase.connect()
    # dataBase.create_tables([userTable,recordTable])
    # userTable.create(device_id='123345', username='Jawa', password="what_*s_t*e_b**t_language_in_t*e_world")
    # recordTable.create(device_id='1234', create_time=datetime.now(), data_content="sdfasdasd" ,hash = "?")

    db_settings = {
        "database": recordTable  # 这里我感觉似乎没啥用，就先不动了
    }
    app.config.update(db_settings)
    app.run(host="0.0.0.0", port=8000)
