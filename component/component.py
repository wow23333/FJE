from abc import ABC, abstractmethod


# 组件类，用于设计组合模式
class Component(ABC):
    def __init__(self, name, level, style):
        self.name = name  # 文件对应的行内容
        self.level = level  # 层级
        self.style = style  # 风格（树形或矩形）
        self.icon = None  # 图标

    @abstractmethod
    def draw(self, prefix, is_last):
        pass
