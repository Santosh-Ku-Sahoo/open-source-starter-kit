# Problem: LRU Cache Implementation
# Difficulty: Intermediate
# Approach: OrderedDict for O(1) get and put with LRU eviction
# Time Complexity: O(1) for both get() and put()
# Space Complexity: O(capacity)
#
# Problem Statement:
# Design a Least Recently Used (LRU) cache data structure that supports
# get() and put() operations in O(1) time. When the cache reaches its
# capacity, it should evict the least recently used item before
# inserting a new item.

from collections import OrderedDict


class LRUCache:
    """
    Least Recently Used (LRU) Cache using OrderedDict.
    The most recently accessed items are moved to the end.
    When capacity is exceeded, the first (least recently used) item is evicted.
    """

    def __init__(self, capacity):
        """
        Initializes the LRU cache with the given capacity.

        Args:
            capacity: Maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        Retrieves the value for the given key and marks it as recently used.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key, or -1 if not found.
        """
        if key not in self.cache:
            return -1

        # Move to end to mark as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        Inserts or updates the key-value pair. If the cache is at capacity,
        evicts the least recently used item first.

        Args:
            key: The key to insert or update.
            value: The value to associate with the key.
        """
        if key in self.cache:
            # Update existing key and move to end
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                # Evict least recently used (first item)
                self.cache.popitem(last=False)
            self.cache[key] = value

    def display(self):
        """
        Returns the current cache contents as a string for debugging.

        Returns:
            String representation of cache contents (LRU to MRU order).
        """
        items = [f"{k}: {v}" for k, v in self.cache.items()]
        return "{" + ", ".join(items) + "}"


# ---- Test Cases ----
if __name__ == "__main__":
    cache = LRUCache(3)

    # Insert items
    cache.put(1, "one")
    cache.put(2, "two")
    cache.put(3, "three")
    print(cache.display())          # Expected: {1: one, 2: two, 3: three}

    # Access an item (moves it to most recently used)
    print(cache.get(1))             # Expected: one
    print(cache.display())          # Expected: {2: two, 3: three, 1: one}

    # Insert new item — should evict key 2 (least recently used)
    cache.put(4, "four")
    print(cache.display())          # Expected: {3: three, 1: one, 4: four}
    print(cache.get(2))             # Expected: -1 (evicted)

    # Update existing item
    cache.put(3, "THREE")
    print(cache.display())          # Expected: {1: one, 4: four, 3: THREE}

    # Insert another — should evict key 1
    cache.put(5, "five")
    print(cache.display())          # Expected: {4: four, 3: THREE, 5: five}
    print(cache.get(1))             # Expected: -1 (evicted)

    # Edge case: cache with capacity 1
    tiny_cache = LRUCache(1)
    tiny_cache.put("a", 100)
    print(tiny_cache.get("a"))      # Expected: 100
    tiny_cache.put("b", 200)
    print(tiny_cache.get("a"))      # Expected: -1 (evicted)
    print(tiny_cache.get("b"))      # Expected: 200
