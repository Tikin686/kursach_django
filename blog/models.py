from django.db import models

NULLABLE = {"blank": True, "null": True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок блога")
    body = models.TextField(verbose_name="Текст блога")
    preview_image = models.ImageField(upload_to="blog/preview", verbose_name="Превью изображения", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    slug = models.SlugField(max_length=150, verbose_name="Slug", **NULLABLE)
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"