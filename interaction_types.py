from enum import Enum

from discord import MessageInteraction


class InteractionTypes(Enum):
    TB_GP_LOW = "tb gp low"
    TW_JOIN_STATUS = "tw member"
    OTHER = "(no_special_handling)"

    @classmethod
    def get_interaction_type(cls, interaction: MessageInteraction):
        result = InteractionTypes.OTHER
        if interaction:
            for type in InteractionTypes:
                result = type if type.value == interaction.name else result
        return result
