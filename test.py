import unittest
from locallib import *
from game import *


def debug_game_info(game: VideoGame):
    """Helper function the print players stats in the game"""
    print("====================================================================\n")
    for p in game.get_players_info():
        print(p)
    print("-- end --\n")


class Test(unittest.TestCase):
    def test_initial(self):
        name = "Daniel"
        msg = hello_msg("Daniel")
        self.assertEqual(msg, "Hello, Daniel")


    def print_player_stats(self, player: Player):
        print(f"Name: {player.name}\nHP: {player.hp}\nMP: {player.mp}\nAlive: {player.alive}\n")


    def test_join_leave_game(self):
        game1 = VideoGame()
        player1 = GamePlayer("Player1")
        player2 = GamePlayer("Player2")
        player3 = GamePlayer("Player3")
        player4 = GamePlayer("Player4")
        player5 = GamePlayer("Player5")
        self.assertEqual("Player1", player1.get_name())
        player1.join_game(game1)
        self.assertEqual(2, len(game1.players))
        self.assertEqual("Player1", game1.players[1].get_name())
        player1.leave_game(game1)
        self.assertEqual(1, len(game1.players))
        ## try to make the game full
        player1.join_game(game1)
        player2.join_game(game1)
        player3.join_game(game1)
        player4.join_game(game1)
        with self.assertRaises(GameException):
            player5.join_game(game1)


    def test_player_hit_and_damage_conceive(self):
        game2 = VideoGame()
        player1 = GamePlayer("Player1")
        player2 = GamePlayer("Player2")
        player3 = GamePlayer("Player3")
        player4 = GamePlayer("Player4")
        player1.join_game(game2)
        player2.join_game(game2)
        player3.join_game(game2)
        player4.join_game(game2)
        debug_game_info(game2)
        game2.pvp_hit(player1, player2)
        game2.pvp_hit(player1, player2)
        game2.pvp_hit(player1, player2)
        game2.pvp_hit(player1, player2)
        game2.pvp_hit(player1, player2)
        game2.pvp_hit(player1, player2)
        game2.pvp_hit(player1, player2)
        game2.pvp_hit(player1, player2)
        game2.pvp_hit(player1, player2)
        game2.pvp_hit(player1, player2)
        debug_game_info(game2)


def main():
    unittest.main()


if __name__ == "__main__":
    main()

unittest.main()
