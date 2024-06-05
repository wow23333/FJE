from abc import ABC, abstractmethod


# 图标簇抽象工厂，用于设计工厂方法模式
class IconFactory(ABC):
    @abstractmethod
    def get_icon(self, is_leaf):
        pass
