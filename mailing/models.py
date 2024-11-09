from django.db import models
from users.models import User


NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name="Ф.И.О. клиента")
    email = models.EmailField(
        max_length=150, verbose_name="Адрес электронной почты", unique=True
    )
    comment = models.TextField(verbose_name="Комментарий", **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name="Тема сообщения")
    massage = models.TextField(max_length=500, verbose_name="Сообщение")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="clients", **NULLABLE
    )

    def __str__(self):
        return f"{self.subject}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Mailing(models.Model):
    STATUS_CHOICES = [
        ("created", "Создана"),
        ("started", "Активна"),
        ("completed", "Завершена"),
        ("disabled", "Отключить"),
    ]

    PERIODICITY_CHOICES = [
        ("daily", "Ежедневно"),
        ("weekly", "Еженедельно"),
        ("monthly", "Ежемесячно"),
    ]
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, verbose_name="Сообщение"
    )
    start_time = models.DateTimeField(auto_now=True, verbose_name="Начало рассылки")
    periodicity = models.CharField(max_length=50, verbose_name="Периодичность отправки")
    end_time = models.DateTimeField(
        blank=True, null=True, verbose_name="Окончание рассылки"
    )
    status = models.CharField(max_length=50, verbose_name="Статус отправки")
    description = models.CharField(max_length=300, verbose_name="Описание", **NULLABLE)
    clients = models.ManyToManyField(Client, verbose_name="Клиенты")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mailings", **NULLABLE
    )

    def __str__(self):
        return f"Mailing{self.id} - {self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [
            ("can_deactivate_mailing", 'Can deactivate mailing'),
        ]


class MailingAttempt(models.Model):
    STATUS_CHOICES = [("success", "Успешно"), ("failed", "Не успешно")]

    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, verbose_name='Рассылка'
    )
    send_time = models.DateTimeField(auto_now=True, verbose_name="Время отправки")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    server_response = models.TextField(verbose_name='Ответ почтового сервера', **NULLABLE)

    def __str__(self):
        return f"Попытка {self.id} для рассылки {self.mailing.id}"

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'


