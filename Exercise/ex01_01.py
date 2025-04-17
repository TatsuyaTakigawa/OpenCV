import cv2
import numpy as np

img = np.zeros((480, 640)).astype(np.uint8)    # 画像を作成（8ビット（0～225）の二次元配列に0初期化）
cv2.imshow('src', img)                         # 画像をウィンドウに表示
cv2.waitKey(0)                                 # キー入力を待機（0は無限待機）任意のキーで閉じる
cv2.destroyAllWindows()                        # すべてのウィンドウを閉じる