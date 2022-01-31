#!/usr/bin/env python
#
# json variation on xml2 tool suite
#
# this tools is helpful for finding the jsonpath for various values on CLI
#
# e.g. just grep for values you know to exist and get the jsonpath(s) where to find
# the you can use that in commads like these:
#
#  - kubectl get jobs -o json | jq -r '.items[]|[.status.completionTime,.metadata.name]|@tsv'
#  - kubectl get job -o jsonpath='{.items[?(@.status.failed==1)].metadata.name}' | xargs -n 1 echo
#
# Refs:
#  - https://en.wikipedia.org/wiki/XMLStarlet
#  - https://github.com/clone/xml2
#  - https://web.archive.org/web/20160719191401/http://ofb.net/%7Eegnor/xml2/
#
import datetime as dt
import json
import sys

def kk(obj,prefix=()):
  if obj is None:
    print(".".join(prefix),f"= -")
  else:
    for key in obj.keys():
      if isinstance(obj[key],(str,int,bool)):
        print(".".join(prefix+(key,)),f"= {obj[key]}")
      elif isinstance(obj[key],list):
        for ii, val in enumerate(obj[key]):
          kk(val,prefix+(f"{key}[{ii}]",))
          #print(".".join(prefix+(f"{key}[{ii}]",)),f"= {obj[key]}")
      elif isinstance(obj[key],object):
        kk(obj[key],prefix+(key,))

data = json.load(sys.stdin)
kk(data)