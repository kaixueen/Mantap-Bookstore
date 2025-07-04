from django.db import connection
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.core.cache import cache

class SetSessionContextMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            self.set_session_context(request)
        response = self.get_response(request)
        return response

    def set_session_context(self, request):
        user = request.user
        role = 'unknown'
        user_id = None
        is_staff = user.is_staff

        if user.is_superuser:
            role = 'admin'
        elif hasattr(user, 'sellerprofile'):
            role = 'seller'
            user_id = user.id
        elif hasattr(user, 'customerprofile'):
            role = 'customer'
            user_id = user.id

        request.session['role'] = role
        request.session['is_staff'] = is_staff
        if user_id:
            request.session['user_id'] = user_id

class RateLimitMiddleware(MiddlewareMixin):
    RATE_LIMIT = 100  # Number of allowed requests
    TIME_PERIOD = 60  # Time period in seconds

    def process_request(self, request):
        ip = self.get_client_ip(request)
        key = f'rate-limit-{ip}'

        if cache.get(key) is None:
            cache.set(key, 1, timeout=self.TIME_PERIOD)
        else:
            request_count = cache.incr(key)
            if request_count > self.RATE_LIMIT:
                return JsonResponse({'error': 'Rate limit exceeded'}, status=429)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
