# FunctionRuntimeMeter
A small python module containing a decorator that can measure the execution time of any of your functions in seconds.
### How to use
To measure the speed of your function, you just need to:
+ add the runtimemeter.py file to the project
+ import runtimemeter
+ add @RuntimeMeter to code before calling the required function.
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
