from main import *
import math


# Player Class. They will be capable of pointing towards a single direction
class Player:
    # Runs on instance initialization
    def __init__(self, x, y, width, height):
        self.rect = pg.FRect(x, y, width, height)
        # Player angle
        self.angle = 0
        # Sets up unique prevTime
        self.prevTime = time.time()

        # Holds the direction the player will go in each direction.
        # 1 = forward, -1 = backwards, 0 = Don't move
        self.dirX = 0
        self.dirY = 0

        # Velocity that automatically move the player based on the value
        self.velocity = pg.Vector2()

        # The player's speed.
        self.speed = 5

    # Runs once every frame.
    def update(self, mousePos, deltaTime):
        self.getAngle(mousePos)

        self.movementLocal(deltaTime)

    # Automatically moves the player locally based on dirX and dirY
    # Which this you can make the player orbit the mouse. Gives me an idea on how to do pivoting
    def movementLocal(self, deltatime):
        self.velocity = pg.Vector2(self.dirX, self.dirY).rotate(self.angle) * self.speed * deltatime * TARGET_FPS

        self.rect.center += self.velocity

    # Handles what happens when a key is pressed
    def keyDown(self, key):
        # Moves the player locally based on angle
        if key == pg.K_d:
            self.dirX += 1  # Left
        if key == pg.K_a:
            self.dirX -= 1  # Right
        if key == pg.K_s:
            self.dirY += 1  # Down
        if key == pg.K_w:
            self.dirY -= 1  # Up

    # Handles what happens when a key is released.
    def keyUp(self, key):
        # Stops the player locally based on angle
        if key == pg.K_d:
            self.dirX -= 1  # Left
        if key == pg.K_a:
            self.dirX += 1  # Right
        if key == pg.K_s:
            self.dirY -= 1  # Down
        if key == pg.K_w:
            self.dirY += 1  # Up

    # Gets the angle needed for the player to point at the mouse.
    def getAngle(self, mousePos):
        # Splits the player's vector
        playerX, playerY = self.rect.center
        # Splits mousePos vector
        mouseX, mouseY = mousePos

        """I think what's going on here is that with math.atan2, it subtracts playerX with mouseY. Then since in
        pygame's coordinate system, the Y axis pointing down so the operations are reversed for Y. Then I guess
        with it converts it two degrees. I personally increased the result by 180 so it could stay within the 360 range.
        
        I'm guessing this statement revolves around the base position(The player in this case) and the target position
        (Which is the position of the mouse) and gets the angle value the player needs to point towards the mouse."""
        self.angle = math.degrees(math.atan2(playerX - mouseX, mouseY - playerY)) + 180
