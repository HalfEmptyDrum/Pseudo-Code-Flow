---
name: translate
description: Translate .pseudo files into real, working code. Use when the user wants to generate or regenerate code from their pseudo-code source files.
argument-hint: "[file.pseudo or directory]"
---

Translate pseudo-code into real, working code.

## Translation steps

1. Read the specified `.pseudo` file(s). If `$ARGUMENTS` is empty, find all `.pseudo` files in the project.
2. Parse the pseudo-code: understand the user's intent, logic, structure, and any inline commands or annotations.
3. Generate real code in the appropriate language/framework. Place output files alongside the `.pseudo` source (same directory, matching filename, real extension).
4. If this is a **re-translation** (output files already exist), ask the user to confirm before overwriting.
5. Review the pseudo-code for potential improvements. Only raise feedback when it matters (see below).

## When to give feedback

Don't comment on every translation. Raise design feedback when you notice:
- **Ambiguity** that would lead to meaningfully different implementations
- **Missing edge cases** that will cause bugs or crashes
- **Structural issues** — pseudo-code that's getting tangled, duplicated, or hard to follow
- **Simplification opportunities** — the same thing expressed more clearly in fewer lines

You may suggest **restructuring** — reordering sections, splitting concerns, merging redundant parts — not just adding lines. Always present changes as a suggested rewrite the user can accept or reject.

## Communication style

**All discussion about design, architecture, and implementation must happen in pseudo-code — never in real code.**

Study how the user writes — their level of detail, phrasing, formatting — and match it. You may gently improve clarity, but it must still read like something they would write.

**Never** show language-specific code (Python, JS, Rust, etc.) to explain a design point. Describe it as pseudo-code the user could paste into their `.pseudo` file.

Good — matching the user's loose style:
```
read a file, split by lines, find duplicates
  -> handle case where file doesn't exist: print error and stop
  -> what counts as duplicate? exact match or ignore whitespace?
```

Bad — leaking real code into the conversation:
```python
try:
    with open(f) as file:
        lines = file.readlines()
except FileNotFoundError:
    print("error")
```

## Rules

- `.pseudo` files are the source of truth. Never modify them without the user's approval.
- Always ask the user before re-translating/overwriting existing output files.
- If the pseudo-code is ambiguous, ask rather than guess.
- Preserve any structure and comments the user has in their pseudo-code.
- When multiple `.pseudo` files exist, be aware of dependencies between them and translate in the right order.

## .pseudo file conventions

- Extension: `.pseudo`
- No enforced syntax — the user writes however feels natural
- Language/output hints are optional: `// use python`, `// output: app.ts`, `LANG: rust`
- If no hint is given, infer from context or ask
