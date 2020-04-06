import sys
import argparse
from app.main import run_app
from app.settings import CONFIG


def init_parser():
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('-f', '--photos_path', help='Имя папки с каталогами фотографий')
    parser.add_argument('-d', '--delay', help='Задержка на отправку ответа клиенту (сек)', type=int)
    parser.add_argument('-l', '--loglevel',
                        help='Уровень логирования (DEBUG, INFO, WARNING, CRITICAL).\n'\
                        'Для отключения логирования - "OFF"')
    return parser


def process_args(args):
    if args.photos_path:
        CONFIG.PHOTOS_PATH = args.photos_path
        # os.environ['PHOTOS_PATH'] = args.photos_path
        print(f'Photos path set to : {args.photos_path}')
    if args.delay:
        CONFIG.DELAY = args.delay
        # os.environ['DELAY'] = args.delay
        print(f'Delay set to : {args.delay}')
    if args.loglevel:
        level = args.loglevel if args.loglevel != 'OFF' else sys.maxsize
        print('LEVEL ', level)
        CONFIG.LOG_LEVEL = level
        # os.environ['LOG_LEVEL'] = args.loglevel
        print(f'Logging level set to : {args.loglevel}')


def activate_cli():
    parser = init_parser()
    process_args(parser.parse_args())

activate_cli()
run_app()