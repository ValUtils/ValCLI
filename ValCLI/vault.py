import typer

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
def auth(username: UserName, remember: bool = True, force: bool = False):
    db = init_vault()
    entry = db.find_one(username=username)
    if force:
        entry._auth = None
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
    db = init_vault()
    res = "\n".join(db.users)
    print(res)
