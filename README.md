# ihr_hack_dns

## How to use this code
- download a dns dump from: https://data-store.ripe.net/datasets/atlas-daily-dumps/
- parse it: python src/parse_dump.py data/dump_file.bz2
- plot results for an AS (e.g. AS7922): python src/plot.py data/parsed_results_2020-06-01T1500.json 7922
- plot will appear in the fig directory

## Queried domains in builtin measurement (30002)
73 queried domains with different upper/lower casing.

['google.co.in.', 'wikipedia.org.', 'amazon.com.', 'tmall.com.',
'TMALL.com.', 'qq.com.', 'google.co.jp.', 'google.co.jP.', 'GOOGLE.Co.jP.',
'sohu.com.', 'sohu.COM.', 'aMaZon.coM.', 'aMAzOn.Com.', 'tmall.Com.',
'google.co.JP.', 'google.co.IN.', 'amazon.COM.', 'GooGLe.CO.Jp.',
'forcesafesearch.google.com.', 'SOHu.com.', 'QQ.com.', 'sohu.Com.', 'qq.Com.',
'sohu.CoM.', 'taobao.com.', 'tmall.coM.', 'ns-rpz.sch.gr.', 'gOOglE.Co.jp.',
'gOOGle.co.in.', 'tMALL.Com.', 'qq.coM.', 'QQ.coM.', 'amaZOn.com.',
'amazon.coM.', 'AMAzON.com.', 'Tmall.com.', 'amAzon.cOM.', 'QQ.cOM.',
'GOOgLE.Co.in.', 'qq.COM.', 'amazon.Com.', 'amazon.cOM.', 'TMaLL.com.',
'tmall.cOM.', 'tmall.COM.', 'tMAll.com.', 'GoOglE.cO.jp.', 'qQ.com.',
'us1.shecan.ir.', 'Amazon.com.', 'amazon.CoM.', 'goOGle.cO.In.', 'QQ.Com.',
'qq.cOM.', 'SOHU.com.', 'sohu.cOM.', 'sohu.coM.', 'TMAlL.COm.', 'qq.CoM.',
'gooGLe.cO.In.', 'soHu.com.', 'aMAZon.cOM.', 'aMAzOn.coM.', 'amAzoN.CoM.',
'soHU.CoM.', 'tmall.CoM.', 'soHu.coM.', 'tMALl.coM.', 'tMAll.Com.',
'SOHu.COm.', 'AmazON.Com.', 'SohU.COm.', 'googLE.cO.In.']

## Things to do:
- [x] grab DNS daily dumps
- [x] parse data to get:
    - probe id
    - probe asn
    - resolver
    - name
    - querytime
    - ttl
    - error
- [x] plot data per ASN
- [x] plot data per resolver
- [ ] compare ipv6, ipv4
