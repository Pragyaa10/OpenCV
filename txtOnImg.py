import cv2
import numpy as np
img_path=r"C:\Users\PRAGYA\Downloads\stickers.webp"
img=cv2.imread(img_path)
img=cv2.resize(img,(500,500))
text="GitHub Stickers"
org=(30,30)
font=cv2.FONT_HERSHEY_DUPLEX
fontScale=0.5
color=(0,0,0)
thickness=1
lineType=cv2.LINE_AA
bottomLeftOrigin=False
img_txt=cv2.putText(img,text,org,font,fontScale,color,thickness,lineType,bottomLeftOrigin)
cv2.imshow("Text image",img_txt)
cv2.waitKey(0)
cv2.destroyAllWindows()