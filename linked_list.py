# Problem: Linked List Implementation
# Difficulty: Intermediate
# Approach: Singly linked list with Node and LinkedList classes
# Time Complexity: Append O(n), Prepend O(1), Delete O(n),
#                  Search O(n), Reverse O(n), Length O(n)
# Space Complexity: O(n)
#
# Problem Statement:
# Implement a singly linked list with the following operations:
# append, prepend, delete, search, display, reverse, and length.

class Node:
    """Represents a single node in the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """Singly linked list with common operations."""

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Adds a new node with the given data at the end of the list.

        Args:
            data: Value to store in the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """
        Adds a new node with the given data at the beginning of the list.

        Args:
            data: Value to store in the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """
        Deletes the first node containing the given data.

        Args:
            data: Value to delete from the list.

        Returns:
            True if the node was found and deleted, False otherwise.
        """
        if not self.head:
            return False

        # Deleting the head node
        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def search(self, data):
        """
        Searches for a node containing the given data.

        Args:
            data: Value to search for.

        Returns:
            True if found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """
        Returns a string representation of the linked list.

        Returns:
            String in the format "1 -> 2 -> 3 -> None".
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"

    def reverse(self):
        """
        Reverses the linked list in-place.
        """
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def length(self):
        """
        Returns the number of nodes in the linked list.

        Returns:
            Integer count of nodes.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# ---- Test Cases ----
if __name__ == "__main__":
    ll = LinkedList()

    # Test append
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll.display())        # Expected: 1 -> 2 -> 3 -> None

    # Test prepend
    ll.prepend(0)
    print(ll.display())        # Expected: 0 -> 1 -> 2 -> 3 -> None

    # Test length
    print(f"Length: {ll.length()}")  # Expected: Length: 4

    # Test search
    print(f"Search 2: {ll.search(2)}")   # Expected: True
    print(f"Search 5: {ll.search(5)}")   # Expected: False

    # Test delete
    ll.delete(2)
    print(ll.display())        # Expected: 0 -> 1 -> 3 -> None

    ll.delete(0)
    print(ll.display())        # Expected: 1 -> 3 -> None

    ll.delete(5)               # Non-existent — no change
    print(ll.display())        # Expected: 1 -> 3 -> None

    # Test reverse
    ll.append(4)
    ll.append(5)
    print(ll.display())        # Expected: 1 -> 3 -> 4 -> 5 -> None
    ll.reverse()
    print(ll.display())        # Expected: 5 -> 4 -> 3 -> 1 -> None

    # Test empty list
    empty_ll = LinkedList()
    print(empty_ll.display())            # Expected: None
    print(f"Length: {empty_ll.length()}") # Expected: Length: 0
    print(f"Delete: {empty_ll.delete(1)}")  # Expected: Delete: False
