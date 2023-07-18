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
       # Write your code here.
    stack_aster = []
    for curr in asteroids:
        # Collision when incoming asteroid is -ve 
        # top of the stack is posive
        while stack_aster and curr < 0 < stack_aster[-1]:
             top = stack_aster[-1]
            #both are equal so both destroyed
             if abs(top) == abs(curr):
                stack_aster.pop()
                break
             # +ve asteroid on top of stack is destroyed
             elif abs(top) < abs(curr):
                stack_aster.pop()
                continue
             
             else:# the new -ve asteroid was destroid by larger asteroid on top of the stack

                break
        else:
            stack_aster.append(curr)
            # -ve asteroid made it all the way to the 
            # bottom of the stack and destroyed all asteroids

    return stack_aster
