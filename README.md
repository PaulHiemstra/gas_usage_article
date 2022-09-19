# Introduction
This article shows a regression model of gas usage, this README provides some additional information. 

# Loading data
The standard data included is of my own usage data, but made anonymous. If you have your own data downloade from 'Mijn Eneco' you can use the following code to create your own anonymous version. You can also just run the code on the non-anonymous data. 

    from local_functions import *
    from sklearn.preprocessing import MinMaxScaler

    verbruik = read_eneco_usage('verbruik_18-09-2014_18-09-2022_20139825_4.xlsx')
    verbruik[:] = MinMaxScaler().fit_transform(verbruik)
    verbruik.to_excel('usage_anonymized.xlsx')

The weather data was downloaded from the Royal Netherlands Meteorological Institute website (KNMI, [link](https://daggegevens.knmi.nl/klimatologie/daggegevens)).

# Development environment
The repo contains a .devcontainer file that can be used with Visual Studio Code. The requirements file contains the packages needed. 