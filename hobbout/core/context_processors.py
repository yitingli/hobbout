from django.conf import settings


def template_constants(request):
    context = {}
    context.update(settings.IMAGE_SIZE)
    # to append other constants "context.update(more)"
    return context
