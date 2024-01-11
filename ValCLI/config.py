import typer

from ValManager import config as cfg

from .user import UserName, user_get

config = typer.Typer()


@config.command()
def backup(username: UserName):
    user, auth = user_get(username)
    cfg.backup(user, auth)


@config.command()
def dump(username: UserName, config: str):
    _, auth = user_get(username)
    cfg.download(config, auth)


@config.command("import")
def imprt(username: UserName, config: str):
    user, auth = user_get(username)
    cfg.backup(user, auth)
    cfg.upload(config, auth)


@config.command()
def restore(username: UserName, config: int):
    user, auth = user_get(username)
    cfg.restore(user, auth, config)
