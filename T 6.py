# AI-Based Personal Shopping Assistant for Nakumatt Supermarket


class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

class BSTNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

class ProductInventory:
    def __init__(self):
        self.root = None

    def insert(self, product):
        if self.root is None:
            self.root = BSTNode(product)
        else:
            self._insert(self.root, product)

    def _insert(self, node, product):
        if product.price < node.product.price:
            if node.left is None:
                node.left = BSTNode(product)
            else:
                self._insert(node.left, product)
        else:
            if node.right is None:
                node.right = BSTNode(product)
            else:
                self._insert(node.right, product)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.product.name, node.product.category, node.product.price))
            self._inorder(node.right, result)

class Purchase:
    def __init__(self, user_id, product_name, quantity):
        self.user_id = user_id
        self.product_name = product_name
        self.quantity = quantity

class AVLNode:
    def __init__(self, purchase):
        self.purchase = purchase
        self.height = 1
        self.left = None
        self.right = None

class UserHistory:
    def __init__(self):
        self.root = None

    def insert(self, purchase):
        self.root = self._insert(self.root, purchase)

    def _insert(self, node, purchase):
        if not node:
            return AVLNode(purchase)
        if purchase.product_name < node.purchase.product_name:
            node.left = self._insert(node.left, purchase)
        else:
            node.right = self._insert(node.right, purchase)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

       
        balance = self._get_balance(node)

        if balance > 1 and purchase.product_name < node.left.purchase.product_name:
            return self._right_rotate(node)
        if balance < -1 and purchase.product_name > node.right.purchase.product_name:
            return self._left_rotate(node)
        if balance > 1 and purchase.product_name > node.left.purchase.product_name:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and purchase.product_name < node.right.purchase.product_name:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.purchase.user_id, node.purchase.product_name, node.purchase.quantity))
            self._inorder(node.right, result)


import heapq

class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        return self.priority < other.priority

class TaskHeap:
    def __init__(self):
        self.heap = []

    def add_task(self, task):
        heapq.heappush(self.heap, task)

    def get_highest_priority_task(self):
        return heapq.heappop(self.heap) if self.heap else None

    def display_tasks(self):
        return [(task.priority, task.description) for task in self.heap]


class Order:
    def __init__(self, order_id, product_name, quantity):
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.next = None

class OrderList:
    def __init__(self, max_orders):
        self.head = None
        self.size = 0
        self.max_orders = max_orders

    def add_order(self, order):
        if self.size == self.max_orders:
            print("Order list is full. Remove an order before adding a new one.")
            return

        if not self.head:
            self.head = order
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = order

        self.size += 1

    def remove_order(self):
        if not self.head:
            print("Order list is empty.")
            return

        self.head = self.head.next
        self.size -= 1

    def display_orders(self):
        current = self.head
        orders = []
        while current:
            orders.append((current.order_id, current.product_name, current.quantity))
            current = current.next
        return orders

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BinaryTreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = BinaryTreeNode(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(data)
            else:
                self._insert(node.right, data)

    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)

 
class HierarchicalTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class HierarchicalTree:
    def __init__(self):
        self.root = None

    def add_root(self, data):
        self.root = HierarchicalTreeNode(data)

    def add_child(self, parent_data, child_data):
        parent_node = self._find(self.root, parent_data)
        if parent_node:
            parent_node.children.append(HierarchicalTreeNode(child_data))

    def _find(self, node, data):
        if not node:
            return None
        if node.data == data:
            return node
        for child in node.children:
            found = self._find(child, data)
            if found:
                return found
        return None

    def display_hierarchy(self, node=None, level=0):
        if node is None:
            node = self.root
        print("  " * level + str(node.data))
        for child in node.children:
            self.display_hierarchy(child, level + 1)


print("\nProduct Inventory (BST):")
inventory = ProductInventory()
inventory.insert(Product("Milk", "Dairy", 1200))
inventory.insert(Product("Bread", "Bakery", 800))
inventory.insert(Product("Apples", "Produce", 1500))
inventory.insert(Product("Chicken", "Meat", 5500))
inventory.insert(Product("Rice", "Grains", 3000))
print("Inorder Traversal of Products:", inventory.inorder())

print("\nUser Purchase History (AVL):")
history = UserHistory()
history.insert(Purchase(1, "Milk", 2))
history.insert(Purchase(2, "Rice", 1))
history.insert(Purchase(1, "Bread", 3))
history.insert(Purchase(3, "Apples", 5))
history.insert(Purchase(2, "Chicken", 1))
print("Inorder Traversal of User Histories:", history.inorder())

print("\nTask Prioritization (Heap):")
task_manager = TaskHeap()
task_manager.add_task(Task(1, "Restock Milk"))
task_manager.add_task(Task(3, "Order New Apples"))
task_manager.add_task(Task(2, "Check Rice Inventory"))
task_manager.add_task(Task(5, "Discount on Chicken"))
task_manager.add_task(Task(4, "Update Bread Prices"))
print("Current Tasks:", task_manager.display_tasks())
highest_priority = task_manager.get_highest_priority_task()
if highest_priority:
    print("Highest Priority Task:", (highest_priority.priority, highest_priority.description))

print("\nFixed Orders (Linked List):")
order_list = OrderList(max_orders=3)
order_list.add_order(Order(1, "Milk", 2))
order_list.add_order(Order(2, "Rice", 1))
order_list.add_order(Order(3, "Bread", 3))
order_list.add_order(Order(4, "Chicken", 1))  
print("Current Orders:", order_list.display_orders())
order_list.remove_order()
print("Orders after removing one:", order_list.display_orders())

print("\nDynamic Tracking of Data (Binary Tree):")
data_tree = BinaryTree()
data_tree.insert("CustomerA")
data_tree.insert("CustomerB")
data_tree.insert("CustomerC")
data_tree.insert("CustomerD")
data_tree.insert("CustomerE")
print("Inorder Traversal of Customer Data:", data_tree.inorder_traversal())

print("\nHierarchical Data Representation (Tree):")
hierarchy = HierarchicalTree()
hierarchy.add_root("Nakumatt")
hierarchy.add_child("Nakumatt", "Electronics")
hierarchy.add_child("Nakumatt", "Groceries")
hierarchy.add_child("Nakumatt", "Clothing")
hierarchy.add_child("Groceries", "Fruits")
hierarchy.add_child("Groceries", "Vegetables")
hierarchy.add_child("Clothing", "Men")
hierarchy.add_child("Clothing", "Women")
hierarchy.display_hierarchy()
