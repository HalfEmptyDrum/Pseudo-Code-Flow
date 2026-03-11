# Pseudo Code Flow

Make programmers think about code again.

Instead of passively accepting AI-generated changes, you write **pseudo-code** — your own logic, your own thinking — and Claude Code translates it into real code.

## How it works

**Two terminals:**
1. You edit `.pseudo` files in your editor
2. You run Claude Code and use `/translate` to generate real code

**The loop:**
- Write pseudo-code describing what you want to build
- Run `/translate` — Claude generates working code
- Claude suggests improvements **back as pseudo-code** in your writing style — never as real code
- You accept, reject, or iterate on the pseudo-code
- Confirm re-translation when ready

`.pseudo` files are the source of truth. Real code is derived.

## Setup

Copy the `.claude/skills/translate/` directory into your project's `.claude/skills/` folder. That's it — Claude Code picks up the `/translate` skill automatically.

## Example

**`example.pseudo`:**
```
// use python
// output: todo.py

a simple command-line todo app

store todos in a list, each todo has a title and done status

commands:
  add <title> - add a new todo
  list - show all todos with numbers
  done <number> - mark a todo as done
  remove <number> - remove a todo
  quit - exit

loop: show prompt "> ", read command, execute it
print a message if the command is unknown
```

Run `/translate example.pseudo` in Claude Code and get a working `todo.py`.

## Pseudo-code conventions

- File extension: `.pseudo`
- No enforced syntax — write however feels natural
- Add language/output hints if you want: `// use python`, `// output: app.ts`, `LANG: rust`
- If no hint is given, Claude infers from context or asks

## Key principles

- Pseudo-code is the source, real code is the output
- Claude never modifies `.pseudo` files without your approval
- All design feedback from Claude comes as pseudo-code, matching your style
- Claude asks before re-translating after pseudo-code changes
- Claude speaks up about ambiguity, edge cases, and structural improvements — but only when it matters
