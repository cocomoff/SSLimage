import cv


img = cv.LoadImageM('sink.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)
image = cv.GetImage(img)
hist = cv.CreateHist([256], cv.CV_HIST_ARRAY, [(0,255)])
cv.CalcHist([image], hist, 0, None)
a = hist.bins

for i in range(256):
	print "a[%d] = %d" % (i, a[i]) 
