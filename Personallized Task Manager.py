"""
Enhanced Personal Task Manager
With categories, due dates, and priority levels
"""

import json
import os
from datetime import datetime, timedelta

class AdvancedTaskManager:
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
    
    def add_task(self):
        """Add a new task with enhanced details"""
        print("\n" + "="*50)
        print("ADD NEW TASK")
        print("="*50)
        
        title = input("Enter task title: ").strip()
        if not title:
            print("Task title cannot be empty!")
            return
        
        description = input("Enter task description: ").strip()
        
        # Category selection
        print("\nAvailable categories:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}. {category}")
        
        try:
            cat_choice = int(input("Select category (1-6): "))
            category = self.categories[cat_choice - 1] if 1 <= cat_choice <= 6 else "Other"
        except (ValueError, IndexError):
            category = "Other"
        
        # Priority selection
        print("\nPriority levels:")
        print("1. High 🔴")
        print("2. Medium 🟡") 
        print("3. Low 🟢")
        
        try:
            pri_choice = int(input("Select priority (1-3): "))
            priority_levels = {1: "High", 2: "Medium", 3: "Low"}
            priority = priority_levels.get(pri_choice, "Medium")
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
        print(f"✅ Task '{title}' added successfully!")
    
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
            custom_date = input("Enter due date (YYYY-MM-DD): ")
            return custom_date
        else:
            return "No due date"
    
    def view_tasks_by_category(self):
        """View tasks grouped by category"""
        if not self.tasks:
            print("No tasks found!")
            return
        
        tasks_by_category = {}
        for task in self.tasks:
            category = task['category']
            if category not in tasks_by_category:
                tasks_by_category[category] = []
            tasks_by_category[category].append(task)
        
        print("\n" + "="*50)
        print("TASKS BY CATEGORY")
        print("="*50)
        
        for category, tasks in tasks_by_category.items():
            print(f"\n📁 {category.upper()}:")
            print("-" * 30)
            for task in tasks:
                status = "✓" if task['completed'] else "✗"
                priority_icon = "🔴" if task['priority'] == "High" else "🟡" if task['priority'] == "Medium" else "🟢"
                print(f"   [{status}] {priority_icon} {task['title']} (Due: {task['due_date']})")
    
    def view_tasks_by_priority(self):
        """View tasks grouped by priority"""
        if not self.tasks:
            print("No tasks found!")
            return
        
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        sorted_tasks = sorted(self.tasks, key=lambda x: priority_order[x['priority']])
        
        print("\n" + "="*50)
        print("TASKS BY PRIORITY")
        print("="*50)
        
        current_priority = None
        for task in sorted_tasks:
            if task['priority'] != current_priority:
                current_priority = task['priority']
                priority_icon = "🔴" if current_priority == "High" else "🟡" if current_priority == "Medium" else "🟢"
                print(f"\n{priority_icon} {current_priority.upper()} PRIORITY:")
                print("-" * 30)
            
            status = "✓" if task['completed'] else "✗"
            print(f"   [{status}] {task['title']} - {task['category']} (Due: {task['due_date']})")
    
    def view_todays_tasks(self):
        """View tasks due today"""
        today = datetime.now().strftime("%Y-%m-%d")
        todays_tasks = [task for task in self.tasks if task['due_date'] == today]
        
        if not todays_tasks:
            print("No tasks due today! 🎉")
            return
        
        print("\n" + "="*50)
        print("TODAY'S TASKS")
        print("="*50)
        
        for task in todays_tasks:
            status = "✓" if task['completed'] else "✗"
            priority_icon = "🔴" if task['priority'] == "High" else "🟡" if task['priority'] == "Medium" else "🟢"
            print(f"{priority_icon} [{status}] {task['title']}")
            print(f"   Category: {task['category']}")
            print(f"   Description: {task['description']}")
            print("-" * 40)
    
    def search_tasks(self):
        """Search tasks by keyword"""
        if not self.tasks:
            print("No tasks available to search!")
            return
        
        keyword = input("Enter search keyword: ").lower().strip()
        if not keyword:
            print("Please enter a keyword to search!")
            return
        
        matching_tasks = [
            task for task in self.tasks 
            if keyword in task['title'].lower() or keyword in task['description'].lower()
        ]
        
        if not matching_tasks:
            print(f"No tasks found containing '{keyword}'")
            return
        
        print(f"\nSearch results for '{keyword}':")
        print("="*50)
        
        for task in matching_tasks:
            status = "✓" if task['completed'] else "✗"
            priority_icon = "🔴" if task['priority'] == "High" else "🟡" if task['priority'] == "Medium" else "🟢"
            print(f"{priority_icon} [{status}] {task['title']}")
            print(f"   {task['description']}")
            print(f"   Category: {task['category']} | Due: {task['due_date']}")
            print("-" * 40)
    
    def show_statistics(self):
        """Show detailed statistics"""
        if not self.tasks:
            print("No tasks available for statistics!")
            return
        
        total_tasks = len(self.tasks)
        completed_tasks = len([task for task in self.tasks if task['completed']])
        pending_tasks = total_tasks - completed_tasks
        
        # Category statistics
        category_stats = {}
        for task in self.tasks:
            cat = task['category']
            category_stats[cat] = category_stats.get(cat, 0) + 1
        
        # Priority statistics
        priority_stats = {}
        for task in self.tasks:
            pri = task['priority']
            priority_stats[pri] = priority_stats.get(pri, 0) + 1
        
        print("\n" + "="*50)
        print("TASK STATISTICS")
        print("="*50)
        print(f"📊 Total Tasks: {total_tasks}")
        print(f"✅ Completed: {completed_tasks}")
        print(f"❌ Pending: {pending_tasks}")
        
        if total_tasks > 0:
            completion_rate = (completed_tasks / total_tasks) * 100
            print(f"📈 Completion Rate: {completion_rate:.1f}%")
        
        print("\n📁 By Category:")
        for category, count in category_stats.items():
            print(f"   {category}: {count} tasks")
        
        print("\n🎯 By Priority:")
        for priority, count in priority_stats.items():
            icon = "🔴" if priority == "High" else "🟡" if priority == "Medium" else "🟢"
            print(f"   {icon} {priority}: {count} tasks")
    
    def run(self):
        """Main application loop"""
        print("🚀 Welcome to Enhanced Task Manager!")
        
        while True:
            self.display_menu()
            
            # Show quick overview
            total_tasks = len(self.tasks)
            completed_tasks = len([task for task in self.tasks if task['completed']])
            print(f"📊 Overview: {total_tasks} tasks ({completed_tasks} completed)")
            
            try:
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
                    '9': self.show_statistics,
                    '10': lambda: None  # Exit handled below
                }
                
                if choice == '10':
                    print("\nThank you for using Enhanced Task Manager! 👋")
                    print("Your tasks have been saved automatically.")
                    break
                elif choice in actions:
                    actions[choice]()
                else:
                    print("Invalid choice! Please enter a number between 1-10.")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\nProgram interrupted. Saving tasks...")
                self.save_tasks()
                break
            except Exception as e:
                print(f"An error occurred: {e}")

# Include the basic methods from previous version (view_all_tasks, mark_completed, delete_task, etc.)
# These would be copied from the basic task manager

def main():
    """Main function to start the application"""
    try:
        task_manager = AdvancedTaskManager()
        task_manager.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")
    except Exception as e:
        print(f"Application error: {e}")

if __name__ == "__main__":
    main()