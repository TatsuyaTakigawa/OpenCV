import cv2

# 画像ファイルのリストを作成（images/People/People_walking_0.png ～ People_walking_6.png）
file_src_list = [f'images/People/People_walking_{i}.png' for i in range(7)]

# 最初に表示する画像のインデックス
index = 0

# 表示用ウィンドウを1回だけ作成（毎回作らずに済む）
cv2.namedWindow('src')

# 無限ループで画像を順番に表示（アニメーション風）
while True:
    # 現在の画像ファイル名を取得
    file_src = file_src_list[index]

    # カラー画像として読み込む
    img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)

    # 画像が読み込めなかった場合は警告を表示してスキップ
    if img_src is None:
        print(f"画像が見つかりません: {file_src}")
    else:
        # 読み込んだ画像をウィンドウに表示
        cv2.imshow('src', img_src)

    # キー入力を1秒（1000ミリ秒）待つ
    key = cv2.waitKey(1000)

    # 'q'キーまたはESCキーが押されたらループを終了
    if key == ord('q') or key == 27:
        break

    # 次の画像へ（最後まで表示したら最初の画像に戻る）
    index = (index + 1) % len(file_src_list)

# すべてのウィンドウを閉じる
cv2.destroyAllWindows()
