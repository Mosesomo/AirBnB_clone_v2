#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the
    contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        Generates a .tgz archize from the content of web_static folder
        Returns: string path to the created archive or none
    """
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        path = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static".format(path))

        return path
    except Exception:
        return None
