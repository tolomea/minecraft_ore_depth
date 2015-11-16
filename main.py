import pymclevel
from collections import defaultdict

block_ids = range(10)

# sotre the altitude frequency array for each block_id
res = defaultdict(lambda: [0]*256)

def main():
    world = pymclevel.loadWorld("C:\\Users\\tolomea\\AppData\\Roaming\\.minecraft2\\saves\\New World-")
    for i, chunk_loc in enumerate(world.allChunks):
        print i, chunk_loc
        data = world.getChunk(*chunk_loc).Blocks
        data = data.reshape((256, 256))  # flatten horizontal position
        for block_id in block_ids:
            res[block_id] += (data == block_id).sum(0)

    for block_id in block_ids:
        print block_id, res[block_id]


if __name__ == "__main__":
    main()

