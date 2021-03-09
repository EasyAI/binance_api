
def format_candles(raw_data, candleType):
    '''
    Candle format =
        [Open_Time, Open, High, Low, Close, Volume, Close_Time, Quote_Asset_Volume, Num_trades]
    '''
    if candleType == 'REST':
        format_data = [
            [int(c[0]), 
            float(c[1]), 
            float(c[2]), 
            float(c[3]), 
            float(c[4]), 
            float(c[5]), 
            int(c[6]), 
            float(c[7]), 
            int(c[8])]
            for c in raw_data]

        format_data.reverse()

    elif candleType == 'SOCK':
        c = raw_data
        format_data = [int(c['t']), 
                    float(c['o']), 
                    float(c['h']), 
                    float(c['l']), 
                    float(c['c']), 
                    float(c['v']), 
                    int(c['T']), 
                    float(c['q']), 
                    int(c['n'])]

    return(format_data)


def format_trades(raw_data):
    format_data = []
    raw_data.reverse()
    for t in raw_data:
        t.update({'side': 'BUY' if t['isBuyerMaker'] else 'SELL'})
        format_data.append(t)
    return(format_data)


def format_depth(raw_data, candleType):
    '''
    Candle format =
        [upID, price, quantity]
    '''
    if candleType == 'REST':
        lastUpdateId = int(raw_data['lastUpdateId'])

        a = {}
        b = {}

        for row in raw_data['asks']:
            a.update({float(row[0]):[lastUpdateId, float(row[1])]})

        for row in raw_data['bids']:
            b.update({float(row[0]):[lastUpdateId, float(row[1])]})

        format_data ={
            'a':a,
            'b':b
        }

    elif candleType == 'SOCK':
        lastUpdateId = int(raw_data['u'])

        format_data = {
            'a':[[lastUpdateId, float(row[0]), float(row[1])] for row in raw_data['a']],
            'b':[[lastUpdateId, float(row[0]), float(row[1])] for row in raw_data['b']]
        }

    return(format_data)
