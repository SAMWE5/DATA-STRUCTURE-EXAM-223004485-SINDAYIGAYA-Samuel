# Bubble Sort Implementation for Sorting Tasks by Priority
class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __repr__(self):
        return f"({self.priority}, {self.description})"

def bubble_sort_tasks(tasks):
    n = len(tasks)
    for i in range(n):
       
        for j in range(0, n-i-1):
            if tasks[j].priority > tasks[j+1].priority:
                
                tasks[j], tasks[j+1] = tasks[j+1], tasks[j]


tasks = [
    Task(4, "Update Bread Prices"),
    Task(1, "Restock Milk"),
    Task(3, "Order New Apples"),
    Task(5, "Discount on Chicken"),
    Task(2, "Check Rice Inventory"),
]

print("\nUnsorted Tasks:")
print(tasks)

bubble_sort_tasks(tasks)

print("\nSorted Tasks by Priority (Lowest to Highest):")
print(tasks)
