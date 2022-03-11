# Pig Dice Game

This is a Pig (dice game) project.

# Authors

Ahmed Mohammed Ahmed, Murwan Eisa

# About the Game

Pig is a simple dice game. Players take turns to roll a single dice as many times as they wish, adding all roll results to a running total, but losing their gained score for the turn if they roll a 1.

# Gameplay

Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

- If the player rolls a 1, they score nothing and it becomes the next player's turn.
- If the player rolls any other number, it is added to their turn total and the player's turn continues.
- If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.

The first player to score 100 or more points wins.

For example, the first player, Donald, begins a turn with a roll of 5. Donald could hold and score 5 points, but chooses to roll again. Donald rolls a 2, and could hold with a turn total of 7 points, but chooses to roll again. Donald rolls a 1, and must end his turn without scoring. The next player, Alexis, rolls the sequence 4-5-3-5-5, after which she chooses to hold, and adds her turn total of 22 points to her score.

# About the application

We have developed an object-oriented Python application using the test-driven development process (TDD). The application consists of 5 classes which include Game, Player, Dice, HighScore and Intelligence.

# Install the dependencies

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the requirements.txt.

```bash
make install
```
