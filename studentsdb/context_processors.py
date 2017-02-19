from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject


def students_proc(request):
    PORTAL_URL =  SimpleLazyObject(lambda: get_current_site(request))
    protocol = 'https' if request.is_secure() else 'http'

    return {
        'PORTAL_URL': "{0}://{1}".format(protocol, PORTAL_URL)}
