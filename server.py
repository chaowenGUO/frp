from aiohttp import web
import os

async def post(request):
    return web.Response(text=str(request.forwarded))

app = web.Application()
app.add_routes([web.post('/', post)])
web.run_app(app, port=os.getenv('PORT'))
