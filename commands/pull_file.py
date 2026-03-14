from pathlib import Path

from core.config import ConfigManager
from core.transfer_manager import TransferManager


def run_pull_file(args):

    config = ConfigManager(args.config)

    conn = {
        "host": config.host,
        "user": config.user,
        "key": config.key
    }

    manager = TransferManager(conn)

    remote = config.target + "/" + args.file
    local = Path(args.file)

    manager.transfer_with_fallback(
        remote,
        str(local),
        direction="pull"
    )
