"""
Enhanced Personal Task Manager
With categories, due dates, and priority levels
"""

import json
import os
from datetime import datetime, timedelta


class AdvancedTaskManager: print("view_all_tasks") 
def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
        self.categories = ["Work", "Personal", "Study", "Shopping", "Health", "Other"]
    
def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)
    
def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("        ENHANCED TASK MANAGER")
        print("="*50)
        print("1. View All Tasks")
        print("2. Add New Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. View Tasks by Category")
        print("6. View Tasks by Priority")
        print("7. View Today's Tasks")
        print("8. Search Tasks")
        print("9. Task Statistics")
        print("10. Exit")
        print("-"*50)
    
def view_all_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("\n📭 No tasks found!")
            return

        print("\n" + "="*50)
        print("ALL TASKS")
        print("="*50)

        for index, task in enumerate(self.tasks, 1):
            status = "✓" if task['completed'] else "✗"
            priority_icon = "🔴" if task['priority'] == "High" else "🟡" if task['priority'] == "Medium" else "🟢"

            print(f"\n{index}. [{status}] {priority_icon} {task['title']}")
            print(f"   Description: {task['description']}")
            print(f"   Category: {task['category']}")
            print(f"   Priority: {task['priority']}")
            print(f"   Due: {task['due_date']}")
            print(f"   Created: {task['created_date']}")
            if task['completed']:
                print(f"   Completed: {task['completed_date']}")
            print("-" * 40)
    
def add_task(self):
        """Add a new task with enhanced details"""
        print("\n" + "="*50)
        print("ADD NEW TASK")
        print("="*50)
        
        title = input("Enter task title: ").strip()
        if not title:
            print("❌ Task title cannot be empty!")
            return
        
        description = input("Enter task description: ").strip()
        
        # Category selection
        print("\nAvailable categories:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}. {category}")
        
        try:
            cat_choice = int(input("Select category (1-6): "))
            if 1 <= cat_choice <= len(self.categories):
                category = self.categories[cat_choice - 1]
            else:
                category = "Other"
        except (ValueError, IndexError):
            category = "Other"
        
        # Priority selection
        print("\nPriority levels:")
        print("1. High 🔴")
        print("2. Medium 🟡") 
        print("3. Low 🟢")
        
        try:
            pri_choice = int(input("Select priority (1-3): "))
            priority = {1: "High", 2: "Medium", 3: "Low"}.get(pri_choice, "Medium")
        except ValueError:
            priority = "Medium"
        
        # Due date
        print("\nDue date options:")
        print("1. Today")
        print("2. Tomorrow") 
        print("3. Next week")
        print("4. Custom date")
        print("5. No due date")
        
        try:
            date_choice = int(input("Select due date option (1-5): "))
            due_date = self.get_due_date(date_choice)
        except ValueError:
            due_date = "No due date"
        
        new_task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'category': category,
            'priority': priority,
            'due_date': due_date,
            'completed': False,
            'created_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'completed_date': None
        }
        
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"\n✅ Task '{title}' added successfully!")
    
def get_due_date(self, choice):
        """Get due date based on user choice"""
        today = datetime.now()
        
        if choice == 1:
            return today.strftime("%Y-%m-%d")
        elif choice == 2:
            return (today + timedelta(days=1)).strftime("%Y-%m-%d")
        elif choice == 3:
            return (today + timedelta(days=7)).strftime("%Y-%m-%d")
        elif choice == 4:
            custom_date = input("Enter due date (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(custom_date, "%Y-%m-%d")
                return custom_date
            except ValueError:
                print("Invalid date format. Using 'No due date'")
                return "No due date"
        else:
            return "No due date"
    
def mark_completed(self):
        """Mark a task as completed"""
        pending_tasks = [t for t in self.tasks if not t['completed']]

        if not pending_tasks:
            print("\n🎉 No pending tasks available!")
            return

        print("\nPENDING TASKS:")
        for i, task in enumerate(pending_tasks, 1):
            priority_icon = "🔴" if task['priority'] == "High" else "🟡" if task['priority'] == "Medium" else "🟢"
            print(f"{i}. {priority_icon} {task['title']} ({task['category']})")

        try:
            num = int(input("\nEnter task number to mark as completed: "))
            if 1 <= num <= len(pending_tasks):
                task = pending_tasks[num - 1]
                task['completed'] = True
                task['completed_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                print(f"\n✅ Task '{task['title']}' marked as completed!")
            else:
                print("❌ Invalid number!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
def delete_task(self):
        """Delete any task"""
        if not self.tasks:
            print("\n📭 No tasks available!")
            return

        print("\nALL TASKS:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task['completed'] else "✗"
            priority_icon = "🔴" if task['priority'] == "High" else "🟡" if task['priority'] == "Medium" else "🟢"
            print(f"{i}. [{status}] {priority_icon} {task['title']} ({task['category']})")

        try:
            num = int(input("\nEnter task number to delete: "))
            if 1 <= num <= len(self.tasks):
                removed = self.tasks.pop(num - 1)
                self.save_tasks()
                print(f"\n🗑️  Task '{removed['title']}' deleted!")
            else:
                print("❌ Invalid number!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
def view_tasks_by_category(self):
        """View tasks grouped by category"""
        if not self.tasks:
            print("\n📭 No tasks found!")
            return
        
        print("\n" + "="*50)
        print("TASKS BY CATEGORY")
        print("="*50)

        categories = {}
        for task in self.tasks:
            categories.setdefault(task['category'], []).append(task)

        for cat, tasks in sorted(categories.items()):
            print(f"\n📁 {cat.upper()}:")
            print("-" * 30)
            for t in tasks:
                status = "✓" if t['completed'] else "✗"
                icon = "🔴" if t['priority'] == "High" else "🟡" if t['priority'] == "Medium" else "🟢"
                print(f"   [{status}] {icon} {t['title']} (Due: {t['due_date']})")
    
def view_tasks_by_priority(self):
        """View tasks by priority level"""
        if not self.tasks:
            print("\n📭 No tasks found!")
            return

        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        sorted_tasks = sorted(self.tasks, key=lambda x: priority_order[x['priority']])

        print("\n" + "="*50)
        print("TASKS BY PRIORITY")
        print("="*50)

        current = None
        for t in sorted_tasks:
            if t['priority'] != current:
                current = t['priority']
                icon = "🔴" if current == "High" else "🟡" if current == "Medium" else "🟢"
                print(f"\n{icon} {current.upper()} PRIORITY:")
                print("-"*30)

            status = "✓" if t['completed'] else "✗"
            print(f"   [{status}] {t['title']} (Due: {t['due_date']})")
    
def view_todays_tasks(self):
        """View tasks due today"""
        today = datetime.now().strftime("%Y-%m-%d")
        today_tasks = [t for t in self.tasks if t['due_date'] == today]

        print("\n" + "="*50)
        print("TODAY'S TASKS")
        print("="*50)

        if not today_tasks:
            print("\n🎉 No tasks due today!")
            return

        for t in today_tasks:
            status = "✓" if t['completed'] else "✗"
            icon = "🔴" if t['priority'] == "High" else "🟡" if t['priority'] == "Medium" else "🟢"
            print(f"\n{icon} [{status}] {t['title']}")
            print(f"   Category: {t['category']}")
            print(f"   Description: {t['description']}")
            print("-"*40)
    
def search_tasks(self):
        """Search tasks by keyword"""
        if not self.tasks:
            print("\n📭 No tasks available to search!")
            return
        
        keyword = input("Enter search keyword: ").lower().strip()
        if not keyword:
            print("❌ Please enter a keyword!")
            return
        
        matches = [t for t in self.tasks 
                   if keyword in t['title'].lower() 
                   or keyword in t['description'].lower()]

        if not matches:
            print(f"\n❌ No tasks found containing '{keyword}'")
            return

        print("\n" + "="*50)
        print(f"SEARCH RESULTS FOR '{keyword}'")
        print("="*50)

        for t in matches:
            status = "✓" if t['completed'] else "✗"
            icon = "🔴" if t['priority'] == "High" else "🟡" if t['priority'] == "Medium" else "🟢"
            print(f"\n{icon} [{status}] {t['title']}")
            print(f"   Description: {t['description']}")
            print(f"   Category: {t['category']}")
            print(f"   Due: {t['due_date']}")
            print("-"*40)
    
def show_statistics(self):
        """Show statistics of tasks"""
        if not self.tasks:
            print("\n📭 No task data available!")
            return
        
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t['completed']])
        pending = total - completed

        print("\n" + "="*50)
        print("TASK STATISTICS")
        print("="*50)
        print(f"\n📊 Total Tasks: {total}")
        print(f"✅ Completed: {completed}")
        print(f"❌ Pending: {pending}")

        if total > 0:
            print(f"📈 Completion Rate: {completed/total*100:.1f}%")

        print("\n📁 By Category:")
        categories = {}
        for t in self.tasks:
            categories[t['category']] = categories.get(t['category'], 0) + 1

        for cat, count in sorted(categories.items()):
            print(f"   {cat}: {count} tasks")

        print("\n🎯 By Priority:")
        priorities = {}
        for t in self.tasks:
            priorities[t['priority']] = priorities.get(t['priority'], 0) + 1

        for pri in ["High", "Medium", "Low"]:
            if pri in priorities:
                icon = "🔴" if pri == "High" else "🟡" if pri == "Medium" else "🟢"
                print(f"   {icon} {pri}: {priorities[pri]} tasks")
    
def run(self):
        """Main loop"""
        print("\n🚀 Welcome to Enhanced Task Manager!")
        
        while True:
            self.display_menu()

            completed_count = len([t for t in self.tasks if t['completed']])
            print(f"\n📊 Overview: {len(self.tasks)} total tasks ({completed_count} completed, {len(self.tasks) - completed_count} pending)")

            choice = input("\nEnter your choice (1-10): ").strip()

            actions = {
                '1': self.view_all_tasks,
                '2': self.add_task,
                '3': self.mark_completed,
                '4': self.delete_task,
                '5': self.view_tasks_by_category,
                '6': self.view_tasks_by_priority,
                '7': self.view_todays_tasks,
                '8': self.search_tasks,
                '9': self.show_statistics
            }

            if choice == '10':
                print("\n👋 Thank you for using Enhanced Task Manager!")
                self.save_tasks()
                break

            if choice in actions:
                actions[choice]()
            else:
                print("\n❌ Invalid choice, please try again!")

            input("\nPress Enter to continue...")


def main():
    try:
        app = AdvancedTaskManager("View All Tasks")
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Application error: {e}")


if __name__ == "__main__":
    main()