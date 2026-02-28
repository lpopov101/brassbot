def create_level_list() -> List[int]:
    level_list = []
    cur_level = -10
    for _ in range(0, 11):
        level_list.append(cur_level)
        cur_level += 1

    indices_remaining = 2
    for _ in range(11, 31):
        level_list.append(cur_level)
        indices_remaining -= 1
        if indices_remaining == 0:
            cur_level += 1
            indices_remaining = 2

    indices_remaining = 3
    for _ in range(31, 61):
        level_list.append(cur_level)
        indices_remaining -= 1
        if indices_remaining == 0:
            cur_level += 1
            indices_remaining = 3

    indices_remaining = 4
    for _ in range(61, 97):
        level_list.append(cur_level)
        indices_remaining -= 1
        if indices_remaining == 0:
            cur_level += 1
            indices_remaining = 4

    indices_remaining = 3
    for _ in range(97, 100):
        level_list.append(cur_level)
        indices_remaining -= 1
        if indices_remaining == 0:
            cur_level += 1
            indices_remaining = 3

    return level_list


class Income:
    def __init__(self):
        self.level_list = create_level_list()
        self.cur_index = 10

    def get_level(self) -> int:
        index = min(max(0, self.cur_index), len(self.level_list) - 1)
        return self.level_list[index]

    def increase(self, amount: int):
        self.cur_index += amount
        self.cur_index = min(self.cur_index, len(self.level_list) - 1)

    def take_loan(self):
        cur_level = self.get_level()
        new_level = max(cur_level - 3, -10)
        while self.get_level() > new_level:
            index -= 1
