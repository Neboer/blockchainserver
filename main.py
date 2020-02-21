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
    dataBase, dataTable = getDataBase(config["mysql"])
    dataBase.connect()
    # dataBase.create_tables([dataTable])
    dataTable.create(device_id='12345', create_time=datetime.now(), data_content="sdfasdasd")

    db_settings = {
        "database": dataTable
    }
    app.config.update(db_settings)
    app.run(host="0.0.0.0", port=8000)
