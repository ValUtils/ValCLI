import typer
from httpx import get
from ValWrap import (
    get_current_game_player,
    get_pregame_player,
    post_current_game_quit,
    post_pregame_quit,
    post_select_character,
)

from .user import UserName, user_get

match_typer = typer.Typer()


@match_typer.command()
def dodge(username: UserName):
    _, auth = user_get(username)
    match_player = get_pregame_player(auth)
    post_pregame_quit(auth, match_player['MatchID'])


@match_typer.command()
def select(username: UserName, agent: str):
    _, auth = user_get(username)
    match_player = get_pregame_player(auth)
    agents = get("https://valorant-api.com/v1/agents").json()["data"]
    agents = {agent["displayName"]: agent["uuid"] for agent in agents}
    if agent not in agents:
        return
    post_select_character(auth, match_player['MatchID'], agents[agent])


@match_typer.command()
def leave(username: UserName):
    _, auth = user_get(username)
    match_player = get_current_game_player(auth)
    post_current_game_quit(auth, match_player['MatchID'])

