import os
import asyncio
from app.settings import CONFIG
from app.utils.logger import get_logger


logger = get_logger(__name__)


async def send_archive(resp, archive_hash):
    path = os.path.join(CONFIG.MEDIA_URI, archive_hash)
    cmd = ['zip', '-', path, '-r', '-j']
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        )
    # send archive to a client
    try:
        while True:
            archive_chunk = await proc.stdout.readline()
            if not archive_chunk:
                break
            logger.info('Sending archive chunk {:.2} Mb'.format(len(archive_chunk) / 1024))
            await resp.write(archive_chunk)
            await asyncio.sleep(CONFIG.DELAY)
        logger.info('Archive {} was sent'.format(archive_hash))
    except (asyncio.CancelledError):
        logger.info('Download was interrupted')
        proc.terminate()
        raise
    finally:
        resp.force_close()
