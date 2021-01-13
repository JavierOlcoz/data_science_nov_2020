import pandas as pd

def r_e(variable, excel, sheet):
    """ Read excel
        Args = variables, excel to read, shhet of the excel
    """
    variable = pd.read_excel(excel, sheet_name=sheet, engine='openpyxl')

    return variable

def estadisticos(dataset):
    """ This function allows us to calculate the statistics and create columns
        Args: dataset
    """

    dataset['count'] = dataset.count(axis=1)
    dataset['mean'] = dataset.mean(axis=1, skipna=True)
    dataset['median'] = dataset.median(axis=1, skipna=True)
    dataset['desv_tipica'] = dataset.std(axis=1, skipna=True)
    dataset['quantile_1'] = dataset.quantile(q=0.25, axis=1)
    dataset['quantile_3'] = dataset.quantile(q=0.75, axis=1)
    dataset['IQR'] = dataset['quantile_3'] - dataset['quantile_1']
    dataset['skew'] = dataset.skew(axis=1, skipna=True)
    dataset['kurtosis'] = dataset.kurtosis(axis=1, skipna=True)

    return dataset


def under_50(dataset):
    """ This function let us take only the values with more than 50 data
        Args: dataset
    """
    dataset = dataset[dataset['count'] > 50]

    return dataset
    
def under_1(dataset):
    """ This function let us take only the values with more than 50 data
        Args: dataset
    """
    dataset = dataset[dataset['count'] > 1]

    return dataset

def meses_pd(dataset,i):
    """ Assign dataframes to each month
        Args: datasset and month
    """

    lista_anos = ['2001', '2002', '2003','2004','2005','2006','2007','2008','2009',
    '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']

    lista_anos_1 = []

    for j in lista_anos:
        y = j + str(i)
        lista_anos_1.append(y)
    
    lista_anos_2 = []

    for k in lista_anos_1:
        z = int(k)
        lista_anos_2.append(z)

    x = dataset.loc[:,lista_anos_2]

    return x


def means(enero,f,m,a,ma,j,jl,ag,s,o,n,d):
    """ Dataframe with the mean values of every month
        Args: months
    """
    enero = enero.rename(columns={'mean':'enero_mean'})
    f = f.rename(columns={'mean':'febrero_mean'})
    m = m.rename(columns={'mean':'marzo_mean'})
    a = a.rename(columns={'mean':'abril_mean'})
    ma = ma.rename(columns={'mean':'mayo_mean'})
    j = j.rename(columns={'mean':'junio_mean'})
    jl = jl.rename(columns={'mean':'julio_mean'})
    ag = ag.rename(columns={'mean':'agosto_mean'})
    s = s.rename(columns={'mean':'septiembre_mean'})
    o = o.rename(columns={'mean':'octubre_mean'})
    n = n.rename(columns={'mean':'noviembre_mean'})
    d = d.rename(columns={'mean':'diciembre_mean'})

    means = pd.concat([enero['enero_mean'], f['febrero_mean'], m['marzo_mean'], a['abril_mean'], ma['mayo_mean'],
    j['junio_mean'], jl['julio_mean'], ag['agosto_mean'], s['septiembre_mean'], o['octubre_mean'], 
    n['noviembre_mean'], d['diciembre_mean']], axis=1)

    return means

def medians(enero,f,m,a,ma,j,jl,ag,s,o,n,d):
    """ Dataframe with the median values of every month
        Args: months
    """
    enero = enero.rename(columns={'median':'enero_median'})
    f = f.rename(columns={'median':'febrero_median'})
    m = m.rename(columns={'median':'marzo_median'})
    a = a.rename(columns={'median':'abril_median'})
    ma = ma.rename(columns={'median':'mayo_median'})
    j = j.rename(columns={'median':'junio_median'})
    jl = jl.rename(columns={'median':'julio_median'})
    ag = ag.rename(columns={'median':'agosto_median'})
    s = s.rename(columns={'median':'septiembre_median'})
    o = o.rename(columns={'median':'octubre_median'})
    n = n.rename(columns={'median':'noviembre_median'})
    d = d.rename(columns={'median':'diciembre_median'})

    medians = pd.concat([enero['enero_median'], f['febrero_median'], m['marzo_median'], a['abril_median'],
    ma['mayo_median'], j['junio_median'], jl['julio_median'], ag['agosto_median'], s['septiembre_median'], 
    o['octubre_median'], n['noviembre_median'], d['diciembre_median']], axis=1)

    return medians

