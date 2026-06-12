from services.storage import load_data, save_data

 
class ProjectManager:

    def add_user(self, name):
        data = load_data()

        user = {
            "user_id": len(data["users"]) + 1,
            "name": name,
            "projects": []
        }

        data["users"].append(user)
        save_data(data)

        print(f"User '{name}' created")

    def list_users(self):
        data = load_data()

        if not data["users"]:
            print("No users found")
            return

        for user in data["users"]:
            print(f"ID: {user['user_id']} | Name: {user['name']}")

    def add_project(self, username, title):
        data = load_data()

        for user in data["users"]:
            if user["name"] == username:

                project = {
                    "project_id": len(user["projects"]) + 1,
                    "title": title,
                    "tasks": []
                }

                user["projects"].append(project)
                save_data(data)

                print(f"Project '{title}' added to {username}")
                return

        print("User not found")

    def list_projects(self):
        data = load_data()

        for user in data["users"]:
            print(f"\nUser: {user['name']}")

            for project in user["projects"]:
                print(f"  Project: {project['title']}")

    def add_task(self, project_title, task_title):
        data = load_data()

        for user in data["users"]:
            for project in user["projects"]:

                if project["title"] == project_title:

                    task = {
                        "task_id": len(project["tasks"]) + 1,
                        "title": task_title,
                        "completed": False
                    }

                    project["tasks"].append(task)
                    save_data(data)

                    print(f"Task '{task_title}' added")
                    return

        print("Project not found")

    def complete_task(self, project_title, task_title):
        data = load_data()

        for user in data["users"]:
            for project in user["projects"]:

                if project["title"] == project_title:

                    for task in project["tasks"]:
                        if task["title"] == task_title:
                            task["completed"] = True
                            save_data(data)

                            print(f"Task '{task_title}' completed")
                            return

        print("Task not found")

    def view_user_projects(self, username):
        data = load_data()

        for user in data["users"]:
            if user["name"] == username:

                print(f"\nProjects for {username}")

                for project in user["projects"]:
                    print(f"\nProject: {project['title']}")

                    for task in project["tasks"]:
                        status = "✓" if task["completed"] else "✗"
                        print(f"  {status} {task['title']}")

                return

        print("User not found")