def classFactory(iface):
    from .burn_mapper import BurnMapperPlugin
    return BurnMapperPlugin(iface)