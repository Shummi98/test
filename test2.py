import json
import os
import random
import time
from datetime import datetime
class TaskManager:
"""Manages a persistent, terminal-based to-do list with performance metrics."""
def init(self, filename="tasks.json"):
self.filename = filename
self.tasks = self._load_tasks()
def _load_tasks(self):
if os.path.exists(self.filename):
try:
with open(self.filename, 'r') as f:
return json.load(f)
except json.JSONDecodeError:
print("⚠️ Error reading storage file. Starting fresh.")
return []
def _save_tasks(self):
with open(self.filename, 'w') as f:
json.dump(self.tasks, f, indent=4)
def add_task(self, description, priority="Medium"):
task = {
"id": len(self.tasks) + 1,
"description": description,
"priority": priority.capitalize(),
"completed": False,
"created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
}
self.tasks.append(task)
self._save_tasks()
print(f"✅ Added: "{description}" [{priority}]")
def list_tasks(self, include_completed=False):
visible_tasks = [t for t in self.tasks if include_completed or not t["completed"]]
if not visible_tasks:
print("📭 No tasks found matching the criteria.")
return
print(f"\n{'ID':<5} {'Status':<10} {'Priority':<10} {'Created':<18} {'Description'}")
print("-" * 70)
for t in visible_tasks:
status = "🟢 Done" if t["completed"] else "🔴 Pending"
print(f"{t['id']:<5} {status:<10} {t['priority']:<10} {t['created_at']:<18} {t['description']}")
print()
def complete_task(self, task_id):
for t in self.tasks:
if t["id"] == task_id:
if t["completed"]:
print("ℹ️ Task is already completed.")
return
t["completed"] = True
self._save_tasks()
print(f"🎉 Task {task_id} marked as completed!")
return
print("❌ Task ID not found.")
def show_metrics(self):
total = len(self.tasks)
if total == 0:
print("📈 No data available to calculate metrics.")
return
completed = sum(1 for t in self.tasks if t["completed"])
rate = (completed / total) * 100
print("\n--- Productivity Metrics ---")
print(f"📊 Completion Rate: {rate:.1f}%")
print(f"✅ Completed Tasks: {completed}")
print(f"⏳ Pending Tasks: {total - completed}")
# Simple motivational generator based on performance
quotes = [
"Keep pushing forward!",
"Small steps lead to big results.",
"You are doing great!",
"Productivity is intentional choices."
]
print(f"💡 Quote of the day: {random.choice(quotes)}\n")
def main():
manager = TaskManager()
print("🚀 Welcome to PyManager v1.0")
while True:
print("1. Add Task 2. List Pending 3. List All 4. Complete Task 5. Metrics 6. Exit")
choice = input("Select an option (1-6): ").strip()
if choice == "1":
desc = input("Enter task description: ").strip()
prior = input("Enter priority (Low, Medium, High): ").strip()
if desc:
manager.add_task(desc, prior if prior else "Medium")
elif choice == "2":
manager.list_tasks(include_completed=False)
elif choice == "3":
manager.list_tasks(include_completed=True)
elif choice == "4":
try:
tid = int(input("Enter Task ID to complete: "))
manager.complete_task(tid)
except ValueError:
print("❌ Please enter a valid numerical ID.")
elif choice == "5":
manager.show_metrics()
elif choice == "6":
print("👋 Goodbye! Stay productive.")
break
else:
print("⚠️ Invalid selection. Try again.")
time.sleep(0.5)
if name == "main":
main()

