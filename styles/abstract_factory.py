from abc import ABC, abstractmethod


# 风格抽象工厂，用于设计抽象工厂模式。每个具体工厂创建对应风格的组件。
class StyleFactory(ABC):
    @abstractmethod
    def create_container(self, name, level):
        pass

    @abstractmethod
    def create_leaf(self, name, level):
        pass
