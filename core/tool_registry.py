from tools.rsync_tool import RsyncTool
from tools.scp_tool import ScpTool
from tools.rclone_tool import RcloneTool
from tools.aspera_tool import AsperaTool


class ToolRegistry:

    def __init__(self):

        self.tools = [
            AsperaTool(),
            RcloneTool(),
            RsyncTool(),
            ScpTool()
        ]

    def available_tools(self):

        return [tool for tool in self.tools if tool.available()]
