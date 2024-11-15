import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_wsgi_application()

# Only needed for production environments
if __name__ == "__main__":
    from waitress import serve
    serve(application, host='127.0.0.1', port=8000)
