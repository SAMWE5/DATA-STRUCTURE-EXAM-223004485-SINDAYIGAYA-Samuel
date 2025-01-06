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

# Example Usage
print("Product Inventory (BST):")
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
