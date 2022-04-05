import aiohttp_jinja2
from aiohttp import web
import aiohttp


@aiohttp_jinja2.template('index.html')
async def index(request):
    return


async def chat(request):
    ws = web.WebSocketResponse()

    await ws.prepare(request)

    async for message in ws:
        if message.type == aiohttp.WSMsgType.TEXT:
            print(message.data) 
            if message.data == 'EXIT':
                await ws.close()
            elif message.type == aiohttp.WSMsgType.ERROR:
                print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws