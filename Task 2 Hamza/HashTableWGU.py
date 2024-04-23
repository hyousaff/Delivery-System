# Name: Hamza Yousaf
# Course: DATA STRUCTURES AND ALGORITHMS II — C950
# Student ID: 011006052
class HashTable:
    def __init__(self, initial_capacity=20):
        """Initializes the hash table with the specified initial capacity.
        The table will contain a list of buckets, each initialized as an empty list."""
        self.table = [[] for _ in range(initial_capacity)]

    def bucket_index(self, key):
        """Private method to calculate the bucket index where a key-value pair should be stored.
        Uses the built-in hash function and modulus operator to find the index."""
        return abs(hash(key)) % len(self.table)


    def delete(self, key):
        """Removes the key-value pair using the provided key.
        If the key is found, the key-value pair is removed from the hash table."""
        index = self.bucket_index(key)
        bucket = self.table[index]

        for i, (a, _) in enumerate(bucket):
            if a == key:
                del bucket[i]  # Remove the key-value pair if the key is found
                return

    def lookup(self, key):
        """Looks up and returns the item associated with the key.
        If the key is not found, returns None."""
        index = self.bucket_index(key)
        bucket = self.table[index]

        for a, b in bucket:
            if a == key:
                return b  # Return the item if the key is found

        return None  # Return None if the key is not found

    def insert(self, key, item):
        """Inserts a new key-value pair into the hash table.
        If the key already exists, updates the item associated with the key."""
        index = self.bucket_index(key)
        bucket = self.table[index]

        # Iterate through the bucket to find the key if it exists
        for ab in bucket:
            if ab[0] == key:
                ab[1] = item # Update existing key-value pair
                return
        # If the key is not found, append the new key-value pair to the bucket
        bucket.append([key, item])



