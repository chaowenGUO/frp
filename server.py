from aiohttp import web
import os

async def post(request):
    print(request.host)
    return web.Response(text='fuck you')

app = web.Application()
app.add_routes([web.post('/ajax', post)])
web.run_app(app, port=os.getenv('PORT'))
