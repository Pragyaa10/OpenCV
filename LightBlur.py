import cv2
import numpy as np
img_path=r"C:\Users\PRAGYA\Downloads\stickers.webp"
img=cv2.imread(img_path)
img=cv2.resize(img,(500,500))
img_blur=cv2.blur(img,(3,3))
cv2.imshow("Gray image",img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()