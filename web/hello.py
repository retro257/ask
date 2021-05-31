import re
def wsgidef(slov, start_func):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_func(status, headers)
    test = r"\w+=\d+"
    text = slov["QUERY_STRING"]
    otvet = re.findall(test, text)
    kon_otv = [bytes(i+'\n', 'ascii')for i in slov["QUERY_STRING"].split("&")]
    return kon_otv
