import os
from aiohttp.web import HTTPNotFound
from app.settings import CONFIG
from app.utils.logger import get_logger


logger = get_logger(__name__)

def path_exists(resource_name):
    def decorator_path_exists(func):
        async def wrapper(request, *args, **kwargs):
            path = os.path.join(CONFIG.MEDIA_URI, request.match_info[resource_name])
            if not os.path.exists(path):
                logger.info('Requested archive does not exist. Path: {}'.format(path))
                raise HTTPNotFound(reason=f'Archive does not exist or has been moved')
            return await func(request, *args, **kwargs)
        return wrapper
    return decorator_path_exists
