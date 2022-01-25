from univariate_simulations import *
import matplotlib.pyplot as plt
import scipy.stats
#
# loc = 0.0002, shape = 0.015, df = 4.5


def walk_vs_walk(start, simulations, steps, t_params, n_params):
    n1 = np.zeros(simulations)
    t1 = np.zeros(simulations)
    for i in range(simulations):
        choice = random.choice([1, 2])
        n = normal_random_walk(start=start, steps=steps, loc=n_params[0], shape=n_params[1])
        t = t_random_walk(start=start, steps=steps, loc=t_params[0], df=t_params[1], shape=t_params[2])
        if choice == 1:
            plt.plot(n[1], color='blue')
            plt.plot(t[1], color='green')
        else:
            plt.plot(t[1], color='green')
            plt.plot(n[1], color='blue')
        n1[i] = n[0][-1]
        t1[i] = t[0][-1]
    plt.show()

plt.hist(n1, bins=30)
# plt.title('Normal RW')
# plt.show()
plt.hist(t1, bins=30)
plt.title('T RW')
plt.show()

print(scipy.stats.jarque_bera(n1), '    Norm')
print(scipy.stats.jarque_bera(t1), '    T')
