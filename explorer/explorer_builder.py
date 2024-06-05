from explorer.explorer import FunnyJsonExplorer


# 建造者类，用于设计建造者模式，将类的构建步骤分开
class ExplorerBuilder:
    def __init__(self):
        self._style_factory = None
        self._icon_factory = None

    def set_style_factory(self, style_factory):
        self._style_factory = style_factory
        return self

    def set_icon_factory(self, icon_factory):
        self._icon_factory = icon_factory
        return self

    def build(self):
        return FunnyJsonExplorer(self._style_factory, self._icon_factory)
