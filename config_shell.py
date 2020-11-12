#!/usr/bin/env python
import argparse

import yaml
from box import Box


def argument_parsing() -> argparse.Namespace:
    """ Parse arguments from command line
    :return Object of all arguments
    """
    parser = argparse.ArgumentParser(description="Load configuration file to environnement variable to use shell command")
    parser.add_argument('-r', '--repo', help='Repository name', required=True)
    parser.add_argument('config', help='Configuration file (default: config.yml)', nargs='?', default="config.yml")
    return parser.parse_args()


def load_config(filename: str) -> Box:
    with open(filename, 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    return Box(cfg, box_it_up=True)


if __name__ == '__main__':
    args = argument_parsing()
    config = load_config(args.config)

    print(f"export RCLONE_CONNECTION_NAME={config.information.rclone_connection_name}")
    print(f"export CLIENT_NAME={config.information.client_name}")
    print(f"export BUCKET_NAME={config.information.bucket_name}")
    print(f"export SERVER_NAME={config.information.server_name}")
    print(f"export RESTIC_REPO_NAME={args.repo}")
    restic_cmd = (
        fr"{config.binaries.restic} "
        fr"-r rclone:{config.information.rclone_connection_name}:{config.information.bucket_name}/"
        fr"{config.information.client_name}/{config.information.server_name}/{args.repo}"
    )
    print(f"export RESTIC_CMD=\"{restic_cmd}\"")
