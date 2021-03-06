"""这是一个模块，提供了一个名为print_lol()的函数，这个函数的作用是打印列表，
其中有可能包含（或不包含）嵌套列表"""

def print_lol(the_list, indent=False, level=0):
    """这个函数取一个位置参数，名为the_list，这可以是任何python列表
    （也可以是包含嵌套列表的列表）。所指定的列表中的每个数据项会（递归）
    输出到屏幕上，各数据项各占一行"""

    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='')
            print(each_item)


# 测试代码
# movies = ['a', 'aa', 'aaa', ['b', 'bb', 'bbb', ['c', 'cc', 'ccc']]]
# print_lol(movies, True)

