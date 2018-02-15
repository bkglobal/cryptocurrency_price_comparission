import requests as r
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

# def compare_coin(name, compare=['USD'], all_data=True, aggregate=1, exchange=''):
#     limit=9999
#     st='https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&aggregate={}'.format(name, ','.join(compare).upper(), limit, aggregate)
#     res= r.get(st)
#     ans=res.json()['Data']
#     dpd=pd.DataFrame(ans)
#     return dpd
#
# df=compare_coin('BTC')
# df['timestamp']= [dt.datetime.fromtimestamp(d) for d in df.time]
# plt.plot(df.timestamp,df.close)
# plt.xticks(rotation=30)
# plt.show()


def compare_price(symbol, comparison_symbol, all_data=True, aggregate=1, exchange=''):

    inp = int(input('1 for Minute\n2 for Hourly\n3 for Daily '))
    if inp == 1:
        limit = 9999
        history = 'histominute'
    elif inp == 2:
        limit = 9999
        history = 'histohour'
    elif inp == 3:
        limit = 1
        history = 'histoday'

    url = 'https://min-api.cryptocompare.com/data/'+history+'?fsym={}&tsym={}&limit={}&aggregate={}'.format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)

    df = pd.DataFrame(r.get(url).json()['Data'])
    df['timestamp'] = [dt.datetime.fromtimestamp(d) for d in df.time]
    plt.plot(df.timestamp, df.close)
    plt.xticks(rotation = 30)
    return plt.show()


print(compare_price('BTC', 'USD'))







# import matplotlib.pyplot as plt
# import numpy as np
# import plotly.plotly as py
#
# colormaps_fig = plt.figure()
#
# num_plots = 10
#
# # Have a look at the colormaps here and decide which one you'd like:
# # http://matplotlib.org/1.2.1/examples/pylab_examples/show_colormaps.html
# colormap = plt.cm.gist_ncar
# plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
#
# # Plot several different functions...
# x = np.arange(10)
# labels = []
# for i in range(1, num_plots + 1):
#     plt.plot(x, i * x + 5 * i)
#     labels.append(r'$y = %ix + %i$' % (i, 5 * i))
#
# plot_url = py.plot_mpl(colormaps_fig, filename='mpl-colormaps')

