import pytesseract
from PIL import Image
import cv2
import numpy as np

# 1. 載入圖片
image_path = 'lab13_2.png' # 請確保檔名與路徑正確
img = cv2.imread(image_path)

if img is None:
    print("錯誤：找不到圖片，請確認 lab13_2.png 是否已上傳至正確路徑")
else:
    # 2. 預處理
    # 轉為灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 關鍵修正：針對白底黑字，我們不應該使用 INV (反轉)
    # 或是使用 OTSU 自動計算閾值
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 3. 執行辨識 (將語言參數移至 lang，將輸入改為 thresh)
    # lang='chi_tra+eng' 
    # --psm 6 適合這種手寫排列
    custom_config = r'--oem 3 --psm 6'
    
    # 注意：傳入 thresh (處理後的圖)，並指定 lang
    text = pytesseract.image_to_string(thresh, lang='chi_tra+eng', config=custom_config)

    print("--- OCR 辨識結果 ---")
    if text.strip():
        print(text.strip())