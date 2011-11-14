from math import sqrt
import sys, cv, os


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
	
    return hist

def isImg(x):
    name, ext = os.path.splitext(x)
    return ext == ".jpg" or ext == ".png"

if __name__ == '__main__':
    # getting paths
    files = os.listdir("near-sim/")
    print files
    files = filter(isImg, files)

    # make vector
    f = open("histvs.csv", "w")
    for file in files:
        h = calculate_hist("near-sim/%s" % file)
        
        l = []
        for hi in h:
            if hi != None:
                for j in range(256):
                    l.append(hi.bins[j])
        for d in l:
            f.write("%d, " % int(d))
        f.write("\n")
    f.close()
