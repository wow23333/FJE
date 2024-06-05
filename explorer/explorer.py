import json


class FunnyJsonExplorer:
    def __init__(self, style_factory, icon_factory):
        self.style_factory = style_factory  # 风格
        self.icon_factory = icon_factory  # 图标簇
        self.is_first_line = True  # 是否是第一行

    # 从文件加载JSON数据
    def _load(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    # 显示文件内容
    def show(self, file_path):
        data = self._load(file_path)
        self.show_data(data)

    def show_data(self, data, level=0, prefix='', is_last=True, is_last_line=None):
        # is_last_line用于判断是否是最后一行，只有元组内的所有元素都是True，表示字典嵌套结构中每一个都是最后一个，此时是最后一行
        if is_last_line is None:
            is_last_line = ()

        global container, new_prefix

        items = list(data.items())
        for index, (key, value) in enumerate(items):
            is_last_item = (index == len(items) - 1)  # 判断是否是当前层级的最后一个项
            is_last_line += (is_last_item,)

            if isinstance(value, dict):
                container = self.style_factory.create_container(key, level)
                container.icon = self.icon_factory.get_icon(is_leaf=False)

                # 设置前缀符号
                if container.style == "tree":
                    if level == 0:
                        new_prefix = prefix + ('' if is_last else '│  ')
                    else:
                        new_prefix = prefix + ('   ' if is_last else '│  ') + ' ' * len(container.icon)
                elif container.style == "rectangle":
                    if level == 0:
                        if self.is_first_line:
                            self.is_first_line = False
                            new_prefix = '┌─ '
                        else:
                            new_prefix = '├─ '
                    elif level == 1:
                        new_prefix = '│  ' + ' ' * len(container.icon)
                    else:
                        new_prefix = prefix + '│  ' + ' ' * len(container.icon)
                container.draw(new_prefix, is_last_item)
                self.show_data(value, level + 1, new_prefix, is_last_item, is_last_line)
                is_last_line = is_last_line[:-1]  # 弹出最后一个元素
            else:
                leaf = self.style_factory.create_leaf(key, level + 1)  # 创建叶子节点
                leaf.icon = self.icon_factory.get_icon(is_leaf=True)
                if value is not None:
                    leaf.name += f': {value}'

                if container.style == "tree":
                    leaf.draw(prefix + (' ' if is_last else '│') + ' ' * len(leaf.icon), is_last_item)
                elif container.style == "rectangle":
                    is_last_leaf = True
                    for e in is_last_line:
                        if not e:
                            is_last_leaf = False
                            break

                    is_last_line = is_last_line[:-1]  # 弹出最后一个元素

                    # 处理特殊情况
                    if '├─' in prefix:  # 第二次及以后出现的第1级的第一行为叶子节点
                        prefix = prefix.replace('├─', '│ ') + ' ' * len(leaf.icon)
                    elif '┌─' in prefix:  # 只有两行的情况
                        prefix = prefix.replace('┌─', '│ ') + ' ' * len(leaf.icon)

                    if is_last_leaf:  # 最后一行
                        prefix = prefix.replace('│', '└', 1)
                        prefix = prefix.replace('│', '┴')
                        prefix = prefix.replace(' ', '─')
                        if level > 1:
                            prefix += '┴──' + '─' * len(leaf.icon)
                        leaf.draw(prefix, is_last_leaf)
                    else:
                        if level == 1:
                            leaf.draw(prefix, is_last_leaf)
                        else:
                            leaf.draw(prefix + '│  ' + ' ' * len(leaf.icon), is_last_leaf)
