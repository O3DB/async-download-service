import os
from aiohttp.web import HTTPBadRequest, HTTPNotFound
from app.settings import CONFIG
from app.utils.logger import get_logger


logger = get_logger(__name__)


def validate_archive_hash(archive_hash):
    photo_archive_path = os.path.join(CONFIG.MEDIA_URI, archive_hash)
    if not os.path.exists(photo_archive_path):
        logger.info('Requested archive does not exist. Path: {}'.format(photo_archive_path))
        raise HTTPNotFound(reason=f'Archive does not exist or has been moved')

