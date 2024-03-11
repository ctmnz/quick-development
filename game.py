from abc import ABC, abstractmethod
from typing import List
import random

class Game(ABC):
    pass


class Player(ABC):
    def get_name():
        pass
    def get_info() -> str:
        pass

class GameException(Exception):
    pass


class VideoGame(Game):
    def __init__(self):
        self.players = [Player]
        self.max_players = 4

    def add_player(self, player: Player):
        if player in self.players:
            pass
        if len(self.players) > self.max_players:
            raise GameException(f"The game has {len(self.players)} joined players. Max possible players {self.max_players}! The game is full.")
        if player not in self.players:
            self.players.append(player)
    
    def del_player(self, player: Player):
        if player in self.players:
            self.players.remove(player)

    def get_players_info(self) -> [str]:
        result = []
        for player in self.players:
            result.append(player.get_info())
        return result

    def pvp_hit(self, player_source: Player, player_target: Player):
        dmg = random.randrange(1, player_source.attack_power)
        player_target.hp -= dmg

        
class GamePlayer(Player):
    def __init__(self, name:str, hp:int=100, mp:int=100, attack_power:int=10, spell_power:int=10):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.alive = True
        self.attack_power = attack_power
        self.spell_pwoer = spell_power

    def join_game(self, game: Game):
        game.add_player(self)
    
    def leave_game(self, game: Game):
        game.del_player(self)

    def get_name(self) -> str:
        return self.name

    def get_info(self) -> str:
        return f"Name: {self.name}\nHP: {self.hp}\nMP: {self.mp}\nAlive: {self.alive}\n"




