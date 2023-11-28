from random import randrange
from time import sleep
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
        self._ENEMY_NAME = "enemy"  # 白玉(敵)の名前
        self._ENEMY_COLOR = "white"  # 白玉(敵)の色
        self._MAXIMUM_ENEMIES = 20  # 白玉(敵)の最大数

        self.enemy_information = []  # 敵の情報

    def repaint_object(
        self, name, color, x_position, move_x_amount, y_position, move_y_amount
    ):
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
            name=self._MY_NAME,
            color=self._MY_COLOR,
            x_position=self.my_x_position,
            move_x_amount=self._OBJECT_SIZE,
            y_position=self.my_y_position,
            move_y_amount=self._OBJECT_SIZE,
        )
        self.canvas.update()

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
                self.paint_me()
        elif direction == "Right":
            if self.my_x_position < self.x_window_size - self._OBJECT_SIZE:
                self.my_x_position += self._OBJECT_SIZE
                self.paint_me()

    def is_hit(self):
        """
        黄色玉が白玉に敵に当たったかどうか
        :return:
        """
        for enemy in self.enemy_information:
            if self.my_x_position == enemy["position_x"]:
                if self.my_y_position == enemy["position_y"]:
                    return True
        return False

    def is_arrived_in_window_bottom(self):
        """
        白玉が画面下に敵が到達したかどうか
        :return:
        """
        for enemy in self.enemy_information:
            if enemy["position_y"] >= self.y_window_size:
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
        for enemy_number in range(self._MAXIMUM_ENEMIES):
            self.enemy_information.append(
                {
                    "position_x": randrange(
                        0, self.x_window_size, self._OBJECT_SIZE
                    ),  # 出現位置x
                    "position_y": 0,  # 出現位置y
                    "color": self._ENEMY_COLOR,  # 色
                    "name": self._ENEMY_NAME + str(enemy_number),  # 名前
                }
            )
        for enemy in self.enemy_information:
            sleep(0.05)
            self.repaint_object(
                name=enemy["name"],
                color=enemy["color"],
                x_position=enemy["position_x"],
                move_x_amount=self._OBJECT_SIZE,
                y_position=enemy["position_y"],
                move_y_amount=self._OBJECT_SIZE,
            )
            self.canvas.update()
        self.canvas.delete("ready")

    def fall(self):
        """
        白玉(敵)の落下処理
        :return:
        """
        for enemy in self.enemy_information:
            enemy["position_y"] += self._OBJECT_SIZE
            self.repaint_object(
                name=enemy["name"],
                color=enemy["color"],
                x_position=enemy["position_x"],
                move_x_amount=self._OBJECT_SIZE,
                y_position=enemy["position_y"],
                move_y_amount=self._OBJECT_SIZE,
            )
        self.canvas.update()

    def reset_game(self):
        """
        ゲームの初期化
        :return:
        """
        for enemy in self.enemy_information:
            self.canvas.delete(enemy["name"])
        self.enemy_information = []
        self._MAXIMUM_ENEMIES *= 2

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
        self.REFRESH = 30  # 更新頻度(ミリ秒)

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
        self.game_status = 0  #  1:スタンバイ中、2:ゲーム中 3:ゲームオーバー 4:ゲームクリア
        self.number_of_games = 0  # ゲームの回数

        self.window.bind(
            "<Key>", self.snowball.input_key
        )  # キーボードのキーが押されたらkey_move関数をコール

    def start(self):
        self.loop()
        self.window.mainloop()

    def loop(self):
        if self.game_status == 0:  # 初期状態
            self.game_status = 1
            self.window.after(self.REFRESH, self.loop)  # 30ミリ秒後にloop関数をコール
            return
        if self.game_status == 1:  # スタンバイ中
            self.snowball.paint_me()
            self.snowball.generate_enemy()
            self.game_status = 2
        if self.game_status == 2:  # ゲーム中
            self.snowball.fall()
            if self.snowball.is_hit():
                self.game_status = 3
            if self.snowball.is_arrived_in_window_bottom():
                self.number_of_games += 1
                self.snowball.reset_game()
                if self.number_of_games < 3:
                    self.snowball.generate_enemy()
            if self.number_of_games == 3:
                self.game_status = 4
        if self.game_status == 3:  # ゲームオーバー
            self.snowball.game_over()
        if self.game_status == 4:  # ゲームクリア
            self.snowball.game_completed()
        self.window.after(self.REFRESH, self.loop)  # 30ミリ秒後にloop関数をコール


if __name__ == "__main__":
    game = GameManager()
    game.start()
