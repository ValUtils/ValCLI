from typing import Annotated, Tuple

import typer

from ValLib import ExtraAuth, User
from ValVault.terminal import (
    EntryNotFoundException,
    get_auth,
    get_pass,
    init_vault
)


def username_get(user: str) -> str:
    db = init_vault()
    if user in db.users:
        return user
    try:
        return db.find_one(alias=user).username
    except EntryNotFoundException:
        raise typer.BadParameter("User doesn't exist")


def user_get(username: str) -> Tuple[User, ExtraAuth]:
    password = get_pass(username)
    user = User(username, password)
    auth = get_auth(user)
    return (user, auth)


UserName = Annotated[str, typer.Argument(parser=username_get)]
