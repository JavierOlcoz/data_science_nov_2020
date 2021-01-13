import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


def plot_graphs(to_plot, title_1):
    """ Used to plot similar graphs
        Args: column to plot, title
    """ 
    plt.plot(to_plot)
    plt.title(title_1)
    plt.xlabel('LATITUDE(º)')
    plt.ylabel('TEMPERATURE(ºC)')
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    plt.grid()
    plt.legend()
    plt.xticks([90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90])
    return plt.show()


def plot_std(to_plot, title_1):
    """ Used to plot similar graphs
        Args: column to plot, title
    """ 
    plt.plot(to_plot)
    plt.title(title_1)
    plt.xlabel('LATITUDE(º)')
    plt.ylabel('TEMPERATURE(ºC)')
    plt.axvline(x=0, color='black')
    plt.grid()
    plt.xticks([90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90])
    return plt.show()


def plot_graphs_sns(dataset, y_1, title_1):
    """ Used to plot similar graphs
        Args: column to plot, title
    """ 
    sns.relplot(data=dataset, kind='line', x=dataset.index, y=y_1)
    plt.title(title_1)
    plt.xlabel('LATITUDE(º)')
    plt.ylabel('TEMPERATURE(ºC)')
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    plt.grid()
    plt.xticks([90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90])
    return plt.show()


def plot_std_sns(dataset, y_1, title_1):
    """ Used to plot similar graphs
        Args: column to plot, title
    """ 
    sns.relplot(data=dataset, kind='line', x=dataset.index, y=y_1)
    plt.title(title_1)
    plt.xlabel('LATITUDE(º)')
    plt.ylabel('TEMPERATURE(ºC)')
    plt.axvline(x=0, color='black')
    plt.grid()
    plt.xticks([90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90])
    return plt.show()


def plot_graphs_months(to_plot_1, to_plot_2, to_plot_3, to_plot_4, to_plot_5, to_plot_6, to_plot_7, to_plot_8, 
to_plot_9, to_plot_10, to_plot_11, to_plot_12, title_1, label_1, label_2, label_3, label_4, label_5, label_6, 
label_7, label_8, label_9, label_10, label_11, label_12):
    """ Used to plot similar graphs
        Args: 12 differents columns to plot, title and the labels for each plot
    """ 
    plt.plot(to_plot_1, label=label_1)
    plt.plot(to_plot_2, label=label_2)
    plt.plot(to_plot_3, label=label_3)
    plt.plot(to_plot_4, label=label_4)
    plt.plot(to_plot_5, label=label_5)
    plt.plot(to_plot_6, label=label_6)
    plt.plot(to_plot_7, label=label_7)
    plt.plot(to_plot_8, label=label_8)
    plt.plot(to_plot_9, label=label_9)
    plt.plot(to_plot_10, label=label_10)
    plt.plot(to_plot_11, label=label_11)
    plt.plot(to_plot_12, label=label_12)
    
    plt.title(title_1)
    plt.xlabel('LATITUDE(º)')
    plt.ylabel('TEMPERATURE(ºC)')
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    plt.grid()
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
    plt.xticks([90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90])
    return plt.show()


def correlation_matrix_all_rows(dataset, title_1):
    """ Plot the correlation matrix
        Args: dataset, title
    """
    x = dataset.iloc[:,240:]
    plt.title(title_1)
    x1 = x.corr()
    sns.heatmap(x1, cmap="BrBG", annot=True)
    return plt.show()

def correlation_matrix_north_hemisphere(dataset, title_1):
    """ Plot the correlation matrix
        Args: dataset, title
    """
    z = dataset.iloc[:836,240:]
    plt.title(title_1)
    z1 = z.corr()
    sns.heatmap(z1, cmap="BrBG", annot=True)
    return plt.show()

def correlation_matrix_south_hemisphere(dataset, title_1):
    """ Plot the correlation matrix
        Args: dataset, title
    """
    z = dataset.iloc[836:,240:]
    plt.title(title_1)
    z1 = z.corr()
    sns.heatmap(z1, cmap="BrBG", annot=True)
    return plt.show()

def correlation_matrix_hot(dataset, title_1):
    """ Plot the correlation matrix
        Args: dataset, title
    """
    z = dataset.iloc[599:1071,240:]
    plt.title(title_1)
    z1 = z.corr()
    sns.heatmap(z1, cmap="BrBG", annot=True)
    return plt.show()

def correlation_matrix_cold(dataset, title_1):
    """ Plot the correlation matrix
        Args: dataset, title
    """
    a = dataset.iloc[:599,240:]
    b = dataset.iloc[1071:,240:]
    c = pd.concat([a,b], axis=0)
    plt.title(title_1)
    c1 = c.corr()
    sns.heatmap(c1, cmap="BrBG", annot=True)
    return plt.show()

def correlation_matrix_all(dataset, title_1):
    """ Plot the correlation matrix
        Args: dataset, title
    """
    plt.title(title_1)
    x1 = dataset.corr()
    sns.heatmap(x1, cmap="BrBG", annot=True)
    return plt.show()

def months_histograms(dataset, column, title_1):
    """ Plot the histograms required
        Args: dataset, column to plot and title
    """
    plt.hist(dataset[column], bins=5, rwidth=0.95)
    plt.title(title_1)
    plt.xlabel('TEMPERATURE(ºC)')
    plt.ylabel('QUANTITY')
    return plt.show()

def project_steps_pie_chart(subject,data,hypothesis,steps,mining,document):
    """ Pie chart of the time each step has taken to me
        Args: time for each step
    """
    labels = 'Find the subject', 'Find the data', 'Define a hypothesis', 'Define the steps', 'Get and clean data, graphs and results', 'Document all steps'
    sizes = [subject,data,hypothesis,steps,mining,document]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    plt.axis('equal')  
    plt.title("Time For Steps Proportion")
    plt.tight_layout()
    return plt.show()

