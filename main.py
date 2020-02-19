from sanic import Sanic
from sanic.response import json
from database import init_table, data_record_table
from read_config import get_config

app = Sanic()


@app.route("/")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    config = get_config()
    table = init_table(config["mysql"])

    app.run(host="0.0.0.0", port=8000)
