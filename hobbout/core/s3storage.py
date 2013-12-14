from django.contrib.staticfiles.storage import CachedFilesMixin
from pipeline.storage import PipelineMixin
from storages.backends.s3boto import S3BotoStorage
from storages.utils import setting


class S3PipelineStorage(PipelineMixin, CachedFilesMixin, S3BotoStorage):

    headers = setting('AWS_STATIC_HEADERS', {})
    bucket_name = setting('AWS_STATIC_STORAGE_BUCKET_NAME')
    custom_domain = setting('AWS_STATIC_S3_CUSTOM_DOMAIN')
    location = setting('AWS_STATIC_PATH')
