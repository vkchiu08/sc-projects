"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts
switch = 1               # 遊戲的開關(1=開, -1=關)



def main():
    graphics = BreakoutGraphics()
    global switch
    # Add animation loop here!
    while switch == 1 and graphics.fall_count < 3:       # 開關開啟的時候，球還沒墜落三次時可以執行遊戲
        if graphics.fall_count == NUM_LIVES:
            break
        if graphics.break_count == graphics.brick_cols * graphics.brick_rows:
            break
        if graphics.ball.y >= graphics.window.height:    # 球墜落時，遊戲的開關關閉
            switch = -1
        if switch == -1:
            switch = 1                                   # 墜落完，重新設定球的起始點跟速度，並將遊戲開關重新打開
            graphics.reset_ball_position()
            graphics.restart()

        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.ball_bounce_wall()
        graphics.bounce_and_breakout()
        graphics.leave_paddle()
        pause(FRAME_RATE)











if __name__ == '__main__':
    main()
