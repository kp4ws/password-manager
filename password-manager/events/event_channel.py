'''
Primary Author: Kent Pawson
Contributor(s): N/A
'''

from enum import Enum

class EventChannel(Enum):
    '''
    Contains event names that are used with the event system in the application
    '''
    INDEX_VIEW = 1
    HOME_VIEW = 2
    CREATE_PASSWORD_VIEW = 3
    MODIFY_PASSWORD_VIEW = 4