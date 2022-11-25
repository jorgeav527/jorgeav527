from django.db import models
from django.utils.translation import gettext_lazy as _


class Language(models.Model):
    # Knowing language
    LANGUAGE_KNOW = (
        ("P", "Portuguese"),
        ("S", "Spanish"),
        ("E", "English"),
    )
    """
    This is for change or track the laguage of the CV:
    """
    language = models.CharField(_("Name Language"), max_length=1, choices=LANGUAGE_KNOW)

    def __str__(self):
        return "%s" % (self.language)
