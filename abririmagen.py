import cv2
import cv2 as cv


img = cv.imread('vasos.jpg', 1)

cv2.imshow('titulo de la ventana donde se va abirir la imagen', img) #se muestra la imagen


cv2.waitKey(0)
cv2.destroyAllWindows()