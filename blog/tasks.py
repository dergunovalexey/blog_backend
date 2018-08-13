from django.apps import apps
import requests
from bs4 import BeautifulSoup
from celery import shared_task


@shared_task
def get_preview_description(id):
    """
    save description and preview from url
    :param id: blogentry id
    """
    BlogEntry = apps.get_model('blog', 'BlogEntry')
    obj = BlogEntry.objects.filter(id=id).first()
    if obj and obj.link:
        resp = requests.get(obj.link)
        if 'text/html' in resp.headers['Content-Type']:
            soup = BeautifulSoup(resp.content, 'html.parser')
            description = soup.head.find('meta', property="og:description")
            image = soup.head.find('meta', property="og:image")

            if description:
                obj.description = description['content']

            if image:
                obj.preview = image['content']

            if description or image:
                obj.save()
