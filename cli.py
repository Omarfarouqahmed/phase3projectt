from models import User, Task
from dbstuff import session
# from mycode import session
tasks = []

# Function to create a new user
def create_user(username, password):
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print(f"🖨️ Error: User with username '{username}' already exists.")
        return None

    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    print(f"🖨️ ✅ User {username} created successfully. ✅ ")
    return user


# Function to authenticate and return user_id
def login(username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        return user.user_id
    else:
        return None

# Function to create a new task
def create_task(user_id, title):
    user = session.query(User).filter_by(user_id=user_id).first()
    if user:
        task = Task(user_id=user_id, title=title)
        session.add(task)
        session.commit()
        tasks.append(task)
        print(f"🖨️ ✅ Task '{title}' created successfully. Task ID: {task.task_id} ✅ ")
    else:
        print(f"🖨️ User with ID '{user_id}' does not exist. Please create a user first.")

# Function to delete tasks by title
def delete_task(username, title):
    user = session.query(User).filter_by(username=username).first()
    if user:
        task_to_delete = session.query(Task).filter_by(user_id=user.user_id, title=title).first()
        if task_to_delete:
            session.delete(task_to_delete)
            session.commit()
            print(f"🖨️ ✅ Task with title '{title}' deleted successfully. ✅ ")
        else:
            print(f"🖨️ No task found with title '{title}' for user '{username}'.")
    else:
        print(f"🖨️ User '{username}' not found.")

# Function to display tasks by username
def display_tasks(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        tasks = session.query(Task).filter_by(user_id=user.user_id).all()
        if tasks:
            print(f"🖨️ Tasks for {username}:")
            for task in tasks:
                print(f"🖨️ Task ID: {task.task_id}, Title: {task.title}")
        else:
            print(f"🖨️ No tasks found for {username}.")
    else:
        print(f"🖨️ User '{username}' not found.")

# Function to generate a report of users and their tasks
def generate_report():
    users = session.query(User).all()
    print("User Report:")
    for user in users:
        print(f"User: {user.username}")
        tasks = session.query(Task).filter_by(user_id=user.user_id).all()
        for task in tasks:
            print(f"  Task ID: {task.task_id}, Title: {task.title}")


def delete_user(username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        # Delete the user's tasks first
        tasks = session.query(Task).filter_by(user_id=user.user_id).all()
        for task in tasks:
            session.delete(task)

        session.delete(user)
        session.commit()
        print(f"🖨️ User '{username}' and associated tasks deleted successfully.")
    else:
        print("🖨️ User not found or password is incorrect.")


if __name__ == '__main__':
    while True:
        print("*********** 💫 Available actions 💫  ************")
        print("1. Create User")
        print("2. Login")
        print("3. Create Task")
        print("4. Delete Task")
        print("5. Display Tasks")
        print("6. Generate Report")
        print("7. Delete a User")
        print("8. Exit")

        choice = input("🗣️ Enter the number of your choice: ")

        if choice == '1':
            username = input("🗣️ Enter username: ")
            password = input("🗣️ Enter password: ")
            create_user(username, password)
        elif choice == '2':
            username = input("🗣️ Enter username: ")
            password = input("🗣️ Enter password: ")
            user_id = login(username, password)
            if user_id:
                print(f" ✅ Login successful. User ID: {user_id} ✅ ")
            else:
                print(" ❌ Login failed. Invalid username or password. ❌ ")
        elif choice == '3':
            username = input("🗣️ Enter your username: ")
            user = session.query(User).filter_by(username=username).first()
            if user:
                title = input("Enter task title: ")
                create_task(user.user_id, title)
            else:
                print(" ❌ User not found. Please create a user first. ❌ ")
        elif choice == '4':
            username = input("🗣️ Enter your username: ")
            user = session.query(User).filter_by(username=username).first()
            if user:
                title = input("🗣️ Enter task title to delete: ")
                delete_task(username, title)
            else:
                print(" ❌ User not found. ❌ ")
                
        elif choice == '5':
            username = input("🗣️ Enter your username: ")
            user = session.query(User).filter_by(username=username).first()
            display_tasks(username)

        elif choice == '6':
            generate_report()

        elif choice == '7':
            username = input("🗣️ Enter username: ")
            password = input("🗣️ Enter password: ")
            delete_user(username, password)

        elif choice == '8':
            print(" 😘 Goodbye!")


            break
