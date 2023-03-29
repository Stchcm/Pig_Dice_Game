## 🎲 Pig Dice Game
| ![license badge](https://img.shields.io/badge/license%20-MIT-green) | ![coverage badge](https://img.shields.io/badge/coverage%20-99%25-success) | ![pylint badge](https://img.shields.io/badge/pylint-passed-blue) | ![flake8 badge](https://img.shields.io/badge/flake8-passed-blue) |
| :-----------------------------------------------------------------: | :-----------------------------------------------------------------------: | :--------------------------------------------------------------: | :--------------------------------------------------------------: |

A concise guide on how to engage in the game:

- Two players can participate in the game, or one can play against the computer. Each turn involves rolling a pair of six-sided dice by a player.

- The total of the numbers shown on the dice determines the player's score for the turn.

- A player has the option to roll again, adding the new sum to their existing score or to conclude their turn, retaining their current score.

- Should a player roll a one on any of the dice, their turn comes to an end, and their score for that turn is nullified.

- In the event that a player rolls a one on both dice, their turn is over, and they lose their entire score for that round.

- Victory is achieved when a player reaches a pre-established target score (100 points) first.

## ⚠️ Requirements
**python** - >= v3.10

**make** - You might want to use Chocolatey in order to install make on Windows

**pip** - Usually comes with Python but you might need to manually install it

**graphviz** - Optional and only required in case you want to generate UML for the codebase

**_Important:_** _Use just native terminal/cmd to launch the game; avoid using IDEs.

## 🎮 Play the Game
_To start and play the game follow the steps listen down below_

Clone the game

```bash
  https://github.com/Stchcm/Pig_Dice_Game.git
```
To go to the game directory

```bash
  cd Pig_Dice_Game
```

To create and activate a virtual enviroment(Linux/macOS)

```bash
  python -m venv venv && source ./venv/bin/activate
```

To create and activate a virtual enviroment(Windows)

```bash
  python -m venv venv && .\venv\Scripts\activate
```

To install required dependencies

```bash
  make init
```

Running the game

```bash
  make play
```

! Don't forget to deactivate virtual enviroment when finished!

```bash
  deactivate
```

**_Important -_** _Always reactivate virtual environment before playing._

**_Note:_** _Running 'make' without specifying any args will result in 'make init' being invoked._

## ⚙️ Tests - for development purposes

To execute tests and linters follow this command

```bash
  make test dir=./src/<package>
```

To run tests and linters on the player package you can do the following:

```bash
  make test dir=./src/player
```

**_Note:_** _Windows users must use a bash terminal such as [git bash](https://gitforwindows.org/) in order for this to work correctly._

## 📃 Documentation - for development purposes

For viewing documentation for different modules proceed to follow the following commands:

```bash
  make doc module=./src/<package>/<module>.py
```

For viewing documentation for the player mod you can do the following command:

```bash
  make doc module=./src/player/player.py
```

## 📝 UML - for development purposes 

For generating UML, run the following command

```bash
  make uml
```

After that UMLs will be generated in the root directory

## 🖥️ Computer Difficulty - for development purposes

We had the chance to develop a dice game that involved randomness in its gameplay mechanics. However, we aimed to make the game more interesting and unpredictable by **manipulating the probabilities of certain outcomes.**

To achieve this, we utilized **biased probabilities to limit the likelihood of particular outcomes when rolling the dice.**

For example, we increased the chances of bots winning more points in the hard level by **boosting the likelihood of rolling a higher number on the die.**
We also made it more difficult for players to beat bots by **reducing the probability of the bots rolling a low number.**
The same method was applied to handle the bot's decision to roll or pass the dice.

By introducing these biased probabilities, we created a gameplay experience that was both challenging and unpredictable.

It is essential to note that introducing biased probability into a game **needs careful consideration and testing to ensure that the gameplay remains fair and balanced.**
If the probabilities are excessively skewed, the game may lose its appeal to players by becoming imbalanced. Hence, it is vital to adjust the probabilities cautiously to create an exclusive gameplay experience while still maintaining fairness and balance.

Overall, manipulating the probabilities of certain outcomes in a dice game can be an effective method to create a more engaging and exciting gameplay experience. With careful planning and testing, it is possible to introduce biased probability that is enjoyable and fair for players.
