"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 8       # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle_offset = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.x = (window_width-ball_radius*2)/2
        self.ball.y = (window_height-ball_radius*2)/2
        self.window.add(self.ball, x=self.ball.x, y=self.ball.y)

        # Default initial velocity for the ball
        self.fall_count = 0                                 # 計算墜落視窗外幾次
        # self.ball._dx = random.randint(1, MAX_X_SPEED)
        # self.ball._dy = INITIAL_Y_SPEED
        self.ball_dx = 0                                    # 球X速度
        self.ball_dy = 0                                    # 球Y速度

        # Initialize our mouse listeners
        onmouseclicked(self.click)
        onmousemoved(self.paddle_move)
        self.click_switch = 1                               # 點擊的開關(1=開,-1=關)

        # Draw bricks
        self.break_count = 0                                # 計算消除幾次磚塊
        self.brick_offset = brick_offset
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        for i in range(brick_cols):                                     # 直行(掌控x)
            for j in range(brick_rows):                                 # 橫列(掌控y)
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'black'
                if j <= 1:
                    self.brick.fill_color = 'red'
                if 1 < j <= 3:
                    self.brick.fill_color = 'orange'
                if 3 < j <= 5:
                    self.brick.fill_color = 'yellow'
                if 5 < j <= 7:
                    self.brick.fill_color = 'green'
                if 7 < j <= 9:
                    self.brick.fill_color = 'blue'
                self.brick.x = i*(brick_width+brick_spacing)               # 總共貼上i行
                self.brick.y = j*(brick_height+brick_spacing)              # 總共貼上j列
                self.window.add(self.brick, x=self.brick.x, y=self.brick.y+self.brick_offset)

    def click(self, e):
        if self.click_switch == 1:                                         # 開關開的時候可以執行onmouseclicked
            self.ball_dx = random.randint(1, MAX_X_SPEED)                  # 讓滑鼠點擊以後才開始有速度
            self.ball_dy = INITIAL_Y_SPEED
            self.click_switch = -1                                         # 點完以後就讓滑鼠點擊開關關起來
            if random.random() > 0.5:                                      # 球起始的時候，x隨機方向
                self.ball_dx = -self.ball_dx

    def get_dx(self):
        return self.ball_dx                                                # 讓breakout.py可以使用球x速度絕招

    def get_dy(self):                                                      # 讓breakout.py可以使用球y速度絕招
        return self.ball_dy

    def restart(self):                                                     # 讓球的速度重新歸零，停在起始點
        self.ball_dx = 0
        self.ball_dy = 0

    def reset_ball_position(self):                                         # 讓球重新回到起始點，把點擊的開關打開
        self.window.add(self.ball, x=(self.window.width-self.ball_radius*2)/2, y=(self.window.height-self.ball_radius*2)/2)
        self.click_switch = 1

    def paddle_move(self, m):
        self.paddle.x = m.x - self.paddle.width / 2      # 讓滑鼠移動時，paddle可以跟著滑鼠(這是變動的!! paddle.x還是指paddle左上角的座標)
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width-self.paddle.width

    def ball_bounce_wall(self):                          # 球與視窗反彈跟墜落視窗外的關係
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.ball_dx = -self.ball_dx
        if self.ball.y <= 0:
            self.ball_dy = -self.ball_dy
        if self.ball.y >= self.window.height:
            self.fall_count += 1                         # 計算墜落視窗外的次數

    def bounce_and_breakout(self):                       # 球反彈磚塊和板子，如果球的位子高於起始點的height,就可以消除掉物件
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            if self.ball.y <= (self.window.height-self.ball_radius*2)/2:
                maybe_brick = self.window.get_object_at(self.ball.x, self.ball.y)
                self.window.remove(maybe_brick)
                self.break_count += 1                    # 計算磚塊被消除的次數
            self.ball_dy = -self.ball_dy
        elif self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y) is not None:
            if self.ball.y <= (self.window.height-self.ball_radius*2)/2:
                maybe_brick = self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y)
                self.window.remove(maybe_brick)
                self.break_count += 1
            self.ball_dy = -self.ball_dy
        elif self.window.get_object_at(self.ball.x, self.ball.y+2*self.ball_radius) is not None:
            if self.ball.y <= (self.window.height-self.ball_radius*2)/2:
                maybe_brick = self.window.get_object_at(self.ball.x, self.ball.y+2*self.ball_radius)
                self.window.remove(maybe_brick)
                self.break_count += 1
            self.ball_dy = -self.ball_dy
        elif self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y+2*self.ball_radius) is not None:
            if self.ball.y <= (self.window.height-self.ball_radius*2)/2:
                maybe_brick = self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y+2*self.ball_radius)
                self.window.remove(maybe_brick)
                self.break_count += 1
            self.ball_dy = -self.ball_dy

    def leave_paddle(self):        # 把球的座標左上跟右上設為一組，左下跟右下設為一組，當一組碰到板子另一組沒有碰到板子時，強制讓球向上飄移一個高度，避免球重複反彈黏在板子上
        if self.window.get_object_at(self.ball.x, self.ball.y+2*self.ball_radius) is not None and self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y+2*self.ball_radius) is not None and self.window.get_object_at(self.ball.x, self.ball.y) is None and self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y) is None:
            self.ball.move(0, -10)
        if self.window.get_object_at(self.ball.x, self.ball.y+2*self.ball_radius) is None and self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y+2*self.ball_radius) is None and self.window.get_object_at(self.ball.x, self.ball.y) is not None and self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y) is not None:
            self.ball.move(0, -10)
































