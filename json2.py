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

only_keys = True

def kk(obj, prefix=()):
    global only_keys
    if obj is None:
        if only_keys:
            print(".".join(prefix))
        else:
            print(".".join(prefix), f"= -")
    elif isinstance(obj, (str, int, float, bool)):
        if only_keys:
            print(".".join(prefix))
        else:
            print(".".join(prefix), f"= {obj}")
    else:
        try:
            if isinstance(obj, list):
                for ii, val in enumerate(obj):
                    kk(val, prefix + (f"[{ii}]",))
            elif isinstance(obj, object):
                for key in obj.keys():
                    if isinstance(obj[key], list):
                        for ii, val in enumerate(obj[key]):
                            kk(val, prefix + (f"{key}[{ii}]",))
                    elif isinstance(obj[key], object):
                        kk(obj[key], prefix + (key,))
        except AttributeError as ex:
            print("Fatal error parsing the JSON structures: ", ex)
            sys.exit(-1)


data = json.load(sys.stdin)
kk(data)
