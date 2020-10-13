from aiohttp import web
import os

async def post(request):
    print(request.transport.get_extra_info('peername'))
    return web.Response(text='')

app = web.Application()
app.add_routes([web.post('/', post)])
web.run_app(app, port=os.getenv('PORT'))
