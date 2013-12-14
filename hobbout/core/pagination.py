from django.conf import settings


class BasePaginationMixin(object):

    class Meta:
        abstract = True

    def dispatch(self, request, *args, **kwargs):
        self.max_id = int(request.GET.get('max_id', '0'))
        return super(BasePaginationMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BasePaginationMixin, self).get_context_data(**kwargs)
        if self.max_id == 0:
            context['first_page'] = True
        return context


class MicroBlogPaginationMixin(BasePaginationMixin):

    PAGE_SIZE = settings.PAGE_SIZE['MICROBLOG']


class NoteBoardPaginationMixin(BasePaginationMixin):

    PAGE_SIZE = settings.PAGE_SIZE['NOTEBOARD']


class NotePaginationMixin(BasePaginationMixin):

    PAGE_SIZE = settings.PAGE_SIZE['NOTE']


class BlogPaginationMixin(BasePaginationMixin):

    PAGE_SIZE = settings.PAGE_SIZE['BLOG']


class AlbumPaginationMixin(BasePaginationMixin):

    PAGE_SIZE = settings.PAGE_SIZE['ALBUM']


class MediaFramePaginationMixin(BasePaginationMixin):

    PAGE_SIZE = settings.PAGE_SIZE['MEDIAFRAME']


class BasePaginationAPIMixin(object):

    def get_max_id(self, request):
        self.max_id = int(request.GET.get('max_id', '0'))
        self.size = self.PAGE_SIZE
        return self.max_id


class MicroBlogPaginationAPIMixin(BasePaginationAPIMixin):

    PAGE_SIZE = settings.PAGE_SIZE['MICROBLOG']
