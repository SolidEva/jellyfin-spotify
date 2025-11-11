#!/usr/bin/env python3
import jellyfin_api
import click

def run(jellyfin_username, jellyfin_password, server, jellyfin_library_id):
    jelly = jellyfin_api.jellyfin(server, jellyfin_username, jellyfin_password)
    jelly.scan_library(jellyfin_library_id)

@click.command()
@click.option("--jellyfin_username", type=str, required=True, help="username of the user to login as")
@click.option("--jellyfin_password", type=str, required=True, help="password of the user to login as")
@click.option("--server", type=str, required=True, help="server url")
@click.option("--jellyfin_library_id", type=str, required=True, help="id of the jellyfin library to scan")
def main(jellyfin_username, jellyfin_password, server, jellyfin_library_id):
    run(jellyfin_username=jellyfin_username,
        jellyfin_password=jellyfin_password,
        server=server,
        jellyfin_library_id=jellyfin_library_id)

if __name__ == "__main__":

    main()
