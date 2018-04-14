import hashlib
import datetime

# Datastructure
class Block:

    def __init__(self, index, prevHash, timestamp, data):

        self.index = index
        self.prevHash = prevHash
        self.timestamp = timestamp
        self.data = data


    def createHash(self, block):

        hashblock = str(block.index) + str(block.data) + str(block.prevHash) + str(block.timestamp)
        sha = hashlib.sha256()
        sha.update(hashblock.encode('utf-8'))
        self.hash = sha.hexdigest()

# Chain blocks
def nextBlock(block):
    timestamp = datetime.datetime.now()
    print((timestamp))

    index = block.index
    data = 1562

    n_block = Block(block.index + 1,
                    block.hash,
                    timestamp,
                    data)
    return n_block



if __name__ == '__main__':
    block = Block(1,12,13,11)
    prevhash = block.createHash()
    print(prevhash)
    print("Rishabh is a tool")