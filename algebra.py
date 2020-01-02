import numpy as np
from symfit import Variable, Parameter, Fit, Model, sqrt
import matplotlib.pyplot as plt

t_data = np.array([1.4, 2.1, 2.6, 3.0, 3.3])
h_data = np.array([10, 20, 30, 40, 50])

h = Variable('h')
t = Variable('t')
g = Parameter('g')

t_model = Model({t: sqrt(2 * h / g)})

fit = Fit(t_model, h=h_data, t=t_data)
fit_result = fit.execute()
print(fit_result)

plt.plot(h_data, t_data)
plt.show()