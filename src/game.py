import random
import tkinter
import time

# 定数
WINDOW_SIZE = (640, 480)
BOX_SIZE = 10
REFRESH = 30

#主人公ブロック
##初期座標
box = [320,420]#左端、上端
##ブロックサイズ
box_SIZE = 10
##タグ
box_TAG = "Block"
##動作回数
rotation = 0
#ゲームオーバーフラグ
gameover_flg = False
welldone_flg = False
#当たり判定フラグ
hit_flg = False
under_flg = False
#ブロック
x_posi=box[0]
class Block:
    global box,WINDOW_SIZE,hit_flg,x_posi,y_posi
    def __init__(self, left, up, color, tag):
        self.x_position = left
        self.y_position = up
        self.color = color
        self.tag =  tag
    def block_reset(self):#初期化
        box[0] = self.x_position
        box[1] = self.y_position
    def repaint_box(self):
        canvas.delete(self.tag)
        canvas.create_oval(self.x_position + box_SIZE, self.y_position, self.x_position, self.y_position + box_SIZE, fill=self.color, tag=self.tag)
    def move(self,direction):
        if direction == "Left":
            if self.x_position > 0:
                self.x_position -= box_SIZE
                bl.repaint_box()
                return self.x_position
        else:
            if self.x_position<WINDOW_SIZE[0]-10:
                self.x_position += box_SIZE
                bl.repaint_box()
class hit(Block):#当たり判定処理
    global box, hit_flg, enemy_x, enemy_y
    def __init__(self):
        self.left = 0
        self.right = WINDOW_SIZE[0]
        self.up = 0
        self.down = WINDOW_SIZE[1]
    def hit(self):
        global hit_flg,gameover_flg
        for i in range(c_max):
            if bl.x_position == enemy_x[i]:
                if bl.y_position == enemy_y[i]:
                    gameover_flg = True
                    return gameover_flg
    def under(self):
        global under_flg, WINDOW_SIZE
        if min(enemy_y) >= WINDOW_SIZE[1]:
            under_flg = True
        return under_flg
bl = Block(box[0],box[1],"gold",box_TAG)
ht = hit()

c = 0#敵の初期値
v = 1
enemy_x=[]
enemy_y=[]
enemy_flg = False
def enemy():#敵ブロックの生成
    global c,c_max,enemy_x,enemy_flg
    c_max = int(20**v)#敵の上限数
    #出現位置
    enemy_box = [0,0]#X座標とY座標
    enemy_box[0] = random.randrange(0,WINDOW_SIZE[0],10)
    if c < c_max:#座標取得
        enemy_x.append(enemy_box[0])
        enemy_y.append(enemy_box[1])
    if c < c_max:
        #タグ付け
        enemy_tag = "enemy" + str(c)
        #ブロック生成
        enemy_bl = Block(enemy_box[0],enemy_box[1],"white", enemy_tag)
        enemy_bl.repaint_box()
        canvas.create_text(320, 200, fill="white", tag="ready", text='READY?', font =("FixedSys", 50))

        c += 1
    if c == c_max:
        enemy_flg = True

def enemy_fall():#落下処理
    global enemy_x,enemy_y
    time.sleep(REFRESH/1000)
    for i in range(c_max):
        enemy_y[i] += random.randrange(0,30,10)
        enemy_bl = Block(enemy_x[i],enemy_y[i],"white", "enemy"+str(i))
        enemy_bl.repaint_box()
        ht.hit()

def gameover():#ゲームオーバー処理
    if gameover_flg == True:
        if welldone_flg == True:
            canvas.delete("ready")
            canvas.create_text(320, 200, fill="black", tag="WELLDONE", text='Congratulations!', font =("FixedSys", 50))
        else:
            canvas.delete("ready")
            canvas.create_text(320, 200, fill="black", tag="GAMEOVER", text='GAME OVER', font =("FixedSys", 50))

window = tkinter.Tk() # window の初期化
window.resizable(width=False, height=False) # window のサイズを変更できないように
canvas = tkinter.Canvas(window, width=WINDOW_SIZE[0], height=WINDOW_SIZE[1]) # windows上に絵を書く場所を作る
canvas.create_rectangle(0, 0, WINDOW_SIZE[0], WINDOW_SIZE[1], fill="#FF1493") # windows上にWINDOW_SIZE[0]xWINDOW_SIZE[1]の黒い四角を書く
canvas.pack()

def reset():#初期化
    global enemy_flg, under_flg, v, c, enemy_y, enemy_x, rotation, gameover_flg,welldone_flg
    enemy_flg = False
    under_flg = False
    enemy_y = []
    enemy_x = []
    c = 0
    v += 0.5
    if rotation == 2:
        welldone_flg = True
        gameover_flg = True
        gameover()
    rotation += 1

def game_loop():#ゲームマネージメント
    if gameover_flg == False:
        bl.repaint_box()
        enemy()
        ht.under()
        if enemy_flg == True:
            canvas.delete("ready")
            enemy_fall()
        if under_flg == True:
            reset()
        if hit_flg == True:
            gameover()
        window.after(REFRESH,game_loop)
    else:
        gameover()

# キーボードが押された時
def key_move(event):
    if event.keysym == "Left":
        bl.move(direction="Left")
    elif event.keysym == "Right":
        bl.move(direction="Right")
# イベントの関連付け
window.bind("<Key>", key_move) # キーボードのキーが押されたら
# 実行
game_loop() # ゲームの計算を一定のタイミングで行う
window.mainloop() # 画面表示を続ける
