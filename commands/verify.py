from pathlib import Path
from core.checksum import sha256sum
from core.config import ConfigManager
from core.remote_manager import RemoteManager


def run_verify(args):
    config = ConfigManager(args.config)
    conn = {
        "host": config.host,
        "user": config.user,
        "key": config.key
    }

    remote = RemoteManager(conn)
    local_file = Path(args.file)
    local_hash = sha256sum(local_file)
    remote_path = config.target + "/" + local_file.name
    remote_hash = remote.run(
        f"sha256sum {remote_path} | cut -d ' ' -f1"
    ).strip()
    if local_hash == remote_hash:
        print("Verification successful")
    else:
        print("Verification failed")
