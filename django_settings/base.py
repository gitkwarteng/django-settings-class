from dataclasses import dataclass
from functools import cached_property
from typing import Dict, Any


class BaseSettingsCollection:
    """A collection of settings with each field representing a key in the resulting settings dict."""

    def __call__(self, *args, **kwargs) -> Dict[str, Dict[str, Any]]:

        return {
            attr: value.as_dict if isinstance(value, BaseDjangoSettings) else value
            for attr, value in self.__class__.__dict__.items()
            if not attr.startswith("__") and not callable(value)
        }


class BaseExtraSettings(BaseSettingsCollection):
    """A collection of settings with each field representing a key in the resulting settings dict."""

    def __call__(self, *args, **kwargs) -> Dict[str, Dict[str, Any]]:

        return {
            attr.upper(): value.as_dict if isinstance(value, BaseDjangoSettings) else value
            for attr, value in self.__class__.__dict__.items()
            if not attr.startswith("__") and not callable(value)
        }


@dataclass
class BaseDjangoSettings:
    """A base class for settings which converts it's dataclass fields into django-styled settings in caps."""

    # Extra settings
    extra: BaseSettingsCollection = None

    @cached_property
    def as_dict(self) -> Dict[str, Any]:
        """Return a dictionary with original Django setting names (capitalized) and their values."""
        attr_dict = {}
        # for field in self.__dataclass_fields__:
        # User build in __dict__ to capture dynamically added fields
        for field, value in self.__dict__.items():
            if not value:
                # Skip empty values
                continue

            if field == 'extra' and self.extra:
                attr_dict.update(self.extra())
                continue

            attr_dict[field.upper()] = value.as_dict if isinstance(value, BaseDjangoSettings) else value() if isinstance(value, BaseSettingsCollection) else value

        return attr_dict
