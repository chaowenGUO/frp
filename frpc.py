import aiohttp, asyncio, io, tarfile, pathlib, fileinput
async def f():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://github.com/fatedier/frp/releases/download/v0.34.3/frp_0.34.3_linux_amd64.tar.gz') as response:
            with io.BytesIO(await response.content.read()) as _:
                with tarfile.open(mode='r:gz', fileobj=_) as tar: 
                    tar.extract('frp_0.34.3_linux_amd64/systemd/frpc.service', '/lib/systemd/system')
                    tar.extract('frp_0.34.3_linux_amd64/frpc', '/usr/bin')
        pathlib.Path('/etc/frp/frpc.ini').write_text(
asyncio.run(f())
