import random
import time
import tkinter


class Snowball:
    def __init__(self, canvas, window_size):
        # ゲーム内の設定
        self.canvas = canvas  # canvasの情報
        self.x_window_size = window_size[0]  # ウィンドウの横幅
        self.y_window_size = window_size[1]  # ウィンドウの縦幅

        self._OBJECT_SIZE = 10  # 玉のサイズ
        self.my_x_position = 320  # 黄色玉(自分)のX座標
        self.my_y_position = 420  # 黄色玉(自分)のY座標
        self._MY_COLOR = "gold"  # 黄色玉(自分)の色
        self._MY_NAME = "me"  # 黄色玉(自分)の名前
        self._ENEMY_NMAE = "enemy"  # 白玉(敵)の名前
        self._ENEMY_COLOR = "white" # 白玉(敵)の色

        self.generate_enemy()  # 敵の生成

    def repaint_object(self, name,color, x_position, move_x_amount, y_position, move_y_amount):
        """
        黄色玉(自分)の描画
        :return:
        """
        self.canvas.delete(name)
        self.canvas.create_oval(
            x_position + move_x_amount,
            y_position,
            x_position,
            y_position + move_y_amount,
            fill=color,
            tag=name,
        )

    def paint_me(self):
        """
        黄色玉(自分)の描画
        :return:
        """
        self.repaint_object(
            self._MY_NAME,
            self._MY_COLOR,
            self.my_x_position,
            self._OBJECT_SIZE,
            self.my_y_position,
            self._OBJECT_SIZE,
                )

    def input_key(self, event):
        """
        キーボードが押された時
        :param event:
        :return:
        """
        if event.keysym == "Left":
            self.move_left_right(direction="Left")
        elif event.keysym == "Right":
            self.move_left_right(direction="Right")

    def move_left_right(self, direction):
        """
        黄色玉(自分)の移動処理
        :param direction:
        :return:
        """
        if direction == "Left":
            if self.my_x_position > 0:
                self.my_x_position -= self._OBJECT_SIZE
                self.repaint_object()
        elif direction == "Right":
            if self.my_x_position < WINDOW_SIZE[0] - 10:
                self.my_x_position += self._OBJECT_SIZE
                self.repaint_object()

    def is_hitted(self):
        """
        黄色玉が白玉に敵に当たったかどうか
        :return:
        """
        for i in range(c_max):
            if bl.me_x_position == enemy_x[i]:
                if bl.my_y_position == enemy_y[i]:
                    gameover_flg = True
                    return gameover_flg

    def is_arrived_in_window_bottom(self):
        """
        白玉が画面下に敵が到達したかどうか
        :return:
        """
        if min(enemy_y) >= self.y_window_size:
            return True
        return False

    def generate_enemy(self):  # 敵ブロックの生成
        """
        白玉(敵)の生成
        :return:
        """
        self.canvas.create_text(
            320, 200, fill="white", tag="ready", text="READY?", font=("FixedSys", 50)
        )
        global c, c_max, enemy_x, enemy_flg
        c_max = int(20**v)  # 敵の上限数
        # 出現位置
        enemy_box = [0, 0]  # X座標とY座標
        enemy_box[0] = random.randrange(0, WINDOW_SIZE[0], 10)
        if c < c_max:  # 座標取得
            enemy_x.append(enemy_box[0])
            enemy_y.append(enemy_box[1])
        if c < c_max:
            # タグ付け
            enemy_tag = "enemy" + str(c)
            # ブロック生成
            enemy_bl = Snowball(enemy_box[0], enemy_box[1], "white", enemy_tag)
            enemy_bl.repaint_object()

            c += 1
        if c == c_max:
            enemy_flg = True

        self.canvas.delete("ready")

    def enemy_fall(self):
        """
        白玉(敵)の落下処理
        :return:
        """
        global enemy_x, enemy_y
        time.sleep(REFRESH / 1000)
        for i in range(c_max):
            enemy_y[i] += random.randrange(0, 30, 10)
            enemy_bl = Snowball(enemy_x[i], enemy_y[i], "white", "enemy" + str(i))
            enemy_bl.repaint_object()
            ht.is_hitted()

    def reset_game(self):
        """
        ゲームの初期化
        :return:
        """
        self.canvas.delete("enemy")
        self.canvas.delete("me")
        self.canvas.delete("gameover")
        self.canvas.delete("completed")
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

    def game_over(self):  # ゲームオーバー処理
        """
        ゲームオーバー処理
        :return:
        """
        self.canvas.create_text(
            320,
            200,
            fill="black",
            tag="gameover",
            text="GAME OVER",
            font=("FixedSys", 50),
        )

    def game_completed(self):
        self.canvas.create_text(
            320,
            200,
            fill="black",
            tag="completed",
            text="Congratulations!",
            font=("FixedSys", 50),
        )


# 当たり判定フラグ
hit_flg = False
under_flg = False
# ブロック
x_posi = box[0]


c = 0  # 敵の初期値
v = 1
enemy_x = []
enemy_y = []
enemy_flg = False


class GameManager:
    """
    ゲームの管理/運用を行うクラス
    """

    def __init__(self):
        # windowの設定
        WINDOW_SIZE = (
            640,
            480,
        )  # ウィンドウサイズ
        REFRESH = 30  # 更新頻度(ミリ秒)

        self.window = tkinter.Tk()  # window の初期化
        self.window.resizable(width=False, height=False)  # window のサイズを変更できないようにする
        self.canvas = tkinter.Canvas(
            self.window, width=WINDOW_SIZE[0], height=WINDOW_SIZE[1]
        )  # windows上に絵を書く場所を作る
        self.canvas.create_rectangle(
            0, 0, WINDOW_SIZE[0], WINDOW_SIZE[1], fill="#FF1493"
        )  # windows上にWINDOW_SIZE[0]xWINDOW_SIZE[1]の黒い四角を書く
        self.canvas.pack()  # canvasをウィンドウに貼り付ける

        self.snowball = Snowball(self.canvas, WINDOW_SIZE)
        self.game_status = 0  #  0:ゲーム中 1:ゲームオーバー 2:ゲームクリア
        self.number_of_games = 0  # ゲームの回数

        self.window.bind(
            "<Key>", self.snowball.input_key
        )  # キーボードのキーが押されたらkey_move関数をコール
        self.window.after(REFRESH, self.loop)  # 30ミリ秒後にloop関数をコール

    def start(self):
        self.window.mainloop()

    def loop(self):
        if self.game_status == 0:  # ゲーム中
            self.snowball.repaint_object()
            self.snowball.enemy_fall()
            if self.snowball.is_hitted():
                self.game_status = 1
                return
            self.snowball.is_arrived_in_window_bottom()

        if self.game_status == 1:  # ゲームオーバー
            self.snowball.game_over()
        if self.game_status == 2:  # ゲームクリア
            self.snowball.game_completed()


if __name__ == "__main__":
    game = GameManager()
    game.start()
