# json2 - get jsonpath by value

Variation on xml2, html2, etc.

The purpose of the tool `json2.py` is to help users to get __jsonpath__ by grepping the desired value on CLI.

As en example:

```bash
kubectl get pod/my_pod_name -o json | python json2.py | grep status
```

might yield something like

```
spec.containers[0].env[1].valueFrom.fieldRef.fieldPath = status.hostIP
spec.containers[0].env[26].valueFrom.fieldRef.fieldPath = status.podIP
status.conditions[0].lastProbeTime = -
status.conditions[0].lastTransitionTime = 2022-01-31T11:13:13Z
status.conditions[0].status = True
status.conditions[0].type = Initialized
status.conditions[1].lastProbeTime = -
status.conditions[1].lastTransitionTime = 2022-01-31T11:13:16Z
status.conditions[1].status = True
status.conditions[1].type = Ready
status.conditions[2].lastProbeTime = -
status.conditions[2].lastTransitionTime = 2022-01-31T11:13:16Z
status.conditions[2].status = True
status.conditions[2].type = ContainersReady
status.conditions[3].lastProbeTime = -
status.conditions[3].lastTransitionTime = 2022-01-31T11:13:13Z
status.conditions[3].status = True
status.conditions[3].type = PodScheduled
status.containerStatuses[0].containerID = docker://5b87dc13db32417c98c07f4e4ef9f28dd0d4d4903da42f50d3b2a2e782181480
status.containerStatuses[0].name = web-handler
status.containerStatuses[0].ready = True
status.containerStatuses[0].restartCount = 0
status.containerStatuses[0].started = True
status.containerStatuses[0].state.running.startedAt = 2022-01-31T11:13:16Z
status.hostIP = 10.7.19.90
status.phase = Running
status.podIP = 172.23.51.131
status.podIPs[0].ip = 172.23.51.131
status.qosClass = Burstable
status.startTime = 2022-01-31T11:13:13Z
```

I have also made another tool which us web based repo @ [https://github.com/PexMor/json-tool](https://github.com/PexMor/json-tool) and [the WebUI itself](https://pexmor.github.io/json-tool/both.html).
