""" Define interfaces for your add-on.
"""

import zope.interface


class IAddOnInstalled(zope.interface.Interface):
    """ A layer specific for this add-on product.
    """
