import irispy
import numpy as np

p2 = irispy.Polyhedron()
p2.setA(np.eye(2))
p2.setB(np.array([3.0, 4.0]))
print p2.contains(np.array([2.5, 5.5]), 0.0)
p2.printGenerators()

p3 = irispy.Polyhedron.fromBounds([-1,-1], [2,2])
p3.printGenerators()

problem = irispy.IRISProblem(2)
problem.setBounds(irispy.Polyhedron.fromBounds([-1,-1], [2,2]))
problem.setSeedPoint(np.array([0.0, 0.0]))
problem.addObstacle(np.array([[1.5, 2], [1.5, 2]]))
region = irispy.inflate_region(problem, irispy.IRISOptions())
print region
print region.getPolyhedron().generatorPoints()
print region.getEllipsoid().getC()
print region.getEllipsoid().getD()

import matplotlib.pyplot as plt
region.polyhedron.draw2d()
region.ellipsoid.draw2d()
plt.gca().set_xlim([-1.5, 2.5])
plt.gca().set_ylim([-1.5, 2.5])
plt.show()