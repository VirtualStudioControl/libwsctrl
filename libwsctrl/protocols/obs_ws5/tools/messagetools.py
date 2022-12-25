from logging import Logger

def checkError(msg, errorLogger: Logger):
    if msg['op'] == 7:
        if not data(msg)['requestStatus']['result']:
            code = data(msg)['requestStatus']['code']
            comment = ""
            if 'comment' in data(msg)['requestStatus']:
                comment = data(msg)['requestStatus']['comment']
            type = data(msg)['requestType']
            id = data(msg)['requestId']

            errorLogger.error("Request {} of type {} failed with Code {}: {}".format(id, type, code, comment))
            return False

    return True


def data(msg):
    return msg['d']


def innerData(msg):
    if msg['op'] == 5: # Event
        return data(msg)["eventData"]
    if msg['op'] == 6: # Request
        return data(msg)["requestData"]
    if msg['op'] == 7: # Response
        if "responseData" not in data(msg):
            print(msg)
        return data(msg)["responseData"]
