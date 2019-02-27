from django.utils.deprecation import MiddlewareMixin


class DisableCsrf(MiddlewareMixin):
    def process_request(self, request):
            setattr(request, '_dont_enforce_csrf_checks', True)
