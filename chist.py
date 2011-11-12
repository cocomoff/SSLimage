import math, sys, cv


def calculate_hist(filename):
	src = cv.LoadImage(filename, cv.CV_LOAD_IMAGE_COLOR)
	if not src: sys.exit(-1)
	
	# Prepare each channel
	sch = src.channels
	dst = [None, None, None, None]
	for i in range(sch):
		dst[i] = cv.CreateImage((src.width, src.height), src.depth, 1)
		
	# Prepare histogram
	size = 256
	ranges = [(0,255)]
	hist = [None, None, None, None]
	for i in range(sch):
		hist[i] = cv.CreateHist([size], cv.CV_HIST_ARRAY, ranges) 
		
	# split image into each color
	if sch == 1: cv.Copy(src, dst[0])
	else:        cv.Split(src, dst[0], dst[1], dst[2], dst[3])
	
	# calc hist
	for i in range(sch): cv.CalcHist([dst[i]], hist[i])
	# for i in range(sch): print hist[i].bins
	
	return hist


def hist_to_file(hist, filename):
	bin = hist.bins
	f = open(filename, 'w')
	for i in range(256):
		f.write("%d, %d\n" % (i, bin[i]))

if __name__ == '__main__':

	# Loag Image from args.
	if len(sys.argv) < 3: sys.exit(-1)
	filename1 = sys.argv[1]
	filename2 = sys.argv[2]

	hs1 = calculate_hist(filename1)
	hs2 = calculate_hist(filename2)
	
	for i in range(len(hs1)):
		if hs1[i] != None: hist_to_file(hs1[i], "%s-%d.csv" % (filename1, i))
		if hs2[i] != None: hist_to_file(hs2[i], "%s-%d.csv" % (filename2, i))
		
	# compare hists
	diff = 0.0
	for i in range(len(hs1)):
		if hs1[i] != None and hs2[i] != None:
			comp = cv.CompareHist(hs1[i], hs2[i], cv.CV_COMP_BHATTACHARYYA)
			diff += comp ** 2.0
	
	# distance
	print "%f" % (math.sqrt(diff))
	
