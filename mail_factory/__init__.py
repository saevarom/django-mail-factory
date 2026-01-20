"""Django Mail Manager"""

import django

from mail_factory.app_no_autodiscover import SimpleMailFactoryConfig
from mail_factory.apps import MailFactoryConfig
from mail_factory.factory import MailFactory
from mail_factory.forms import MailForm  # NOQA
from mail_factory.mails import BaseMail  # NOQA

try:
    from importlib import metadata as importlib_metadata
except ImportError:  # pragma: no cover - Python < 3.8 fallback
    import importlib_metadata  # type: ignore[no-redef]

try:
    __version__ = importlib_metadata.version("django-mail-factory")
except importlib_metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__all__ = ["MailFactoryConfig", "SimpleMailFactoryConfig"]

factory = MailFactory()


if django.VERSION[:2] < (3, 2):
    default_app_config = "mail_factory.apps.MailFactoryConfig"
