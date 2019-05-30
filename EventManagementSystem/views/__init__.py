# The urls.py searches in the init file of views folder, if it cannot find views.py
# Every method that is used in elsewhere needs to be imported here, that way it does not need to change the path.

from . import association
from . import district
from . import province
from . import slkf
from . import genericUser
