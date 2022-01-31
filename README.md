# json2 - get jsonpath by value

Variation on xml2, html2, etc.

The purpose of the tool `json2.py` is to help users to get __jsonpath__ by grepping the desired value on CLI.

As en example:

```bash
kubectl get pod/my_pod_name | python json2.py | grep status
```

I have also made another tool which us web based repo @ [https://github.com/PexMor/json-tool](https://github.com/PexMor/json-tool) and [the WebUI itself](https://pexmor.github.io/json-tool/both.html).
