from .container import Container


class ConcreteContainer(Container):
    def __init__(self, name, level, style):
        super().__init__(name, level, style)

    def draw(self, prefix, is_last):
        """
        绘制container，根据样式不同绘制树形或矩形。

        :param prefix: 前缀
        :param is_last: 是否是当前层级的最后一个元素
        """
        if self.style == 'tree':
            connector = '└─' if is_last else '├─'
            print(f"{prefix}{connector} {self.icon}{self.name}")
        elif self.style == 'rectangle':
            connector = '├─'
            if self.level == 0:
                # 绘制顶层container
                context = f"{prefix}{self.icon}{self.name} "
                border = '─' * (50 - len(context))
                if prefix == '┌─ ':
                    print(context + f"{border}┐")
                else:
                    print(context + f"{border}┤")
            else:
                # 绘制非顶层container
                context = f"{prefix}{connector} {self.icon}{self.name} "
                border = '─' * (50 - len(context))
                print(context + f"{border}┤")
