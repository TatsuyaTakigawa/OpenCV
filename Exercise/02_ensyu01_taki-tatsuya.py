import cv2

# 画像ファイルのリストを作成（images/n0.jpg ～ images/n9.jpg）
file_src_list = [f'images/n{i}.jpg' for i in range(10)]

index = 0  # 現在表示している画像のインデックス

while True:
    # 現在の画像ファイルを取得
    file_src = file_src_list[index]

    # カラー画像を読み込む
    img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)

    # 画像が読み込めなかった場合はスキップして次へ
    if img_src is None:
        print(f"画像が見つかりません: {file_src}")
        index = (index + 1) % len(file_src_list)  # インデックスを1進めてループ
        continue

    # ウィンドウを作成して画像を表示
    cv2.namedWindow('src')       # 表示用ウィンドウ（毎回作り直される）
    cv2.imshow('src', img_src)   # 画像を表示

    while True:
        # キー入力を待機（無限に待つ）
        key = cv2.waitKey(0)

        if key == ord('n'):  # 'n' キーが押されたら次の画像へ
            index = (index + 1) % len(file_src_list)  # インデックスを1進めてループ（0〜9でループ）
            break  # 外側のループに戻る
        elif key == ord('q') or key == 27:  # 'q' キーまたは ESC キーが押されたら終了
            cv2.destroyAllWindows()  # 全ウィンドウを閉じる
            exit()  # プログラム終了
