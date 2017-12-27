import requests


def _url(path):
    return 'https://api.pandapay.io/v1' + path


def _auth(pandapay_secret):
    return (pandapay_secret)


def create_donation(pandapay_auth, **kwargs):
    return requests.post(
        _url('/donations'),
        data=kwargs,
        auth=pandapay_auth
    )


def create_customer(pandapay_auth, **kwargs):
    return requests.post(
        _url('/customers'),
        data=kwargs,
        auth=pandapay_auth
    )


def update_customer(pandapay_auth, customer_id, **kwargs):
    url = _url('/customers/{:d}'.format(customer_id))
    return requests.put(
        url,
        data=kwargs,
        auth=pandapay_auth
    )


def delete_customer(pandapay_auth, customer_id):
    url = _url('/customers/{:d}'.format(customer_id))
    return requests.delete(
        url,
        auth=pandapay_auth
    )


def create_grant(pandapay_auth, donation_id, **kwargs):
    if donation_id:
        url = _url('/donations/{:d}/grants'.format(donation_id))
    else:
        url = _url('/grants')

    return requests.post(
        url,
        data=kwargs,
        auth=pandapay_auth
    )
