# 🎮 **Catch the Falling Object Game** 🎮

## 🚀 Overview
Welcome to **Catch the Falling Object**! This is a simple yet addictive game built with **Python** and **Pygame**. The objective is simple: control the player to catch falling objects before they hit the ground. Every time you catch an object, your score increases. But be careful — miss too many, and it’s **Game Over**!

Perfect for gamers who love quick reflex challenges! Are you ready to test your skills?

---

## 🕹️ **How to Play**
1. **Move Left**: Use the **Left Arrow** key to move the player to the left.
2. **Move Right**: Use the **Right Arrow** key to move the player to the right.
3. **Catch Objects**: Your goal is to catch the falling objects to score points.
4. **Game Over**: If you miss 6 objects, the game will end!
5. **Restart**: Press **R** to restart the game once it's over.

### Tips:
- The faster you catch objects, the higher your score!
- Be strategic — move quickly but carefully to avoid missing too many objects.

---

## 📜 **Features**
- **Catch falling objects**: Your goal is to catch as many falling objects as possible without missing.
- **Player Movement**: Move your player with the left and right arrow keys.
- **Score Tracking**: Keep track of your score as you catch objects. The faster you catch, the higher your score.
- **Game Over Mechanism**: The game ends after 6 missed objects. Press **R** to restart the game.
- **Simple yet Challenging**: With adjustable difficulty via object speed and player control, the game stays challenging yet fun.

---

## ⚙️ **Code Breakdown**

### 1. **Game Setup**
The game runs at **800x600 pixels**, and uses **60 FPS** for smooth gameplay. The player is a black rectangle that moves left and right, while falling objects are red rectangles. You control the player with the arrow keys.

### 2. **Player Class**
The **Player** class allows the player to move left and right using the arrow keys. Movement is restricted to the screen’s boundaries, ensuring the player cannot move off-screen.

```python
if keys[pygame.K_LEFT]:
    player.move(-PLAYER_SPEED)  # Move left
if keys[pygame.K_RIGHT]:
    player.move(PLAYER_SPEED)  # Move right
