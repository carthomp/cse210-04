# Greed Design

```
For Greed:


Directing
--+ Director
    Responsibility: Direct the order of the steps of the game
    Relationship: Manages the Services and collects the Actors
Services
--+ Keyboard Service
    Responsibility: Respond to user keyboard input
    Relationship: Managed by Director
--+ Video Service
    Responsibility: Display the game on the screen
    Relationship: Managed by Director
Casting
--+ Actor
    Responsibility: Create any visible, moveable object in the game and keep track of its position, color, and movement
    Relationship: Parent of Gem and Rock, and managed by Director
--+ Gem
    Responsibility: Create the gem elements, gives them movement, and add points whenever the player interacts with them
    Relationship: Inherits traits from Actor, managed by Director
--+ Rock
    Responsibility: Create the rock elements, gives them movement, and subtracts points whenever the player interacts with them
    Relationship: Inherits from Actor, managed by Director
Shared
--+ Color
    Responsibility: Create a random color using RGB colors
    Relationship: Used by Actors and Director to apply color to all Actors
--+ Point
    Responsibility: Show and keep information about the X,Y position
    Relationship: Used by Actors and Director to keep track of where an Actor is on screen
    
```
