import cv

img  = cv.LoadImageM("sink.jpg")
dst = cv.CreateImage(cv.GetSize(img), cv.IPL_DEPTH_16S, 3)
laplace = cv.Laplace(img, dst)
cv.SaveImage("sink-lpc.png", dst)

