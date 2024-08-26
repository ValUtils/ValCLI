import typer
from rich.console import Console
from rich.table import Table

from ValVault.terminal import init_vault

from .user import UserName

vault = typer.Typer()


@vault.command()
def alias(username: UserName, alias: str):
    db = init_vault()
    db.find_one(username=username).alias = alias
    db.db.save()


@vault.command()
def delete(username: UserName):
    db = init_vault()
    db.find_one(username=username).entry.delete()
    db.db.save()


@vault.command()
def auth(
    username: UserName, remember: bool = True, force: bool = False, legacy: bool = False
):
    db = init_vault()
    entry = db.find_one(username=username)
    if force:
        entry._auth = None
    if legacy:
        from ValLib.auth import legacy_auth
        entry.auth = legacy_auth(entry.as_user(), remember)
        return
    entry.get_auth(remember, True)
    db.db.save()


@vault.command()
def add(username: str, alias: str = ""):
    db = init_vault()
    password = typer.prompt("Password: ", hide_input=True)
    db.save_user(username, password, alias)
    db.db.save()


@vault.command("list")
def list_users():
    t = Table(title="Users")
    t.add_column("Alias", no_wrap=True)
    t.add_column("Username", no_wrap=True)
    db = init_vault()
    for alias, users in zip(db.aliases, db.users):
        t.add_row(alias, users)
    console = Console()
    console.print(t)
