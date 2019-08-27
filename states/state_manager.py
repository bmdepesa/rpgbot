from enum import Enum

import util.slack_api as slack_api

class GameState(Enum):
    ALL = "all"
    TOWN = "town"
    ADVENTURE = "adventure"
    COMBAT = "combat"
    POST_COMBAT = "post_combat"
    IN_GROUP = "in_group"

def process_current_state():
    return None