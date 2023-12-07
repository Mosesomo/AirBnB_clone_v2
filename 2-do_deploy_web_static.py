#!/usr/bin/python3
"""Fabric script that distributes an archive to your web
    servers, using the function do_deploy:
"""
from fabric.api import run, put, env
import os
env.hosts = ['52.3.252.97', '100.25.197.100']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Returns False if the file at the path archive_path
        doesnt exist
    Args:
        archive_path: path
    """

    if not os.path.exists(archive_path):
        return False
    try:
        archive = archive_path.split('/')[-1]
        archive_no_ext = archive.split('.')[0]
        remote_path = "/tmp/{}".format(archive)
        remote_folder = "/data/web_static/releases/{}".format(archive_no_ext)

        put(archive_path, remote_path)
        run("sudo mkdir -p {}".format(remote_folder))
        run("sudo tar -xzf {} -C {}".format(remote_path, remote_folder))
        run("sudo rm -rf {}".format(remote_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(remote_folder))

        return True
    except Exception:
        return False
