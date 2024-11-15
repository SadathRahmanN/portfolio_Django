import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_wsgi_application()

# Ensure the app listens on the correct port for Render:
if __name__ == "__main__":
    from gunicorn.app.base import BaseApplication

    class GunicornApplication(BaseApplication):
        def __init__(self, *args, **kwargs):
            self.cfg = gunicorn.config.Config()
            self.cfg.set('bind', f'0.0.0.0:{os.environ.get("PORT", "8000")}')
            super().__init__(*args, **kwargs)

        def load(self):
            return application

    GunicornApplication().run()
