# json2

Variation on xml2, html2, etc.

The purpose of the tool `json2.py` is to help users to get __jsonpath__ by grepping the desired value.

As en example:

```bash
kubectl get pod/my_pod_name | python json2.py | grep status
```

My another repo [https://github.com/PexMor/json-tool](https://github.com/PexMor/json-tool) - My Web UI alternative with [The WebUI itself](https://pexmor.github.io/json-tool/both.html).
