from core.config import ConfigManager
from core.engine import TransferEngine


def run_transfer(args):
    config = ConfigManager(args.config)
    conn = {
        "host": config.host,
        "user": config.user,
        "key": config.key
    }
    engine = TransferEngine(conn)
    if args.mode == "send":
        engine.send(args.src, args.dst)
    elif args.mode == "fetch":
        engine.fetch(args.src, args.dst)
