from pyzabbix import ZabbixMetric, ZabbixSender


class Sender():
    def __init__(self, host, key, value):
        self.host = host
        self.key = key
        self.value = value

    def _data(self):
        packet = [ ZabbixMetric(self.host, self.key, self.value) ]
        return packet

    def send(self):
        zbx = ZabbixSender('127.0.0.1')
        data = self._data()
        try:
            zbx_result = zbx.send(data)
            failure_result = zbx_result.failed
        except:
            failure_result = 1

        if failure_result == 0:
            result = True
        else:
            result = False
        return result
