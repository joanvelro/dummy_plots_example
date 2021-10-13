import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12})
from matplotlib import rc

rc('font', **{'family': 'serif', 'serif': ['Times New Roman']})

# create stationary demand
data = pd.DataFrame({})
y = []
for d in range(365):
    if d < 90:  # January-March
        mu = 50
        sd = 0.5
    if 90 <= d < 180:  # april-june
        mu = 60
        sd = 0.6
    if 180 <= d < 270:  # july-september
        mu = 30
        sd = 0.3
    if d >= 270:  # october-december
        mu = 80
        sd = 0.2
    y.append(np.random.normal(loc=mu, scale=sd))

data['variable'] = y
data['time'] = np.arange(0, 365) + 1

data['variable_2'] = np.random.beta(a=1, b=3, size=data.shape[0])


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        # except TypeError:
        #    print(f"{func.__name__} only takes numbers as the argument")
        except Exception as exception_msg:
            print('(!) Error in {}: {} '.format(func.__name__, str(exception_msg)))

    return inner_function


@exception_handler
def plot_timeseries(data, var_name):
    """
        *Plot histograms*
    """
    fig = plt.figure(figsize=(10, 4), dpi=150, facecolor='w', edgecolor='w')
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(data['time'],
             data[var_name],
             linewidth=2,
             linestyle='solid',
             color='k',
             label=var_name)
    ax1.set_ylabel(var_name)
    ax1.set_xlabel('Time')

    plt.grid(True)
    plt.legend()
    plt.show()
    plt.savefig('../../reports/figures/plot_timeseries.png', bbox_inches='tight', pad_inches=0)
    plt.close()


@exception_handler
def plot_pdf(x, pdf):
    """
        *Plot PDF*
    """
    fig = plt.figure(figsize=(10, 4), dpi=150, facecolor='w', edgecolor='w')
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(x,
             pdf,
             linewidth=2,
             linestyle='solid',
             color='k',
             label='PDF')
    ax1.set_ylabel('Density')
    ax1.set_xlabel('Variable')

    plt.grid(True)
    plt.legend()
    plt.show()
    plt.savefig('../../reports/figures/plot_pdf.png', bbox_inches='tight', pad_inches=0)
    plt.close()


def adjust_kernel(data):
    """
        *Fit a Kernel by Kernel Density Estimation Technique*
    """
    from sklearn.neighbors import KernelDensity
    h = 0.5
    kde = KernelDensity(bandwidth=h,
                        kernel='gaussian',  # ‘exponential’,gaussian
                        algorithm='kd_tree')
    kde.fit(data.values.reshape(-1, 1))
    # score_samples returns the log of the probability density
    x = np.linspace(min(data), max(data), 1000)
    # Evaluate the log density model on the data
    logdensity = kde.score_samples(x[:, None])
    density_estimated = np.exp(logdensity)

    return x, density_estimated


plot_timeseries(data, 'variable_2')
x, pdf_hat = adjust_kernel(data['variable_2'])
plot_pdf(x, pdf_hat)
