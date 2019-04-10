
import os

DEBUG = False
if "DEBUG" in os.environ:
    if os.environ["DEBUG"].lower() in ["1", "true", "on"]:
        DEBUG = True

DEVELOPER_MODE = False
if "DEVELOPER_MODE" in os.environ:
    if os.environ["DEVELOPER_MODE"].lower() in ["1", "true", "on"]:
        DEVELOPER_MODE = True
