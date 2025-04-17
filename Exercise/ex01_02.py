import cv2

# カラー画像を読み込んで表示
file_src = 'images/lena.jpg'  # 画像ファイルのパス
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)

if img_src is not None:
    cv2.namedWindow('src')                 # ウィンドウを作成
    cv2.imshow('src', img_src)             # 読み込んだ画像を表示
    cv2.waitKey(0)                         # キー入力を待機
    cv2.destroyAllWindows()                # すべてのウィンドウを閉じる
else:
    print(f"Error: ファイル '{file_src}' が見つかりません。")  # エラー表示