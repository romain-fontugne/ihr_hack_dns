import bz2
import json
from ripe.atlas.sagan import DnsResult
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.ERROR)

import sys
sys.path.append('../ip2asn/')
import ip2asn
i2a = ip2asn.ip2asn('../ip2asn/db/rib.20200601.pickle.bz2')

builtin_msmid = [30001, 30002]
fname = 'data/dns-2020-05-29T1300.bz2'

output_fname = 'data/builtin_results_2020-05-29T1300.json'
output = []

with bz2.open(fname, 'rb') as fp:
    for line in fp:

        line_json = json.loads(line)
        result = DnsResult(line_json)

        for response in result.responses:
            # Skip if something's wrong
            if(response.is_error or response.is_malformed 
                    or not response.destination_address or not response.abuf):
                continue

            # Retrieve ASNs
            dstip = response.destination_address
            if line_json['from']:
                srcip = line_json['from']
            else:
                srcip = response.source_address
            dstasn = i2a.ip2asn(dstip)
            srcasn = i2a.ip2asn(srcip)

            # Keep each answer
            for answer in response.abuf.answers:
                if answer.is_error or answer.is_malformed or answer.type not in ['A','AAAA']:
                    continue
                row = { 
                        'msmid': result.measurement_id,
                        'srcip': srcip,
                        'dstip': dstip,
                        'srcasn': srcasn,
                        'dstasn': dstasn,
                        'proto': response.protocol,
                        'resp_time': response.response_time,
                        'name': answer.name,
                        'resol_ip': answer.address,
                        'probe_id': result.probe_id
                    }

                output.append(row)

with open(output_fname, 'w') as fp:
    json.dump(output, fp)

