#!/usr/bin/python3
""" Fabric script (based on the file 2-do_deploy_web_static.py)
    that creates and distributes an archive to your web servers
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os
env.hosts = ['52.3.252.97', '100.25.197.100']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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
        print("web_static packed: {}".format(path))
        return path
    except Exception:
        return None


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
        remote_folder = "/data/web_static/releases/{}/".format(archive_no_ext)

        put(archive_path, remote_path)
        run("sudo mkdir -p {}".format(remote_folder))
        run("sudo tar -xzf {} -C {}".format(remote_path, remote_folder))
        run("sudo rm {}".format(remote_path))
        run("sudo mv {0}web_static/* {0}".format(remote_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(remote_folder))

        return True
    except Exception:
        return False


def deploy():
    """Call the do_pack() function and store the path of the
        created archive
    """

    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive_path=archive)
