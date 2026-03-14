from pathlib import Path

from core.config import ConfigManager
from core.transfer_manager import TransferManager


def run_push_file(args):

    config = ConfigManager(args.config)

    conn = {
        "host": config.host,
        "user": config.user,
        "key": config.key
    }

    manager = TransferManager(conn)

    file_path = Path(args.file)

    remote = config.target + "/" + file_path.name

    manager.transfer_with_fallback(
        str(file_path),
        remote,
        direction="push"
    )
