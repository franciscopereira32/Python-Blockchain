import hashlib
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()
       
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
    
my_blockchain = Blockchain()

compra1 = {
    'item': 'honda fit',
    'valor': 100.000,
    'comprador': '@beu_io',
    'vendedor':'@vendedor'
}

doc = {
    'item': 'algum documento importante',
    'valor_pago_ao_cartorio': 100,
    'comprador': '@beu_io',
    'vendedor': '@cartorio'
}

my_blockchain.add_block(Block(1,date.datetime.now(), compra1, my_blockchain.chain[-1].hash))
my_blockchain.add_block(Block(2, date.datetime.now(), doc, my_blockchain.chain[-1].hash))

print(f'Essa blockchain esta valida? {str(my_blockchain.is_valid())}')

def print_blockchain(chain):
    for block in chain:
        print(f"Block #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print(20*'------')
        
print(print_blockchain(my_blockchain.chain))