
class BinanceAPIException(Exception):
    def __init__(self, response):
        json_res = response.json()
        self.status_code = response.status_code
        self.response = response
        self.code = json_res['code']
        self.message = json_res['msg']
        self.request = getattr(response, 'request', None)

    def __str__(self):  # pragma: no cover
        return 'APIError(code=%s): %s' % (self.code, self.message)


class BinanceOrderException(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return 'BinanceOrderException(code=%s): %s' % (self.code, self.message)


class BinanceOrderMinAmountException(BinanceOrderException):

    def __init__(self, value):
        message = "Amount must be a multiple of %s" % value
        super(BinanceOrderMinAmountException, self).__init__(-1013, message)


class BinanceOrderMinPriceException(BinanceOrderException):

    def __init__(self, value):
        message = "Price must be at least %s" % value
        super(BinanceOrderMinPriceException, self).__init__(-1013, message)


class BinanceOrderMinTotalException(BinanceOrderException):

    def __init__(self, value):
        message = "Total must be at least %s" % value
        super(BinanceOrderMinTotalException, self).__init__(-1013, message)