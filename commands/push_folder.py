from pathlib import Path

from core.config import ConfigManager
from core.transfer_manager import TransferManager
from core.parallel_engine import parallel_transfer


def run_push_folder(args):

    config = ConfigManager(args.config)

    conn = {
        "host": config.host,
        "user": config.user,
        "key": config.key
    }

    manager = TransferManager(conn)

    folder = Path(args.folder)

    files = [x for x in folder.rglob("*") if x.is_file()]

    def transfer(f):

        rel = f.relative_to(folder)

        remote = config.target + "/" + str(rel)

        manager.transfer_with_fallback(
            str(f),
            remote,
            direction="push"
        )

    workers = args.workers or 8

    parallel_transfer(files, transfer, workers)
