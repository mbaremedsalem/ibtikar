import django_filters
from .models import Course

class CoursFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = ['title',]
        # exclude = ['slug','experience','image','prix']