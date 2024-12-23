class Mem:
    def __init__(self, pos, length):
        self.pos = pos
        self.length = length

    def val(self):
        return (2 * self.pos + self.length - 1) * self.length // 2

def get_memory(disk):
    pos, mem = 0, []
    for length in disk:
        mem.append(Mem(pos, length))
        pos += length
    return mem

def part_one(disk):
    F, S, p = [], [], 0
    for i, c in enumerate(disk):
        (F if i % 2 == 0 else S).append(list(range(p, p + c)))
        p += c
    S = sum(S, [])
    for f in reversed(F):
        for x in reversed(range(len(f))):
            if len(S) and f[x] > S[0]:
                f[x] = S[0]
                S = S[1:]
    return sum(i * j for i, f in enumerate(F) for j in f)

def part_two(disk):
    mem = get_memory(disk)
    for used in reversed(mem[::2]):
        for free in mem[1::2]:
            if free.pos <= used.pos and free.length >= used.length:
                used.pos = free.pos
                free.pos += used.length
                free.length -= used.length
                break
    return sum(id * m.val() for id, m in enumerate(mem[::2]))

def main():
    with open("data_files/data_day9.txt") as f:
        disk = list(map(int, f.read().strip()))
    
    print(f"Part 1 Checksum: {part_one(disk)}")
    print(f"Part 2 Checksum: {part_two(disk)}")

if __name__ == "__main__":
    main()