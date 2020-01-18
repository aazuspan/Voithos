def require_attributes(*required_attrs):
    """
    When used as a metaclass, this will raise errors if a class does not define all of the required attributes.
    :param required_attrs: Strings representing attribute names that must be implemented
    :return:
    """
    class RequireAttributesMeta(type):
        def __init__(cls, name, bases, attrs):
            missing_attrs = []
            for attr in required_attrs:
                if attr not in attrs:
                    missing_attrs.append(attr)
            if missing_attrs:
                raise NotImplementedError(f'The following required attributes are missing: {missing_attrs}. Define'
                                          f' those attributes to fix this error.')
    return RequireAttributesMeta
