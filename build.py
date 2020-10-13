from aiohttp import web

app = web.Application()
app.add_routes([web.post('/ajax', post)])
web.run_app(app, port=os.getenv('PORT'))
