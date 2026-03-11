---
name: translate
description: Translate .pseudo files into real, working code. Use when the user wants to generate or regenerate code from their pseudo-code source files.
argument-hint: "[file.pseudo or directory]"
---

Translate pseudo-code into real, working code.

## How to translate

1. Read the specified `.pseudo` file(s). If `$ARGUMENTS` is empty, find all `.pseudo` files in the project.
2. Parse the pseudo-code: understand the user's intent, logic, structure, and any inline commands or annotations.
3. Generate real code in the appropriate language/framework, placing output files alongside the `.pseudo` source (same directory, matching filename, real extension).
4. After translating, review the pseudo-code. When you notice something worth raising, suggest improvements — additions, removals, or **restructuring**. Always write suggestions as pseudo-code, never as real code. Present suggestions as diffs to the `.pseudo` file the user can accept or reject.

## When to talk back

Don't comment on every translation. Raise design feedback when you notice:
- **Ambiguity** that would lead to meaningfully different implementations
- **Missing edge cases** that will cause bugs or crashes
- **Structural issues** — pseudo-code that's getting tangled, duplicated, or hard to follow
- **Simplification opportunities** — the same thing expressed more clearly in fewer lines

You may suggest **restructuring** the pseudo-code — reordering sections, splitting concerns, merging redundant parts — not just adding lines. Always present restructuring as a suggested rewrite the user can accept or reject.

## Rules

- `.pseudo` files are the source of truth. Never modify them without the user's approval.
- Real code is a derived output, but **always ask the user before re-translating/overwriting** after pseudo-code changes.
- If the pseudo-code is ambiguous, ask the user rather than guessing.
- Preserve any structure/comments the user has in their pseudo-code.

## Communication style

**All discussion about design, architecture, and implementation must happen in pseudo-code — never in real code.**

When talking back to the user about:
- Missing edge cases
- Design alternatives
- Structural improvements
- Implementation details

Write everything in the user's pseudo-code style. Study how they write — their level of detail, their phrasing, their formatting — and match it. You may gently improve clarity or structure, but it must still read like something they would write.

**Never** show Python/JS/Rust/etc. snippets to explain a design point. If you need to discuss how something should work, describe it as pseudo-code the user could paste into their `.pseudo` file.

Example — if the user writes loosely:
```
read a file, split by lines, find duplicates
```
Then suggest in the same style:
```
read a file, split by lines, find duplicates
  -> handle case where file doesn't exist: print error and stop
  -> what counts as duplicate? exact match or ignore whitespace?
```

Do NOT suggest:
```python
try:
    with open(f) as file:
        lines = file.readlines()
except FileNotFoundError:
    print("error")
```

## .pseudo file conventions

- Extension: `.pseudo`
- No enforced syntax — the user writes however feels natural to them
- Users may include annotations like `// use python`, `// output: app.ts`, or `LANG: rust` to hint at target language/filename
- If no language hint is given, infer from context or ask
