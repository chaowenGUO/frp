import aiohttp, asyncio, io, tarfile, pathlib, fileinput
async def f():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://github.com/fatedier/frp/releases/download/v0.34.3/frp_0.34.3_linux_amd64.tar.gz') as response:
            with io.BytesIO(await response.content.read()) as _:
                def f(tar):
                    for _ in tar.getmembers():
                        parts = pathlib.Path(_.name).parts 
                        if len(parts) > 2 and parts[1] == 'boost':
                            _.name = '/'.join(('include', *itertools.islice(parts, 1, None)))
                            yield _
                with tarfile.open(mode='r:gz', fileobj=_) as tar: tar.extractall(members=f(tar))
asyncio.run(f())
