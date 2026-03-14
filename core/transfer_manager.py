from core.tool_detector import ToolDetector
from tools.rsync_tool import RsyncTool


class TransferManager:

    TOOL_MAP = {
        "rsync": RsyncTool
    }

    def __init__(self, conn, bandwidth=None):

        self.conn = conn
        self.bandwidth = bandwidth

        detector = ToolDetector()
        available = detector.detect()

        self.tools = []

        for tool in available:
            if tool in self.TOOL_MAP:
                self.tools.append(self.TOOL_MAP[tool]())

    def transfer_with_fallback(self, src, dst, direction="push"):

        for tool in self.tools:

            try:

                tool.transfer(
                    src,
                    dst,
                    self.conn,
                    self.bandwidth,
                    direction
                )

                return True

            except Exception:
                continue

        raise RuntimeError("All transfer tools failed")
