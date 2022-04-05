import json
import aiohttp_jinja2
from aiohttp import web
import aiohttp


@aiohttp_jinja2.template('index.html')
async def index(request):
    return


async def chat(request):
    ws = web.WebSocketResponse()

    await ws.prepare(request)

    all_ws = request.app.get('WEBSOCKETS')
    all_ws.add(ws)

    async for message in ws:
        if message.type == aiohttp.WSMsgType.TEXT:
            message_json = json.loads(message.data)

            if message_json['TYPE'] == 'EXIT':
                await ws.close()
            elif message_json['TYPE'] == 'CONNECTION':

                response = {'USERNAME': message_json['USERNAME'],
                            'MESSAGE': 'CONNECTED'}
                for recipient in all_ws:
                    if recipient != ws:
                        await recipient.send_json(response)

        elif message.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                ws.exception())

    all_ws.discard(ws)
    return ws