from django.db import models
from api.models.base.create_update_mixin import CreateUpdateMixin
from api.models.base.is_active_mixin import IsActiveMixin


class UserMixin(IsActiveMixin, CreateUpdateMixin):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
