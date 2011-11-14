from scikits.learn import mixture
import numpy as np
import pylab as pl

n_samples = 300

# generate random data
np.random.seed(0)
C = np.array( [[0.0, -0.7], [3.5, 0.7]] )
Xtrain = np.r_[np.dot(np.random.randn(n_samples, 2), C),
               np.random.randn(n_samples, 2) + np.array([20,20])]
clf = mixture.GMM(n_states=2, cvtype="full")
clf.fit(Xtrain)

x = np.linspace(-20.0, 30.0)
y = np.linspace(-30.0, 40.0)
X, Y = np.meshgrid(x, y)
XX = np.c_[X.ravel(), Y.ravel()]
Z = np.log(-clf.eval(XX)[0])
Z = Z.reshape(X.shape)
CS = pl.contour(X, Y, Z)
CB = pl.colorbar(CS, shrink=0.8, extend='both')
pl.scatter(Xtrain[:,0], Xtrain[:,1], 0.8)
pl.axis('tight')
pl.savefig("GMM.png")
pl.show()
