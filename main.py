from app.server import run_app
from app.utils.cli_parser import activate_cli


if __name__ == '__main__':
    activate_cli()
    run_app()