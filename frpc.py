import aiohttp, asyncio, io, tarfile, pathlib, fileinput
async def f():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://github.com/fatedier/frp/releases/download/v0.34.3/frp_0.34.3_linux_amd64.tar.gz') as response:
            with io.BytesIO(await response.content.read()) as _:
                def f(tar):
                    for _ in tar.infolist():
                        if _.filename.endswith('chat/index.html'):
                            _.filename = 'chat.html'
                            yield _
                        elif _.filename.endswith('chat/index.js'):
                            _.filename = 'chat.js'
                            yield _
                        else:
                            path = pathlib.Path(_.filename)
                            if path.suffix == '.html' or path.suffix == '.js' or path.suffix == '.sql':
                                _.filename = path.name
                                yield _
                with zipfile.ZipFile(_) as tar: tar.extractall(members=f(tar))
asyncio.run(f())
with fileinput.FileInput('chat.html', inplace=True) as file:
    for line in file:
        print(line.replace('index.js', 'chat.js'), end='')
