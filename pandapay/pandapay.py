import requests


def _url(path):
    return 'https://api.pandapay.io/v1' + path


class Client(object):
    def __init__(self, key):
        auth = (key)
        self.customers = CustomerClient(auth)
        self.donations = DonationClient(auth)
        self.grants = GrantClient(auth)


class DonationClient(object):
    def __init__(self, auth):
        self.auth = auth

    def create(self, **kwargs):
        return requests.post(
            _url('/donations'),
            data=kwargs,
            auth=self.auth
        )


class CustomerClient(object):
    def __init__(self, auth):
        self.auth = auth

    def create(self, **kwargs):
        return requests.post(
            _url('/customers'),
            data=kwargs,
            auth=self.auth
        )

    def update(self, customer_id, **kwargs):
        url = _url('/customers/{:d}'.format(customer_id))
        return requests.put(
            url,
            data=kwargs,
            auth=self.auth
        )

    def delete(self, customer_id):
        url = _url('/customers/{:d}'.format(customer_id))
        return requests.delete(
            url,
            auth=self.auth
        )


class GrantClient(object):
    def __init__(self, auth):
        self.auth = auth

    def create(self, donation_id, **kwargs):
        if donation_id:
            url = _url('/donations/{:d}/grants'.format(donation_id))
        else:
            url = _url('/grants')

        return requests.post(
            url,
            data=kwargs,
            auth=self.auth
        )
