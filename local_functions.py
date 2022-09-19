import pandas as pd

def read_eneco_usage(path):
    verbruik = (
    pd.read_excel(path, skiprows=1, index_col=0)
      .rename(columns={'Verbruik':'gas_usage',
                       'Verbruik laag tarief': 'elec_low',
                       'Verbruik hoog tarief': 'elec_high'})
      .drop(columns=['Meterstand laagtarief (El 1)', 'Meterstand hoogtarief (El 2)', 'Meterstand', 'Geschat?', 'Geschat?.1'])
    )
    verbruik['elec_usage'] = verbruik[['elec_low', 'elec_high']].sum(axis=1)
    return verbruik

def read_knmi(path):
  temp = pd.read_csv(path, comment='#', header=None, names=['station', 'date', 'T_gem', 'T_min', 'T_max'])
  temp['date'] = pd.to_datetime(temp['date'], format='%Y%m%d')
  temp[['T_gem', 'T_min', 'T_max']]  = temp[['T_gem', 'T_min', 'T_max']] / 10
  return temp.set_index('date')