import sys, cv

if __name__ == '__main__':

	# Loag Image from args.
	if len(sys.argv) < 2: sys.exit(-1)
	src = cv.LoadImage(sys.argv[1], cv.CV_LOAD_IMAGE_COLOR)
	if not src: sys.exit(-1)
	
	# Prepare each channel
	sch = src.channels
	dst = [None, None, None, None]
	for i in range(sch):
		dst[i] = cv.CreateImage((src.width, src.height), src.depth, 1)
		
	# Prepare histogram
	chwidth = 260
	size = 256
	ranges = [(0,255)]
	hist = cv.CreateHist([size], cv.CV_HIST_ARRAY, ranges)
	histimg = cv.CreateImage((chwidth * sch, 200), 8, 1)
	
	# split image into each color
	if sch == 1: cv.Copy(src, dst[0])
	else: cv.Split(src, dst[0], dst[1], dst[2], dst[3])
	
	# calculate histogram
	cv.Set(histimg, cv.ScalarAll(255))
	for i in range(sch):
		# acutual calc.
		cv.CalcHist([dst[i]], hist)
		min_v, max_v, _, _ = cv.GetMinMaxHistValue(hist)
		cv.Scale(hist.bins, hist.bins, float(histimg.height)/max_v, 0)
		
		# drawing
		binw = cv.Round(float(chwidth) / size)
		for j in range(size):
			p1 = (j*binw+(i*chwidth), histimg.height)
			p2 = ((j+1)*binw+(i*chwidth), histimg.height-cv.Round(cv.GetReal1D(hist.bins,j)))
			cv.Rectangle(histimg, p1, p2, cv.ScalarAll(0), -1, 8, 0)						 

	# save hist image
	cv.SaveImage('hist_img.png', histimg)
						 
						 
						 





	
