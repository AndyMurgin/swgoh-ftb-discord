from jproperties import Properties


class PropertiesHolder:
    def __init__(self):
        self.properties = Properties()

    def get_property_value(self, key: str) -> str:
        return self.properties.get(key).data


def init_and_get_properties_holder(properties_file: str) -> PropertiesHolder:
    holder = PropertiesHolder()
    init_properties(properties_file, holder)
    return holder


def init_properties(properties_file: str, holder: PropertiesHolder):
    with open(properties_file, "rb") as properties_file:
        holder.properties.load(properties_file, encoding="utf-8")
