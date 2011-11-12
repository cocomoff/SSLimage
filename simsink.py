import os, cv, math, sys

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

def chdiff(hs1, hs2):
	# compare hists
	diff = 0.0
	for i in range(len(hs1)):
		if hs1[i] != None and hs2[i] != None:
			comp = cv.CompareHist(hs1[i], hs2[i], cv.CV_COMP_BHATTACHARYYA)
			diff += comp ** 2.0
	return math.sqrt(diff)

if __name__ == '__main__':
	# Loag Image from args.
	if len(sys.argv) < 2: sys.exit(-1)
	fname = sys.argv[1]
	hs0 = calculate_hist(fname)	

	# search most nearest photo
	# temporarly file list
	flists = os.listdir('/home/cocomoff/python/Photo_samples/')
	files = len(flists)

	diffs = []
	for i in range(files):
		hsi = calculate_hist("/home/cocomoff/python/Photo_samples/%s" % flists[i])
		diff = chdiff(hs0, hsi)
		print 'With %3d - %f' % (i, diff)
		diffs.append( (diff, i) )
	
	# sort 
	diffs.sort()
	
	# Top 10
	for i in range(10):
		d, index = diffs[i]
		fname = "/home/cocomoff/python/Photo_samples/%s" % flists[index]

		# print filename
		img = cv.LoadImageM(fname, cv.CV_LOAD_IMAGE_COLOR)
		print "index %d, name %s | %d" % (index, flists[index], img.width)	

		# save with name
		oname = "%s-sim-%d.png" % (flists[index], index)
		print oname
		cv.SaveImage(oname, img)


