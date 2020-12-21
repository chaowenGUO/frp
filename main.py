from aiohttp import web

async def post(request):
    return web.Response(text='fuck you')

app = web.Application()
app.add_routes([web.get('/', post)])
web.run_app(app)
