import datetime

from src.BlockChain.block import Block
from src.LinkedList.linked_list import LinkedList


class BlockChain:
    def __init__(self):
        self.blocks = LinkedList()

    def add_block(self, data):
        current_time = datetime.datetime.utcnow()

        if len(self.blocks) == 0:
            self.blocks.append(Block(current_time, data, 0))
        else:
            new_block = Block(current_time, data, self.blocks.tail.value.hash)
            self.blocks.append(new_block)

    def print_blocks(self):
        current_block = self.blocks.head
        while current_block:
            print("Index:", self.blocks.index(current_block.value))
            print("Timestamp:", current_block.value.timestamp)
            print("Data:", current_block.value.data)
            print("Previous Hash:", current_block.value.previous_hash)
            print("Hash:", current_block.value.hash)
            print()
            current_block = current_block.next

    def __contains__(self, item):
        current_block = self.blocks.head
        while current_block:
            if item == current_block.value.data:
                return True
        return False


# Sample 1: Adding blocks to the blockchain
blockchain = BlockChain()
blockchain.add_block("Block 0")
blockchain.add_block("Block 1")
blockchain.add_block("Block 2")
blockchain.print_blocks()

# Sample 2: Edge case - Empty data
blockchain_empty = BlockChain()
blockchain_empty.add_block("")  # Adding an empty block
blockchain_empty.print_blocks()

# Sample 3: Edge case - Large data
blockchain_large = BlockChain()
large_data = "A" * 1000  # Creating a large data string
blockchain_large.add_block(large_data)
blockchain_large.print_blocks()
