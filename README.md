# FunctionRuntimeMeter
A small python module containing a decorator that can measure the execution time of any of your functions in seconds
### Code example:
```python
from runtimemeter import RuntimeMeter


@RuntimeMeter
def WebpageSpeedTest():
    import requests
    webpage = requests.get("https://google.com")

WebpageSpeedTest()

# [*] Execution time: 0.6096024513244629s
```
