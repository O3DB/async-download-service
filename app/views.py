import os

from aiohttp import web
import aiofiles

from app.utils.logger import get_logger
from app.utils.send_archive import send_archive
from app.utils.helpers import path_exists
from app.settings import CONFIG


logger = get_logger()


@path_exists('archive_hash')
async def archive(request):
    archive_hash = request.match_info['archive_hash']
    resp = web.StreamResponse()
    resp.headers['Content-Disposition'] = f'attachment; filename="{archive_hash}.zip"'
    await resp.prepare(request)  # Отправка заголовков
    await send_archive(resp, archive_hash)
    return resp


async def index(request):
    tempate = os.path.join(CONFIG.TEMPLATES_URI, 'index.html')
    async with aiofiles.open(tempate, mode='r') as index_file:
        index_contents = await index_file.read()
    return web.Response(text=index_contents, content_type='text/html')
