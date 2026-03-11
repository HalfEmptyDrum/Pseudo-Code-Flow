todos = []


def add_todo(title):
    todos.append({"title": title, "done": False})
    print(f"Added: {title}")


def list_todos():
    if not todos:
        print("No todos.")
        return
    for i, todo in enumerate(todos, 1):
        status = "x" if todo["done"] else " "
        print(f"  {i}. [{status}] {todo['title']}")


def mark_done(number):
    idx = number - 1
    if 0 <= idx < len(todos):
        todos[idx]["done"] = True
        print(f"Done: {todos[idx]['title']}")
    else:
        print(f"No todo #{number}.")


def remove_todo(number):
    idx = number - 1
    if 0 <= idx < len(todos):
        removed = todos.pop(idx)
        print(f"Removed: {removed['title']}")
    else:
        print(f"No todo #{number}.")


while True:
    line = input("> ").strip()
    if not line:
        continue

    parts = line.split(maxsplit=1)
    cmd = parts[0].lower()

    if cmd == "add" and len(parts) > 1:
        add_todo(parts[1])
    elif cmd == "list":
        list_todos()
    elif cmd == "done" and len(parts) > 1:
        mark_done(int(parts[1]))
    elif cmd == "remove" and len(parts) > 1:
        remove_todo(int(parts[1]))
    elif cmd == "quit":
        break
    else:
        print(f"Unknown command: {line}")
