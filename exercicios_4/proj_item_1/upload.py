import click
import os
import logging

from base import *


@click.command()
@click.option('--file', '-f', 'file_path', help='path to save the file', prompt='file')
@click.option('--content', '-c', 'content', help='content to be saved', prompt='content')
@click.option('--user', '-u', 'user_name', help='user that are using the program', prompt='user')
@click.option('--debug', '-d', 'debug', help='debuging info will be printed', default=False, is_flag=True)
def upload(file_path, content, user_name, debug):
    validate_bases(debug)
    user_set = load_users(user_name)

    path = os.path.join(user_name, file_path)
    logging.debug('path: %s' % path)
    cmd = 'echo %s > %s' % (content, path)
    logging.debug('command to run: %s' % cmd)
    os.system(cmd)


if __name__ == '__main__':
    upload()
