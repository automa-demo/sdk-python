from ._client import AsyncAutoma, Automa
from .resources import AsyncCodeResource, CodeResource

__all__ = [
    "Automa",
    "AsyncAutoma",
    "AsyncCodeResource",
    "CodeResource",
]

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# automa._exceptions.NotFoundError -> automa.NotFoundError
__locals = locals()

for __name in __all__:
    if not __name.startswith("__"):
        try:
            __locals[__name].__module__ = "automa"
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass
