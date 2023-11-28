# PicoPong.py: a simple Pong game by Vincent Mistler (YouMakeTech)
from RP import *
import random

LCD = LCD_1inch28()
LCD.set_bl_pwm(30000)
qmi8658=QMI8658()
Vbat= ADC(Pin(Vbat_Pin))

def color(R,G,B): # Convert RGB888 to RGB565
    return (((G&0b00011100)<<3) +((B&0b11111000)>>3)<<8) + (R&0b11111000)+((G&0b11100000)>>5)

R = random.randint(-1,256)
G = random.randint(-1,256)
B = random.randint(-1,256)

c1 = color(R,G,B)
c2 = color(256 - R,256-G,256-B)
c3 = color(256-R,256 - G,B)

def pico_pong_main():
    # Game parameters
    SCREEN_WIDTH = 240                       # size of the screen
    SCREEN_HEIGHT = 240
    BALL_SIZE = int(SCREEN_WIDTH/32)         # size of the ball size in pixels
    PADDLE_WIDTH = int(SCREEN_WIDTH/8)       # size of the paddle in pixels
    PADDLE_HEIGHT = int(SCREEN_HEIGHT/16)
    PADDLE_Y = SCREEN_HEIGHT-2*PADDLE_HEIGHT # Vertical position of the paddle

    # variables
    ballX = random.randint(0,240)     # ball position in pixels
    ballY = 120
    ballVX = 2.0    # ball velocity along x in pixels per frame
    ballVY = 2.0    # ball velocity along y in pixels per frame

    paddleX = int(SCREEN_WIDTH/2) # paddle  position in pixels
    paddleVX = 3                  # paddle velocity in pixels per frame
    score = 0

    while True:
        #READ axix data
        xyz=qmi8658.Read_XYZ()
        x_shift = int(xyz[3]/10)
        # move the paddle when a button is pressed
        if x_shift < 0:
            # right move
            paddleX += paddleVX
            if paddleX + PADDLE_WIDTH > SCREEN_WIDTH:
                paddleX = SCREEN_WIDTH - PADDLE_WIDTH
        elif x_shift > 0:
            # left move
            paddleX -= paddleVX
            if paddleX < 0:
                paddleX = 0
        
        # move the ball
        if abs(ballVX) < 1:
            # do not allow an infinite vertical trajectory for the ball
            ballVX = 1

        ballX = int(ballX + ballVX)
        ballY = int(ballY + ballVY)
        
        # collision detection
        collision=False
        if ballX < 0:
            # collision with the left edge of the screen 
            ballX = 0
            ballVX = -ballVX
            collision = True
        
        if ballX + BALL_SIZE > SCREEN_WIDTH:
            # collision with the right edge of the screen
            ballX = SCREEN_WIDTH-BALL_SIZE
            ballVX = -ballVX
            collision = True

        if ballY+BALL_SIZE>PADDLE_Y and ballX > paddleX-BALL_SIZE and ballX<paddleX+PADDLE_WIDTH+BALL_SIZE:
            # collision with the paddle
            # => change ball direction
            ballVY = -ballVY
            ballY = PADDLE_Y-BALL_SIZE
            # increase speed!
            ballVY -= 0.2
            ballVX += (ballX - (paddleX + PADDLE_WIDTH/2))/10
            collision = True
            score += 10
            
        if ballY < 0:
            # collision with the top of the screen
            ballY = 0
            ballVY = -ballVY
            collision = True
            
        if ballY + BALL_SIZE > SCREEN_HEIGHT:
            # collision with the bottom of the screen
            # => Display Game Over
            LCD.fill(c1)
            LCD.text("GAME OVER", int(SCREEN_WIDTH/2)-int(len("Game Over!")/2 * 8), int(SCREEN_HEIGHT/2) - 8,LCD.white)
            LCD.text(str(score),int(SCREEN_WIDTH/2)-int(len(str(score))/4),int(SCREEN_HEIGHT/10),LCD.white)
            LCD.show()
            
            # wait for a button
            while x_shift == 0 :
                time.sleep(0.001)
            # exit the loop
            break
            
        # clear the screen
        LCD.fill(c1)
        
        # display the paddle color
        LCD.fill_rect(paddleX, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT, c2)
        
        # display the ball color
        LCD.fill_rect(ballX, ballY, BALL_SIZE, BALL_SIZE, c3)
        
        # display the score
        LCD.text(str(score), int(SCREEN_WIDTH/2)-int(len(str(score))*8),int(SCREEN_HEIGHT/10),LCD.white)
        LCD.show()
        
if __name__ == "__main__":
    pico_pong_main()