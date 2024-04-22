#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder
    """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except (PermissionError, FileNotFoundError):
        return None
