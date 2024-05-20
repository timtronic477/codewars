# Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.

def combat(health, damage):
    current_health = health - damage
    return 0 if current_health < 0 else current_health
