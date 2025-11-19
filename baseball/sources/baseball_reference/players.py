from .session import *
from bs4 import BeautifulSoup
from string import ascii_lowercase

session = BaseballReferenceSession()


# TODO JASON ADD ARGS KWARGS RETURN TYPE
def get_all_players():
    """
    Gets all players from Baseball reference.
    """
    player_url = f"{BASE_URL}/players"
    # iterate through all the lowercase letters in the alphabet to access all the players
    # that are listed under that letter
    for c in ascii_lowercase:
        html = session.get(f"{player_url}/{c}").content
        soup = BeautifulSoup(
            html,
            "lxml",
        )
        player_html = soup.find(
            "div",
            class_="section_content",
            id="div_players_",
        )
        players = player_html.find_all("p")
        for player in players:
            player_name = player.get_text()
            player_html = player.find("a")["href"]
            is_current_player = True if player.find("b") else False
            # hopefully no player has a + in their name, if they do, they just
            # became a hall of famer
            is_hall_of_famer = True if "+" in player.get_text() else False
            print(
                f"player: {player_name} - {is_current_player} - {is_hall_of_famer} - "
                f"{player_html}"
            )
            # TODO JASON DO WE PUT THESE INTO A DB TABLE LIKE PLAYERS SHALLOW AND THEN DO A
            #  DEEPER SEARCH FOR A REQUESTED PLAYER
