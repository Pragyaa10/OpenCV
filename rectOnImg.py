import cv2
import numpy as np
img_path=r"C:\Users\PRAGYA\Downloads\stickers.webp"
img=cv2.imread(img_path)
img=cv2.resize(img,(500,500))
p1=(30,30)
p2=(470,470)
color=(0,255,0)
thickness=1
lineType=cv2.LINE_4
img_rect=cv2.rectangle(img,p1,p2,color,thickness,lineType)
cv2.imshow("Text image",img_rect)
cv2.waitKey(0)
cv2.destroyAllWindows()