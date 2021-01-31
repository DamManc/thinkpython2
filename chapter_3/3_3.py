#Chapter 3
#Ex: 3_3
#1
def print_el_ori_one(v_1, v_2):
    print(v_1, v_2, end=' ')
def print_el_ori_two(v_2):
    print(v_2, v_2, v_2, end=' ')
def print_el_one_row(f_0, f_1, v_1, v_2):
    f_0(v_1, v_2)
    f_1(v_2)
def print_row(v_1, v_2, v_3):
    print_el_one_row(print_el_ori_one, print_el_ori_two, v_1, v_2)
    print_el_one_row(print_el_ori_one, print_el_ori_two, v_1, v_2)
    print(v_3)
def print_el_ver_one(v_4):
    print(v_4, ' ' * 7, v_4, ' ' * 7, v_4)
def print_ver(f_2, v_4):
    f_2(v_4)
    f_2(v_4)
    f_2(v_4)
    f_2(v_4)
def print_grid():
    print_row('+', '-', '+')
    print_ver(print_el_ver_one, '|')
    print_row('+', '-', '+')
    print_ver(print_el_ver_one, '|')
    print_row('+', '-', '+')
print_grid()
