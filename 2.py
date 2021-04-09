import re

refs = [
'abc_cmp_campaign1_xyz',
'abc_def_cmp_campaign2',
'cmp_campaign3-xyz',
'abcd-xyz-cmp-campaign4-',
'abccmpcampaign5-xyz',
]

results = []

for ref in refs:
    res = re.findall(r'.*cmp[_-]?([a-y0-9]+)', ref)
    results.extend(res)
print(results)
