import inspect


class DuckTypingMixin:
    
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(instance.__class__)
    
    
    def __subclasscheck__(cls, subclass):
        contracts = getattr(cls, "_interface_contracts_", {})
        for name, info in contracts.items():
            kind = info[0]
            expected_sig = info[1] if len(info) > 1 else None
            expected_type = info[2] if len(info) > 2 else None

            try:
                raw = inspect.getattr_static(subclass, name)
            except AttributeError:
                raw = None

            if kind == "method":
                if raw is None:
                    return False

                if isinstance(raw, staticmethod):
                    raw_type = "staticmethod"
                    func = raw.__func__
                elif isinstance(raw, classmethod):
                    raw_type = "classmethod"
                    func = raw.__func__
                elif isinstance(raw, property):
                    raw_type = "property"
                    func = None
                elif inspect.isfunction(raw) or inspect.ismethod(raw):
                    raw_type = "function"
                    func = raw
                else:
                    raw_type = "field"
                    func = None

                if expected_type is not None and raw_type != expected_type:
                    return False

                if expected_sig is not None and func is not None:
                    try:
                        impl_sig = inspect.signature(func)
                    except (ValueError, TypeError):
                        impl_sig = None
                    if impl_sig is None or impl_sig.parameters.keys() != expected_sig.parameters.keys():
                        return False

            elif kind == "property":
                if raw is None:
                    return False
                if not isinstance(raw, property):
                    return False

            elif kind == "field":
                try:
                    if not hasattr(subclass, name):
                        return False

                    value = getattr(subclass, name)

                    if callable(value):
                        return False
                    if isinstance(value, (staticmethod, classmethod, property)):
                        return False

                    if value is Ellipsis:
                        return False

                except Exception:
                    return False

            else:
                try:
                    if not hasattr(subclass, name):
                        return False
                except Exception:
                    return False

        return True
