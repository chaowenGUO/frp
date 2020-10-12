import aiohttp, asyncio, io, tarfile, pathlib, itertools, git, shutil
async def f():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://dl.bintray.com/boostorg/release/1.71.0/source/boost_1_71_0.tar.bz2') as response:
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
    static = pathlib.Path('/static')
    repository.git.subtree('add', '--prefix=' + str(static), 'https://github.com/chaowenGUO/aiohttp', 'master', '--squash')
    for _  in static.iterdir():
        if _.suffix == '.html' or _.suffix == '.js' or _.suffix == '.sql': shutil.move(str(_), static.parent)
    shutil.rmtree(static)
