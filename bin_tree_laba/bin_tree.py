def gen_bin_tree(height=5, root=1):
    """
    Рекурсивно строит бинарное дерево в виде словаря.
    Если height == 1, возвращается лист.
    Иначе создаются left и right потомки.
    """
    if height < 1:
        return None

    if height == 1:
        return root

    return {
        "root": root,
        "left": gen_bin_tree(height=height - 1, root=root * 2),
        "right": gen_bin_tree(height=height - 1, root=root + 3)
    }


tree = gen_bin_tree(height=5, root=1)
print(tree)