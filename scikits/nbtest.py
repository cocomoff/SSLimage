import numpy as np
from scikits.learn.naive_bayes import GNB

X = np.array( [[-1,-1], [-2,-1], [-3,-2], [1,1], [2,1], [3,2]] )
Y = np.array( [1,1,1,2,2,2] )

clf = GNB()
clf.fit(X, Y)
print clf.predict([[-0.8, -1]])
