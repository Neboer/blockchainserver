from sanic import Sanic, response
from sanic_openapi import swagger_blueprint, doc
from models.user import User

from conn.connection import connect
from sanic.log import logger
from sanic.response import text

app = Sanic(name='blockChainServer')
app.blueprint(swagger_blueprint)


@app.route("/")
async def test(request):
    return response.json({"hello": "world"})


@app.route('/api/login', methods=['POST'])
@doc.description('登录接口，所需参数有username,password')
@doc.consumes(doc.JsonBody(
    {
        "device_id": doc.String("456"),
        "password": doc.String("123"),
    }
),
    location="body",
)
@doc.response(400,{"msg": str}, description="帐号密码输错了")
@doc.response(500,{'msg': str},description="程序出错，找后端查看日志")
async def test(request):
    try:
        device_id = request.json['device_id']
        print(device_id)
        login_user = User(device_id)
        if request.json['password'] != login_user.user_password:
            return response.json({'msg': '帐号不存在或密码错误'}, status=400)
        else:
            return response.json({'username': login_user.user_name, 'password': login_user.user_password})
    except Exception as e:
        print(e)
        return response.json({'msg': '服务器错误'}, status=500)


if __name__ == "__main__":
    app.run(debug=True, access_log=True)
