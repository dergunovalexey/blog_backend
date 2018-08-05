DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'user_blog',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '',
        'TEST': {
            'TEMPLATE': 'template0'
        }
    }
}
