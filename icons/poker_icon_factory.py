import json

from .icon_factory import IconFactory


# 加载图标簇
def load_icon_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


class PokerIconFactory(IconFactory):
    def __init__(self, config):
        self.config = load_icon_config(config)

    def get_icon(self, is_leaf):
        if 'poker' in self.config:
            if is_leaf:
                return self.config['poker']['leaf']
            else:
                return self.config['poker']['container']
        else:
            raise ValueError(f"Icon family '{'poker'}' not found in the config")
