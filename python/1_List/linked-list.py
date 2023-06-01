class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        curr = self
        s = f"[{curr.val}"
        while curr.next:
            curr = curr.next
            s += f",{curr.val}"
        return f"{s}]"

    @staticmethod
    def from_list(vals):
        head = Node(vals[0])
        for val in vals[1:]:
            head.insert(val)
        return head

    def insert(self, val) -> None:
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    @staticmethod
    def reverse(head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


if __name__ == "__main__":
    head = Node.from_list([1])
    print(head)
    head.insert(4)
    print(head)
    print(Node.reverse(head))
