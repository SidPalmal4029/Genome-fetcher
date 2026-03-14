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
    local_folder = args.folder
    remote_folder = config.target

    manager.transfer_with_fallback(
        local_folder,
        remote_folder,
        direction="push"
    )
