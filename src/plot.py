import sys
import pandas as pd
import json
import matplotlib.colors as mcolors
from matplotlib import pylab as plt

MIN_PROBES = 3

input_fname = sys.argv[1]
asn = int(sys.argv[2])

default_color = 'tab:green',
colors_keys = {13335:'tab:orange', 3356:'tab:red', 15169:'tab:blue', 36692:'tab:brown', 19281:'tab:purple'}
dns_names = {13335:'Cloudflare', 3356:'Level(3)', 15169:'Google', 36692:'OpenDNS', 19281:'Quad9'}
asn_names = {7922:'Comcast', 7018:'ATT', 22394:'Verizon', 4713:'NTT OCN', 2497:'IIJ', 17676:'Softbank', 2516:'KDDI', 3320:'DTAG', 21928:'T-Mobile', 3215:'Orange'}

with open(input_fname,'r') as fp:
    d = json.load(fp)

df = pd.DataFrame(d)
# todo remove this
# df['type'] = 'A'

for measurement_id in ['popular', 'all']:
    # for dns_type in ['A', 'AAAA']:
    for ipv in [4,6]:
        if measurement_id == 'all':
            asn_data = df[ (df.srcasn == asn)]
        elif measurement_id == 'popular':
            asn_data = df[
                (df.srcasn == asn)  
                & (df.msmid == 30002)
                ]

        if ipv == 6:
            asn_data = asn_data[asn_data.dstip.str.contains(':')]
        else:
            asn_data = asn_data[asn_data.dstip.str.contains('.')]

        gb = asn_data.groupby('dstasn')
        results = gb.median()

        results['nb_probes'] = gb.probe_id.unique().apply(len)

        results = results[results['nb_probes']>MIN_PROBES] 

        plt.figure()

        # Plot ASN resolver
        resp_time = 0
        if asn in results['resp_time']:
            resp_time = results['resp_time'][asn]
        plt.bar(-1, resp_time, label=asn_names[asn], color=default_color)

        # Plot open resolvers
        for x, dns_asn in enumerate(dns_names.keys()):
            resp_time = 0
            if dns_asn in results['resp_time']:
                resp_time = results['resp_time'][dns_asn]
            plt.bar(x, resp_time, label=dns_names[dns_asn], color=colors_keys[dns_asn])


        # plt.legend()
        plt.xticks(
                [x-1 for x in range(len(dns_names)+1)], 
                [asn_names[asn]]+list(dns_names.values()), 
                rotation=45)
        plt.title(f'{asn_names[asn]}, IPv{ipv}, {measurement_id} domains')
        plt.grid(alpha=.3)
        plt.tight_layout()
        plt.savefig(f'fig/AS{asn}_{measurement_id}_ipv{ipv}.pdf')


        # import IPython
        # IPython.embed()
