from django.db import models

class Customclass(models.Manager):

    def sortfilterasc(self):

        return super().filter(is_deleted="N").order_by('price')

    def sortfilterdesc(self):

        return super().filter(is_deleted="N").order_by('-price')