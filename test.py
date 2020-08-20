from runtimemeter import RuntimeMeter


@RuntimeMeter
def WebpageSpeedTest():
    import requests
    webpage = requests.get("https://google.com")

WebpageSpeedTest()
