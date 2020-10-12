import aiohttp, asyncio, io, tarfile, pathlib, itertools, git, shutil
async def f():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://github.com/fatedier/frp/releases/download/v0.34.1/frp_0.34.1_linux_amd64.tar.gz') as response:
            with io.BytesIO(await response.content.read()) as _:
                def f(tar):
                    for _ in tar.getmembers():
                        parts = pathlib.Path(_.name).parts 
                        if len(parts) > 2 and parts[1] == 'boost':
                            _.name = '/'.join(('include', *itertools.islice(parts, 1, None)))
                            yield _
                with tarfile.open(mode='r:bz2', fileobj=_) as tar: tar.extractall(members=f(tar))
    
asyncio.run(f())

with git.Repo(pathlib.Path(__file__).resolve().parent) as repository:
    repository.config_writer().set_value('user', 'name', 'Your Name').release()
    repository.config_writer().set_value('user', 'email', 'you@example.com').release()
    repository.index.commit('')#git commit --allow-empty-message -m ''
    repository.remote().push()
