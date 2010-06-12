from django.db import connection
import time

class QueriesCountMiddleware:
    def process_request(self, request):
        self.start = time.time()

    def process_response(self, request, response):
        if 'text/html' in response['content-type']:
            duration = time.time() - self.start
            response.content = response.content.replace('</body>', '<b>%f secs</b> and %d queries</body>' % (duration, len(connection.queries)))
        return response
