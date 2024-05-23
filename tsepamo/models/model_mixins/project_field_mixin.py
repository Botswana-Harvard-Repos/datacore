from django.db import models

from ..projects import Projects


class ProjectFieldMixin(models.Model):

    project = models.ForeignKey(
        Projects,
        on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.assign_related_project()
        super().save(*args, **kwargs)

    def assign_related_project(self, name=None):
        try:
            project_obj = Projects.objects.get(name=name)
        except Projects.DoesNotExist:
            raise
        else:
            self.project = project_obj

    class Meta:
        abstract = True
