import os

print("=================== Current Environment ===================")
print("      REPOSITORY_NAME: %s" % os.environ.get("REPOSITORY_NAME", None))
print(" REPOSITORY_DIRECTORY: %s" % os.environ.get("REPOSITORY_DIRECTORY", None))
print("       DEVELOPER_MODE: %s" % os.environ.get("DEVELOPER_MODE", None))
print("           PYTHONPATH: %s" % os.environ.get("PYTHONPATH", None))
