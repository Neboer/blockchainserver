from sanic import Sanic
from sanic.response import json
from conn.connection import connect

app = Sanic()


@app.route("/")
async def test(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    db = connect()
    cursor = db.cursor()
    sql = "select * from users;"
    cursor.execute(sql)
    res = cursor.fetchone()
    print(res)