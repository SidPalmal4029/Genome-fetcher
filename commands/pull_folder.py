from core.config import ConfigManager
from core.transfer_manager import TransferManager


def run_pull_folder(args):

    config = ConfigManager(args.config)

    conn = {
        "host": config.host,
        "user": config.user,
        "key": config.key
    }

    manager = TransferManager(conn)

    remote = config.target + "/" + args.folder

    manager.transfer_with_fallback(
        remote,
        args.folder,
        direction="pull"
    )
