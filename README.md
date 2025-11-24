# Personallized-Task-Manager

A sophisticated Python-based task management application designed to help users organize their daily tasks efficiently with categories, priorities, and intelligent due date tracking.

## 🚀 Features

### Core Functionality
- ✅ **Task Management** - Create, read, update, and delete tasks
- 🏷️ **Categorization** - Organize tasks into Work, Personal, Study, Shopping, Health, and Other categories
- 🎯 **Priority Levels** - High (🔴), Medium (🟡), and Low (🟢) priority system
- 📅 **Due Date Tracking** - Set due dates with smart options (Today, Tomorrow, Next Week)
- 🔍 **Advanced Search** - Find tasks by keywords in titles or descriptions

### Advanced Features
- 📊 **Statistics Dashboard** - Visual insights with completion rates and category distribution
- 👀 **Multiple Views** - View tasks by category, priority, or due date
- 📈 **Progress Tracking** - Monitor completion rates and task distribution
- 💾 **Data Persistence** - Automatic JSON storage with error handling
- 🎨 **User-Friendly Interface** - Clean console interface with emojis and colors

## 📸 Screenshots

<img width="527" height="857" alt="image" src="https://github.com/user-attachments/assets/6a1bfe9b-2550-44cb-9ef7-1b120fb67ff5" />
<img width="490" height="872" alt="image" src="https://github.com/user-attachments/assets/71c81d55-b390-4f79-81d3-4fd78c9698b9" />
<img width="496" height="853" alt="image" src="https://github.com/user-attachments/assets/afb6d92b-b553-44ea-a84d-3f6af01be0a3" />
<img width="530" height="841" alt="image" src="https://github.com/user-attachments/assets/bfb25df1-5c17-48e0-a7b8-3915a7a2bb62" />
<img width="507" height="852" alt="image" src="https://github.com/user-attachments/assets/b8fba8d7-fd90-4353-844e-9cd67914e87c" />
<img width="502" height="525" alt="image" src="https://github.com/user-attachments/assets/5bf72612-842e-432b-96db-a089d6c79ce2" />





## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- No external dependencies required

### Quick Start
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/enhanced-task-manager.git
   cd enhanced-task-manager
   ```

2. **Run the application**
   ```bash
   python advanced_task_manager.py
   ```

### Alternative Installation
1. Download the `advanced_task_manager.py` file
2. Run directly:
   ```bash
   python advanced_task_manager.py
   ```

## 📖 Usage

### Basic Operations
1. **Adding a Task**
   - Enter task title and description
   - Select from 6 predefined categories
   - Choose priority level (High/Medium/Low)
   - Set due date using smart options

2. **Managing Tasks**
   - Mark tasks as completed with timestamps
   - Delete tasks with confirmation
   - View tasks in multiple organized views

3. **Advanced Features**
   - Search across all task fields
   - View statistics and completion rates
   - Filter by category and priority

### Menu Options
```
1. View All Tasks         6. View Tasks by Priority
2. Add New Task           7. View Today's Tasks  
3. Mark Task Completed    8. Search Tasks
4. Delete Task            9. Task Statistics
5. View by Category       10. Exit
```

## 🏗️ Project Structure

```
enhanced-task-manager/
├── advanced_task_manager.py  # Main application file
├── tasks.json               # Auto-generated data storage
├── screenshots/            # Application screenshots
│   ├── main_menu.png
│   ├── add_task.png
│   ├── categories.png
│   ├── priorities.png
│   ├── search.png
│   └── statistics.png
├── recordings/             # Screen recordings (if any)
│   └── demo.mp4
└── README.md              # This file
```

## 💻 Code Architecture

### Class Structure
```python
AdvancedTaskManager
├── __init__() - Initializes task manager and categories
├── load_tasks() - Loads tasks from JSON file
├── save_tasks() - Saves tasks to JSON file
├── display_menu() - Shows main menu interface
├── add_task() - Adds task with enhanced details
├── view_tasks_by_category() - Groups tasks by category
├── view_tasks_by_priority() - Sorts tasks by priority
├── view_todays_tasks() - Shows tasks due today
├── search_tasks() - Keyword-based task search
└── show_statistics() - Displays analytics dashboard
```

### Data Model
```json
{
  "id": 1,
  "title": "Complete project documentation",
  "description": "Write README and add screenshots",
  "category": "Work",
  "priority": "High",
  "due_date": "2024-01-15",
  "completed": false,
  "created_date": "2024-01-10 14:30:00",
  "completed_date": null
}
```

## 🎯 Project Guidelines Compliance

This project addresses all required guidelines:

### ✅ Real-World Problem Solving
- **Problem**: Difficulty in organizing and prioritizing daily tasks
- **Solution**: Intuitive task management with categorization and prioritization

### ✅ Clear Objectives
- Create a user-friendly task management system
- Implement efficient data storage and retrieval
- Provide multiple viewing and organization options
- Offer insights through statistics and analytics

### ✅ Applied Course Concepts
- **File I/O**: JSON data persistence
- **Data Structures**: Lists, dictionaries, and sorting algorithms
- **Object-Oriented Programming**: Class-based architecture
- **Error Handling**: Comprehensive try-except blocks
- **Date/Time Operations**: Due date management and timestamps

### ✅ Development Process
1. **Problem Definition**: Identified need for better task organization
2. **Requirement Analysis**: Feature planning and user workflow
3. **Modular Design**: Separated concerns into class methods
4. **Implementation**: Incremental feature development
5. **Testing**: Manual testing of all functionalities
6. **Documentation**: Comprehensive README and code comments

## 🔧 Technical Details

### Technologies Used
- **Python 3.8+** - Core programming language
- **JSON** - Data storage format
- **datetime** - Date and time operations
- **Standard Library** - No external dependencies

### Key Algorithms
- **Priority Sorting**: Custom sorting for task priorities
- **Search Algorithm**: Linear search with case-insensitive matching
- **Statistics Calculation**: Real-time analytics computation
- **Data Validation**: Input sanitization and error checking

## 🚀 Future Enhancements

### Planned Features
- [ ] Web interface using Flask/Django
- [ ] Email notifications for due tasks
- [ ] Data synchronization across devices
- [ ] Task templates and recurring tasks
- [ ] Collaboration features for team tasks
- [ ] Data export to CSV/PDF formats

### Possible Extensions
- Mobile app version
- Integration with calendar apps
- AI-based task prioritization
- Time tracking features



## 👨‍💻 Developer

**Your Name**  
- GitHub: aahana25boe10087-art
- Email: aahana.25boe10087@vitbhopal.ac.in

## 🙏 Acknowledgments

- Inspired by productivity methodologies like GTD (Getting Things Done)
- Built as part of academic coursework demonstrating software engineering principles
- Thanks to the Python community for excellent documentation and resources

---

<div align="center">

**If you find this project helpful, please give it a ⭐!**

*"Productivity is never an accident. It is always the result of a commitment to excellence, intelligent planning, and focused effort."* - Paul J. Meyer

</div>
