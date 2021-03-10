from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.shortcuts import resolve_url
from django.template.loader import render_to_string


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMELE = "F", "Female"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(
        max_length=13,
        blank=True,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )
    gender = models.CharField(max_length=1, blank=True, choices=Gender.choices)
    avatar = models.ImageField(
        blank=True,
        upload_to="accounts/avatar/%Y/%m/%d",
        help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요.",
    )
    following_set = models.ManyToManyField(
        "self", blank=True, related_name="follower_set", symmetrical=False
    )

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return resolve_url("pydenticon_image", self.username)

    def send_welcome_email(self):
        subject = render_to_string("accounts/welcome_email_subject.txt")
        content = render_to_string("accounts/welcome_email_content.txt", {"user": self})
        self.email_user(subject, content, fail_silently=False)
