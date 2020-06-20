from django.contrib import admin
from .models import ProjectPaper
from .models import Org
from .models import Person
from .models import ArticleUpdate


admin.site.register(ProjectPaper)
admin.site.register(Org)
admin.site.register(Person)
admin.site.register(ArticleUpdate)