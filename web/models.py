from django.db import models


class Category(models.Model):
    icon = models.FileField(upload_to='category/icons/', blank=True)
    title = models.CharField(max_length=50)

    class Meta:
        db_table = "web_category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ratings = models.FloatField(default=0.0)
    duration = models.IntegerField(default=0)
    created_by = models.CharField(max_length=25, default='Unknown')
    languages = models.TextField(default='')
    thumbnail_img = models.ImageField(upload_to='courses/thumbnail', blank=True)
    original_price = models.FloatField(default=0.0)
    discount_price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_ratings = models.IntegerField(default=0)
    lectures = models.IntegerField(default=0)


    class Meta:
        db_table = "web_course"
        verbose_name_plural = "courses"

    def __str__(self):
        return self.title