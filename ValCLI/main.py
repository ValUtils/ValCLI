from sys import argv

import typer

from ValVault.terminal import init_vault

from .config import config
from .loadout import loadout
from .match import match_typer
from .user import UserName
from .vault import vault

app = typer.Typer()
app.add_typer(loadout, name="loadout")
app.add_typer(config, name="config")
app.add_typer(vault, name="vault")
app.add_typer(match_typer, name="match")


@app.command()
def launch(username: UserName):
    from ValChange.config import get_config
    from ValChange.main import change
    cUser = get_config(username)
    change(cUser)


def tui():
    print("TBA")


def main():
    if len(argv) > 1:
        init_vault()
        app()
        return
    tui()
