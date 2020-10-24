    import numpy as np
    import math

    def gaussian(x, alpha, r):
          return 1./(math.sqrt(alpha**math.pi))*np.exp(-alpha*np.power((x - r), 2.))