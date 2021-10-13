#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    this script...
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 10})
from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Times New Roman']})


data = pd.read_csv('../../data/dummy_data.csv')


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
def plot_timeseries(data, var_1, var_2, var_3, var_4):
    """
        *Plot histograms*
    """
    fontsize = 12
    fig = plt.figure(figsize=(12, 8), dpi=150, facecolor='w', edgecolor='w')
    ax1 = fig.add_subplot(4, 1, 1)
    ax1.plot(data[var_1][0:100], linewidth=1, linestyle='dashed', color='c', label=var_1)
    ax1.set_ylabel('Variable')
    ax1.set_xlabel('Time')
    ax1.grid(True)
    ax1.legend()
    ax2 = fig.add_subplot(4, 1, 2)
    ax2.plot(data[var_2][0:100], linewidth=2, linestyle='dashdot', color='k', label=var_2)
    ax2.set_ylabel('Variable')
    ax2.set_xlabel('Time')
    ax2.grid(True)
    ax2.legend()
    ax3 = fig.add_subplot(4, 1, 3)
    ax3.plot(data[var_3][0:100], linewidth=1, linestyle='dotted', color='b', label=var_3)
    ax3.set_ylabel('Variable')
    ax3.set_xlabel('Time')
    ax3.grid(True)
    ax3.legend()
    ax4 = fig.add_subplot(4, 1, 4)
    ax4.plot(data[var_4][0:100], linewidth=2, linestyle='solid', color='gray', label=var_4)
    ax4.set_ylabel('Variable')
    ax4.set_xlabel('Time')
    ax4.grid(True)
    ax4.legend()

    plt.tick_params(axis='both', labelsize=fontsize)
    plt.show()
    plt.savefig('../../reports/figures/plot_timeseries.png', bbox_inches='tight', pad_inches=0)
    plt.close()


@exception_handler
def plot_histograms(data, var_1, var_2, var_3, var_4):
    """
        *Plot histograms*
    """
    fig, axes = plt.subplots(figsize=(12, 8), nrows=2, ncols=2, dpi=150, facecolor='w', edgecolor='w')
    n_bins = 10
    ax1 = axes[0, 0]
    ax1.hist(data[var_1], bins=n_bins, edgecolor='k', facecolor='b', density=True, cumulative=True, alpha=0.2)
    ax1.set_xlabel(var_1)
    ax1.set_ylabel('Prob.')
    ax1.set_title('Cumulative Distribution Function')
    ax2 = axes[1, 0]
    ax2.hist(data[var_2], bins=n_bins, edgecolor='k', facecolor='grey', density=False, cumulative=True, alpha=0.3)
    ax2.set_xlabel(var_2)
    ax2.set_ylabel('No. Observations')
    ax3 = axes[0, 1]
    ax3.hist(data[var_3], bins=n_bins, edgecolor='k', facecolor='c', density=False, cumulative=False, alpha=0.4)
    ax3.set_xlabel(var_3)
    ax3.set_ylabel('No. Observations')
    ax4 = axes[1, 1]
    ax4.hist(data[var_4], bins=n_bins, edgecolor='k', facecolor='g', density=False, cumulative=True, alpha=0.2)
    ax4.set_xlabel(var_4)
    ax4.set_ylabel('No. Observations')

    plt.subplots_adjust(wspace=0.2, hspace=0.4)
    plt.show()
    plt.savefig('../../reports/figures/plot_histograms.png', bbox_inches='tight', pad_inches=0)
    plt.close()


plot_timeseries(data, 'product_1', 'product_2', 'product_3', 'product_4')
plot_histograms(data, 'product_1', 'product_2', 'product_3', 'product_4')
