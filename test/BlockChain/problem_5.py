import unittest

from parameterized import parameterized

from src.BlockChain.block_chain import BlockChain


class MyTestCase(unittest.TestCase):

    @parameterized.expand([
        ["Block 1"],
        ["Block 2"],
        ["Block 3"],
        ["A" * 1000]
    ])
    def test_edge_cases(self, test_block):
        blockchain = BlockChain()
        blockchain.add_block(test_block)

        self.assertIn(test_block, blockchain)

    @parameterized.expand([
        [""],
        [" "],
        [None]
    ])
    def test_empty_cases(self, test_block):
        block_chain = BlockChain()
        block_chain.add_block(test_block)
        self.assertIn(test_block, block_chain)

    def test_empty_block_case(self):
        block_chain = BlockChain()

        self.assertEqual(len(block_chain.blocks), 0)


if __name__ == '__main__':
    unittest.main()
