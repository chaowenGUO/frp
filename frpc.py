import aiohttp, asyncio, io, tarfile, pathlib

async def f():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://github.com/fatedier/frp/releases/download/v0.34.3/frp_0.34.3_linux_amd64.tar.gz') as response:
            with io.BytesIO(await response.content.read()) as _:
                with tarfile.open(mode='r:gz', fileobj=_) as tar:
                    for _ in tar: _.name = pathlib.Path(_.name).name
                    tar.extract('frpc.service', '/lib/systemd/system')
                    tar.extract('frpc', '/usr/bin')
    pathlib.Path('/etc/frp').mkdir()
    pathlib.Path('/etc/frp/frpc.ini').write_text('''[common]
server_addr = [2a02:180:6:1::3142]
[web]
type = tcp
local_port = 8080
remote_port = 9000''')
    await asyncio.create_subprocess_exec('systemctl', 'daemon-reload')
    await asyncio.create_subprocess_exec('systemctl', 'enable', 'frpc') 
    await asyncio.create_subprocess_exec('systemctl', 'restart', 'frpc')
    
asyncio.run(f())
