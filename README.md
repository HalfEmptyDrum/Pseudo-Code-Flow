# Pseudo Code Flow

Make programmers think about code again.

Instead of passively accepting AI-generated changes, you write **pseudo-code** — your own logic, your own thinking — and Claude Code translates it into real code. There's no new syntax to learn. `.pseudo` files are written in *your* language, however you think.

## How it works

**Two terminals:**
1. You edit `.pseudo` files in your editor
2. You run Claude Code and use `/translate` to generate real code

**The loop:**
1. Write pseudo-code describing what you want to build
2. Run `/translate` — Claude generates working code
3. Claude reviews your pseudo-code and may suggest improvements — **as pseudo-code**, in your writing style
4. You update your `.pseudo` file (or don't)
5. Confirm re-translation when ready

`.pseudo` files are the source of truth. Real code is derived.

## Setup

Copy `.claude/skills/translate/` into your project's `.claude/skills/` folder. Restart Claude Code so it picks up the new skill. That's it.

## Example

**You write `example.pseudo`:**
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

**You run `/translate example.pseudo`** — Claude generates a working `todo.py`.

**Claude suggests back (as pseudo-code, not Python):**
```
suggested changes to example.pseudo:
  + handle edge cases:
  +   add with no title - print "usage: add <title>"
  +   done/remove with non-number - print "please give a number"
  +
  + save/load todos to a file so they persist between runs
```

You decide what to keep. You update the `.pseudo` file. You re-translate.

## Pseudo-code conventions

- File extension: `.pseudo`
- No enforced syntax — write however feels natural
- Optional language/output hints: `// use python`, `// output: app.ts`, `LANG: rust`
- If no hint is given, Claude infers from context or asks

## Key principles

- Pseudo-code is the source, real code is the output
- Claude never modifies `.pseudo` files without your approval
- All design feedback from Claude comes as pseudo-code, matching your style
- Claude asks before re-translating after pseudo-code changes
- Claude speaks up about ambiguity, edge cases, and structural issues — only when it matters
