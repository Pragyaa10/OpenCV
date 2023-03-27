import cv2
path=r"""C:\Users\PRAGYA\Downloads"""
i_name="stickers.webp"
img=cv2.imread(path+'\\'+i_name)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destropAllWindows()