from open_lock import OpenLock, DEFAULT_COUNT

list_deadends = [
    ["0201","0101","0102","1212","2002"],
    ["8888"],
    ["8887","8889","8878","8898","8788","8988","7888","9888"]
]

list_target = ["0202", "0009", "8888"]

list_output = [6, 1, DEFAULT_COUNT]

n = len(list_deadends)


for i in range(n):
    deadends = list_deadends[i]
    target = list_target[i]
    output = list_output[i]
    op = OpenLock(deadends=deadends, target=target)

    try:
        level = op.get_level()
        paths = op.get_paths()
        assert level == output
        print(f'Case {i+1}: Target = {target} SUCCESS')
        print(f'Total Minimal Moves = {output} \nPaths = {paths}')
        print('****\t****\t****')
    except AssertionError:
        print(f'FAILED case {i+1}: target = {target}, output = {level}, except = {output}')
