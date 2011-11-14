from scikits.learn import svm, datasets
import numpy as np
import pylab as pl


iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
h = 0.02

svc    = svm.SVC(kernel="linear").fit(X, Y)
rbfsvc = svm.SVC(kernel="poly", degree=3).fit(X, Y)
nu_svc  = svm.NuSVC(kernel='linear').fit(X,Y)
lin_svc = svm.LinearSVC().fit(X, Y)

x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-1, X[:,1].max()+1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

titles = ["SVC with Linear Kernel", "SVC with Deg3 Poly Kernel",
          "NuSVC with Linear Kernel", "LinearSVC(linear kernel)"]

for i, clf in enumerate( (svc, rbfsvc, nu_svc, lin_svc) ):
    # Plot decision boundary
    pl.subplot(2, 2, i+1)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result
    Z = Z.reshape(xx.shape)
    pl.set_cmap(pl.cm.Paired)
    pl.contourf(xx, yy, Z)
    pl.axis('off')

    # Plot the training points
    pl.scatter(X[:,0], X[:,1], c=Y)
    pl.title( titles[i] )

pl.savefig("fig.png")
pl.show()
