"""
You're given an array of integers asteroids, where each integer
represents the size of an asteroid. The sign of the intger
represents the direction the asteroid is moving(positive=right, negative=lef).

For example, the integer 4 represents an asteroid moving to the right. Similarly, -7
represent an asteroid moving to the left.

If two asteroids collide, the smaller asteroid(based on the absolute value) explodes. If two colliding asteroids
are the same size, they both explode.

write a function that takes in this array of asteroids and returns an array of integers representing the asteroids after all
collisions occur.
"""

def collidingAsteroids(asteroids):
    results = []
    for asteroid in asteroids:
        if asteroid > 0:
            results.append(asteroid)
            continue
        
        while True:
            if len(results) == 0 or results[-1] < 0:
                results.append(asteroid)
                break

            asteroid = abs(asteroid)