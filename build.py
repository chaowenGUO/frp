import aiohttp, asyncio, io, tarfile, pathlib
async def f():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://github.com/fatedier/frp/releases/download/v0.34.1/frp_0.34.1_linux_amd64.tar.gz') as response:
            with io.BytesIO(await response.content.read()) as _:
                def f(tar):
                    for _ in tar.getmembers():
                        if pathlib.Path(_.name).name == 'frps':
                            _.name = 'frps'
                            yield _
                with tarfile.open(mode='r:gz', fileobj=_) as tar: tar.extractall(members=f(tar))
    
asyncio.run(f())
