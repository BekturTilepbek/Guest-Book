from django.db import models

statuses = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Entry(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Имя автора записи")
    email = models.EmailField(null=False, blank=False, verbose_name="Почта автора записи")
    text = models.TextField(null=False, blank=False, verbose_name="Текст записи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время редактирования")
    status = models.CharField(max_length=20, choices=statuses, default='active', verbose_name="Статус")

    def __str__(self):
        return f"{self.pk}. {self.name} ({self.status})"

    class Meta:
        db_table = "entries"
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
