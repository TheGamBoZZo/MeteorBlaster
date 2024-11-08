# Meteor Blaster

**Meteor Blaster** is an arcade-style space shooter game developed in Python using the Pygame library. Players control a spaceship to destroy meteors and dodge obstacles, aiming to achieve high scores. The game includes power-ups, customizable aesthetics, and sounds to enhance gameplay.

---

## Features

- **Spaceship Control**: Players can move the spaceship left or right and shoot at incoming meteors.
- **Power-Ups**: Golden stars occasionally appear, granting a rapid-fire mode when collected.
- **Score Tracking**: Players earn points for each meteor destroyed and can aim for a high score.
- **Game Over Screen**: At the end of each game, players see their final score, time survived, and options to replay or exit.
- **Background Music and Sound Effects**: Retro background music plays continuously, and collision sounds are triggered when the spaceship crashes.

---

## Installation

### Prerequisites

- Python 3.x
- Pygame library

Install Pygame with:

bash
pip install pygame


### Running the Game

1. Clone or download this repository.
2. Navigate to the project folder.
3. Run the game with the following command:

bash
   python meteor_blaster.py


---

## Game Controls

- **Arrow Keys**: Move the spaceship left or right.
- **Spacebar**: Shoot projectiles.
- **R**: Restart the game after Game Over.
- **ESC**: Exit the game.

---

## Game Mechanics

- **Meteors**: Randomly sized meteors spawn from the top of the screen and move downwards. Players earn points by shooting meteors.
- **Rapid-Fire Power-Up**: Golden stars appear occasionally; collecting one enables rapid-fire mode for a limited time.
- **Collision Detection**: Meteors hitting the spaceship result in a game over, prompting the Game Over screen.
- **Difficulty**: The speed and number of meteors increase as the game progresses.

---

## Code Structure

- **Spaceship Class**: Handles the spaceship’s position, movement, and shooting mechanics.
- **Projectile Class**: Manages the bullets shot by the spaceship.
- **Meteor Class**: Randomly spawns meteors with variable sizes and controls their movement.
- **Power-Up Class**: Manages the appearance and behavior of golden stars for rapid-fire mode.
- **Game Loop**: Contains the main logic for rendering, game state updates, and event handling.

---

## Assets
- **Sound Files**:
  - **Background Music**: `assets/music.mp3`
  - **Collision Sound**: `assets/crash.wav`

Ensure all assets are placed in an `assets` folder in the same directory as the game file for proper loading.

---

## Future Improvements

- **More Power-Ups**: Adding additional power-ups with unique effects.
- **Difficulty Scaling**: Introducing levels or difficulty scaling based on time survived.
- **Leaderboard**: Storing high scores locally or online for competitive play.
- **Visual Customization**: Additional spaceship designs and backgrounds for player customization.

---

## Troubleshooting

- **Pygame Issues**: Ensure Pygame is correctly installed by running `pip show pygame` to confirm.
- **File Paths**: Make sure the paths to images and sounds are correctly set. Default paths assume an `assets` folder in the project directory.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

Enjoy the game, and aim for a high score!
