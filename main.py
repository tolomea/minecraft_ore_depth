import pymclevel
from collections import defaultdict
import csv

block_ids = [
    # proj red ore
    (665, 0, "ruby(pr)"),
    (665, 1, "sapphire(pr)"),
    (665, 2, "peridot(pr)"),
    (665, 3, "copper(pr)"),
    (665, 4, "tin(pr)"),
    (665, 5, "silver(pr)"),
    (665, 6, "electrotine(pr)"),

    # bop gems
    (423, 0, "amethyst(bop)"),
    (423, 2, "ruby(bop)"),
    (423, 4, "peridot(bop)"),
    (423, 6, "topaz(bop)"),
    (423, 8, "tanzanite(bop)"),
    (423, 10, "malachite(bop)"),
    (423, 12, "sapphire(bop)"),
    (423, 14, "amber(bop)"),

    # electricraft ore
    (554, 0, "copper(e)"),
    (554, 1, "tin(e)"),
    (554, 2, "silver(e)"),
    (554, 3, "nickel(e)"),
    (554, 4, "aluminum(e)"),
    (554, 5, "platinum(e)"),

    # reactorcraft ore
    (643, 1, "pitchblende(r1)"),
    (643, 2, "cadmium(r)"),
    (643, 3, "indium(r)"),
    (643, 4, "silver(r)"),
    (643, 5, "pitchblende(r2)"),
    (643, 6, "ammonium chloride(r)"),
    (643, 7, "calcite(r)"),
    (643, 8, "magnetite(r)"),
    (643, 9, "thorite(r)"),
]


def main():
    # sotre the altitude frequency array for each block_id
    res = defaultdict(lambda: [0]*256)

    world = pymclevel.loadWorld("C:\\Users\\tolomea\\AppData\\Roaming\\.minecraft2\\saves\\New World-")
    for i, chunk_loc in enumerate(world.allChunks):
        print i, chunk_loc
        chunk = world.getChunk(*chunk_loc)
        blocks = chunk.Blocks.reshape((256, 256))  # flatten horizontal position
        data = chunk.Data.reshape((256, 256))  # flatten horizontal position
        for key in block_ids:
            block_id, subblock_id, name = key
            mask = (blocks == block_id)
            if subblock_id is not None:
                mask &= (data == subblock_id)
            res[key] += mask.sum(0)

    body = []
    for key in block_ids:
        column = list(key) + list(res[key])
        body.append(column)
    body = zip(*body)
    with open("dump.csv", "wb") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for r in body:
            print r
            writer.writerow(r)


if __name__ == "__main__":
    main()

