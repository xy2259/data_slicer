"""
Subclass of ViewBox with custom menu items.
"""
import logging

from pyqtgraph.Qt import QtGui
from pyqtgraph.graphicsItems.ViewBox import ViewBox, ViewBoxMenu

logger = logging.getLogger('ds.'+__name__)

class DSViewBoxMenu(ViewBoxMenu.ViewBoxMenu) :
    """ Subclass of ViewBoxMenu with custom menu items. """
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)

        # Define own menu entries
        self.mpl_export = QtGui.QAction('MPL export', self)

class DSViewBox(ViewBox) :
    """
    Subclass of ViewBox with custom menu items, as defined in `DSViewBoxMenu 
    <data_slicer.dsviewbox.DSViewBoxMenu>`.
    """
    def __init__(self, imageplot, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        logger.debug(imageplot)
        self.imageplot = imageplot

        # Connect signal handling and make the menu entry appear
        self.menu = DSViewBoxMenu(self)
        self.menu.mpl_export.triggered.connect(self.imageplot.mpl_export)
        self.menu.addAction(self.menu.mpl_export)

