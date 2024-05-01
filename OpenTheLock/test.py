from open_lock import OpenLock

list_deadends = [
    ["0201","0101","0102","1212","2002"],
    ["8888"],
    ["8887","8889","8878","8898","8788","8988","7888","9888"]
]

list_target = ["0202", "0009", "8888"]

list_output = [6, 1, -1]

n = len(list_deadends)


for i in range(n):
    deadends = list_deadends[i]
    target = list_target[i]
    output = list_output[i]
    op = OpenLock(deadends=deadends, target=target)

    try:
        result = op.result()
        assert result == output
        print(f'SUCCESS case {i+1}: target = {target}, output = {output}')
    except AssertionError:
        print(f'FAILED case {i+1}: target = {target}, output = {result}, except = {output}')
