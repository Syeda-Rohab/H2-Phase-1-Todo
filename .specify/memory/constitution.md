<!--
Sync Impact Report:
- Version change: [NEW] → 1.0.0
- Modified principles: All principles created (initial constitution)
- Added sections:
  * Core Principles (7 principles)
  * Technology Stack
  * Development Workflow
  * Governance
- Removed sections: None
- Templates requiring updates:
  ✅ constitution.md created
  ⚠ plan-template.md (pending review)
  ⚠ spec-template.md (pending review)
  ⚠ tasks-template.md (pending review)
- Follow-up TODOs: Verify template consistency after constitution creation
-->

# The Evolution of Todo Constitution

## Core Principles

### I. Complete Feature Implementation
**All 5 basic features MUST be implemented end-to-end**: Add, Delete, Update, View, and Mark Complete/Incomplete.

**Rationale**: This is a learning project demonstrating full CRUD operations. Partial implementation defeats the educational purpose. Each feature must be fully functional before moving to the next.

### II. Structured Task Data Model
**Every task MUST contain**: unique ID, title, description, completed status (boolean), and created timestamp.

**Requirements**:
- Add operations MUST accept both title and description parameters
- IDs MUST be unique and automatically generated
- Timestamps MUST be ISO 8601 format
- Completed status defaults to false

**Rationale**: Consistent data structure ensures predictable behavior and enables future features like sorting, filtering, and analytics.

### III. Complete CRUD Operations
**Each operation MUST implement its full contract**:
- **Add**: Accept title + description, generate ID and timestamp, persist task
- **View/List**: Display ALL tasks with clear status indicators (✓ complete / ✗ incomplete)
- **Update**: Modify title and/or description by ID
- **Delete**: Remove task completely by ID
- **Complete/Incomplete**: Toggle completion status by ID

**Rationale**: Half-implemented features create confusion and technical debt. Each operation must be production-quality.

### IV. Data Persistence (NON-NEGOTIABLE)
**All task data MUST survive application restart.**

**Requirements**:
- Use file-based persistence (JSON recommended)
- Atomic writes to prevent corruption
- Data integrity checks on load
- Handle missing/corrupted data gracefully

**Rationale**: A todo application that loses data on restart is fundamentally broken. Persistence is core functionality, not a feature.

### V. Type Safety & Error Handling
**Type hints MUST be used on ALL functions and classes. Error handling MUST cover all failure modes.**

**Requirements**:
- Python type hints on all function signatures and class attributes
- Handle invalid IDs (not found, wrong type)
- Handle missing/invalid arguments
- Provide clear error messages to users
- No silent failures

**Rationale**: Type hints catch bugs early and serve as inline documentation. Proper error handling creates a professional user experience.

### VI. Console-Only Interface with Exact Syntax
**Application MUST be console-based with standardized command syntax.**

**Required Commands**:
```bash
python -m src.main add "Title" "Description"
python -m src.main list
python -m src.main update <ID> "New Title" "New Description"
python -m src.main delete <ID>
python -m src.main complete <ID>
python -m src.main incomplete <ID>
```

**Display Format for List**:
```
ID | Title | Status | Created
```

**Rationale**: Consistent CLI syntax is predictable and scriptable. No web/GUI keeps focus on core Python concepts and UV package management.

### VII. Spec-Driven Development Workflow
**Follow strict spec-driven development using Spec-Kit Plus methodology.**

**Mandatory Workflow**:
1. Read specification from `specs_history/` folder
2. Implement ONLY that feature (no scope creep)
3. Test manually via console commands
4. Commit with reference to spec file
5. Move to next specification

**Rationale**: Prevents feature creep, ensures traceability, and teaches disciplined development practices. Each commit maps to a specific requirement.

## Technology Stack

### Required Technologies
- **Python Version**: 3.13+ ONLY
- **Package Manager**: UV package manager ONLY (not pip, poetry, or conda)
- **Dependencies**: Managed via `pyproject.toml`
- **Interface**: Console/CLI only (no web frameworks, no GUI libraries)

### Forbidden Technologies
- ❌ Web frameworks (Flask, Django, FastAPI)
- ❌ GUI libraries (Tkinter, PyQt, etc.)
- ❌ Alternative package managers (pip, poetry, conda)
- ❌ Python versions below 3.13

**Rationale**: UV is modern, fast, and demonstrates current Python tooling. Restricting to console keeps the project focused on core logic and UV package management skills.

## Project Structure

### Required Directory Layout
```
Todo H2/
├── Constitution.txt           # This file (project rules)
├── CLAUDE.md                  # Agent guidance
├── README.md                  # UV setup instructions
├── specs_history/             # All specification files
│   ├── add_task.spec.md
│   ├── view_tasks.spec.md
│   ├── update_task.spec.md
│   ├── delete_task.spec.md
│   └── complete_task.spec.md
├── src/                       # Source code
│   ├── __init__.py
│   ├── main.py               # Console entrypoint
│   ├── todo_app.py           # Core application logic
│   └── models/
│       ├── __init__.py
│       └── task.py           # Task data model
├── pyproject.toml            # UV dependencies
└── .specify/                 # Spec-Kit Plus framework
```

**Rationale**: Standardized structure enables automation, clear separation of concerns, and professional Python project organization.

## Development Workflow

### Feature Implementation Cycle
1. **Read Specification**: Start with `specs_history/<feature>.spec.md`
2. **Implement Feature**: Code ONLY what the spec requires
3. **Manual Testing**: Test all success and error cases via console
4. **Git Commit**: Reference spec file in commit message
5. **Move to Next**: Only proceed when current feature is complete

### Testing Standards
- Manual console testing MUST cover all command variations
- Test success cases (happy path)
- Test error cases (invalid ID, missing args, etc.)
- Verify data persistence across restarts
- Verify list output formatting

### Clean Code Requirements
- Functions MUST be single-purpose
- Variable names MUST be descriptive
- No magic numbers or strings (use constants)
- Maximum function length: ~20 lines (guideline, not hard limit)
- Comments MUST explain "why", not "what"

**Rationale**: Clean code is maintainable code. This project teaches professional coding habits from day one.

## Governance

### Constitution Authority
This constitution is the supreme governing document for "The Evolution of Todo" project. All development decisions, code reviews, and feature implementations MUST align with these principles.

### Amendment Process
1. Propose amendment with clear rationale
2. Identify affected principles and impact
3. Update constitution with new version number
4. Update dependent templates and documentation
5. Commit with descriptive message

### Version Policy
- **MAJOR**: Backward-incompatible principle changes (e.g., removing a required feature)
- **MINOR**: New principles added or significant expansions (e.g., adding security requirements)
- **PATCH**: Clarifications, typos, non-semantic refinements

### Compliance
- Every commit MUST reference its governing specification
- Code reviews MUST verify principle compliance
- No features outside the 5 core operations until all are complete
- Breaking changes require constitution amendment

### Success Criteria
**Project completion** = ALL 5 features (Add, Delete, Update, View, Mark Complete/Incomplete) working end-to-end in a console demonstration.

**Version**: 1.0.0 | **Ratified**: 2025-12-26 | **Last Amended**: 2025-12-26
