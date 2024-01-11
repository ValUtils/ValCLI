import typer

from ValManager import loadout as ldout

from .user import UserName, user_get

loadout = typer.Typer()


@loadout.command()
def backup(username: UserName):
    _, auth = user_get(username)
    ldout.backup(auth)


@loadout.command()
def dump(username: UserName, config: str):
    _, auth = user_get(username)
    ldout.download(config, auth)


@loadout.command("import")
def imprt(username: UserName, config: str):
    _, auth = user_get(username)
    ldout.backup(auth)
    ldout.upload(config, auth)


@loadout.command()
def restore(username: UserName):
    _, auth = user_get(username)
    ldout.restore(auth)
