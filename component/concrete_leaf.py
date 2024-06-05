from .leaf import Leaf


class ConcreteLeaf(Leaf):
    def __init__(self, name, level, style):
        super().__init__(name, level, style)

    def draw(self, prefix, is_last):
        """
        绘制container，根据样式不同绘制树形或矩形。

        :param prefix: 前缀，用于对齐显示
        :param is_last: tree风格为是否是当前层级的最后一个元素；rectangle风格为是否是全局最后一个元素
        """
        if self.style == 'tree':
            connector = '└─' if is_last else '├─'  # is_last为True表示当前container对应的最后一个叶子节点
            print(f"{prefix}  {connector} {self.icon}{self.name}")
        elif self.style == 'rectangle':
            if is_last:  # is_last为True全局最后一个叶子节点，与tree风格不同
                connector = '┴─'
                context = f"{prefix}{connector} {self.icon}{self.name} "
                print(context + f"{'─' * (50 - len(context))}┘")
            else:
                connector = '├─'
                context = f"{prefix}{connector} {self.icon}{self.name} "
                print(context + f"{'─' * (50 - len(context))}┤")
