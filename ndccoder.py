import json

with open('drug-ndc-0001-of-0001.json', 'r') as fp:
    data = fp.read()
    drugs_loaded = json.loads(data)
    results = drugs_loaded['results']
    results_trim = str(results[1:])
    ## this section isn't working
    results_list = results_trim.replace('},\n        {','}\n\n{')
    results_listed = results_list.split('\n\n')
    for i in results_trim:
        record = json.loads(i)
        ndc = json.dumps(record['product_ndc'])
        print(ndc)

