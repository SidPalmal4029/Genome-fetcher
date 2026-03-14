import time
import tempfile
import os
from core.config import ConfigManager
from core.transfer_manager import TransferManager


def run_benchmark(args):
    config = ConfigManager(args.config)
    conn = {
        "host": config.host,
        "user": config.user,
        "key": config.key
    }

    manager = TransferManager(conn)
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(os.urandom(50 * 1024 * 1024))  # 50MB
    temp_file.close()
    start = time.time()
    manager.transfer_with_fallback(
        temp_file.name,
        config.target + "/benchmark.tmp"
    )
    end = time.time()
    size_mb = 50
    speed = size_mb / (end - start)
    print(f"Transfer speed: {speed:.2f} MB/s")
    os.remove(temp_file.name)
