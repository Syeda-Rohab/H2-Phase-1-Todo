---
description: "Dependency-ordered task list for Console CRUD Todo Application"
---

# Tasks: Console CRUD Todo Application

**Input**: Design documents from `/specs/001-console-todo-crud/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/cli-commands.md

**Tests**: NOT included (not requested in specification)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/`, `data/` at repository root
- Structure follows plan.md: src/models/, src/main.py, src/todo_app.py

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure (src/, src/models/, data/, tests/manual/)
- [X] T002 Initialize pyproject.toml with Python 3.13+ and UV configuration
- [X] T003 [P] Create empty __init__.py files in src/ and src/models/
- [X] T004 [P] Create data/.gitkeep to track data directory
- [X] T005 [P] Copy Constitution.txt from .specify/memory/constitution.md to repository root
- [X] T006 [P] Create README.md with setup instructions and usage examples
- [X] T007 [P] Create CLAUDE.md with development workflow documentation

**Checkpoint**: Project structure ready for implementation

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T008 Create Task dataclass in src/models/task.py with id, title, description, completed, created_at fields
- [ ] T009 Add Task.to_dict() method for JSON serialization in src/models/task.py
- [ ] T010 Add Task.from_dict() static method for JSON deserialization in src/models/task.py
- [ ] T011 Add Task.validate() method with title/description length constraints in src/models/task.py
- [ ] T012 Create create_task() factory function with auto-timestamp in src/models/task.py
- [ ] T013 Implement load_tasks() function with FileNotFoundError and JSONDecodeError handling in src/todo_app.py
- [ ] T014 Implement save_tasks() function with atomic write pattern (temp file + os.replace) in src/todo_app.py
- [ ] T015 Implement generate_next_id() function (max existing ID + 1) in src/todo_app.py
- [ ] T016 Create argparse parser with subcommands structure in src/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Task Creation (Priority: P1) 🎯 MVP Component 1/2

**Goal**: Enable users to add tasks with title and optional description, receiving immediate confirmation with unique ID

**Independent Test**: Run `python -m src.main add "Test Task" "Test Description"` and verify task appears in list with ID #1

### Implementation for User Story 1

- [ ] T017 [US1] Implement add_task(title, description) function in src/todo_app.py that creates Task with generated ID
- [ ] T018 [US1] Add 'add' subcommand parser with title (required) and description (optional) arguments in src/main.py
- [ ] T019 [US1] Implement handle_add() function that calls add_task() and saves to file in src/main.py
- [ ] T020 [US1] Add success output "Task added: #<ID> <title>" to handle_add() in src/main.py
- [ ] T021 [US1] Add error handling for empty title with message "Error: Title cannot be empty" in src/main.py
- [ ] T022 [US1] Add error handling for title >500 chars with message "Error: Title cannot exceed 500 characters" in src/main.py
- [ ] T023 [US1] Add error handling for description >2000 chars with message "Error: Description cannot exceed 2000 characters" in src/main.py

**Checkpoint**: At this point, users can add tasks and they persist to data/tasks.json

---

## Phase 4: User Story 2 - Task Viewing (Priority: P1) 🎯 MVP Component 2/2

**Goal**: Enable users to review all tasks with IDs, titles, descriptions, completion status, and timestamps in clear console format

**Independent Test**: Create 3 tasks with varying data, run `python -m src.main list`, verify all tasks display with proper formatting and status symbols

### Implementation for User Story 2

- [ ] T024 [US2] Implement get_all_tasks() function that returns list of tasks in src/todo_app.py
- [ ] T025 [US2] Add 'list' subcommand parser (no arguments) in src/main.py
- [ ] T026 [US2] Implement format_timestamp() helper to convert ISO 8601 to "YYYY-MM-DD HH:MM" in src/main.py
- [ ] T027 [US2] Implement format_description() helper to truncate long descriptions to 30 chars with "..." in src/main.py
- [ ] T028 [US2] Implement handle_list() function with tabular output formatting in src/main.py
- [ ] T029 [US2] Add status symbols (✓ for completed=true, ○ for completed=false) to handle_list() in src/main.py
- [ ] T030 [US2] Add "No tasks found." message when task list is empty in handle_list() in src/main.py
- [ ] T031 [US2] Add column headers (ID | Status | Title | Description | Created) to handle_list() output in src/main.py

**Checkpoint**: MVP complete - users can add and view tasks (User Stories 1 & 2 functional)

---

## Phase 5: User Story 3 - Task Completion Toggle (Priority: P2)

**Goal**: Enable users to mark tasks complete or incomplete to track progress

**Independent Test**: Create task, run `python -m src.main complete 1`, verify status shows ✓ in list, run `python -m src.main incomplete 1`, verify status shows ○

### Implementation for User Story 3

- [ ] T032 [P] [US3] Implement find_task_by_id(task_id) helper function that returns Task or None in src/todo_app.py
- [ ] T033 [P] [US3] Implement update_task_status(task_id, completed) function in src/todo_app.py
- [ ] T034 [US3] Add 'complete' subcommand parser with id argument (integer) in src/main.py
- [ ] T035 [US3] Implement handle_complete() function that calls update_task_status(id, True) in src/main.py
- [ ] T036 [US3] Add success output "Task #<ID> marked as complete." to handle_complete() in src/main.py
- [ ] T037 [US3] Add 'incomplete' subcommand parser with id argument (integer) in src/main.py
- [ ] T038 [US3] Implement handle_incomplete() function that calls update_task_status(id, False) in src/main.py
- [ ] T039 [US3] Add success output "Task #<ID> marked as incomplete." to handle_incomplete() in src/main.py
- [ ] T040 [US3] Add error handling for invalid ID format with message "Error: Invalid ID '<value>'. Must be a number." in src/main.py
- [ ] T041 [US3] Add error handling for task not found with message "Error: Task #<ID> not found." in src/main.py

**Checkpoint**: Users can now manage task completion status (User Stories 1, 2, 3 functional)

---

## Phase 6: User Story 4 - Task Modification (Priority: P2)

**Goal**: Enable users to update task title and/or description while preserving ID and metadata

**Independent Test**: Create task, run `python -m src.main update 1 --title "New Title" --description "New Desc"`, verify changes in list while ID and timestamp remain unchanged

### Implementation for User Story 4

- [ ] T042 [US4] Implement update_task(task_id, title, description) function with partial update support in src/todo_app.py
- [ ] T043 [US4] Add 'update' subcommand parser with id (required), --title (optional), --description (optional) in src/main.py
- [ ] T044 [US4] Implement handle_update() function that validates at least one field provided in src/main.py
- [ ] T045 [US4] Add logic to preserve existing title if --title not provided in handle_update() in src/main.py
- [ ] T046 [US4] Add logic to preserve existing description if --description not provided in handle_update() in src/main.py
- [ ] T047 [US4] Add success output "Task #<ID> updated." to handle_update() in src/main.py
- [ ] T048 [US4] Add error handling for "Error: At least one of --title or --description must be provided." in src/main.py
- [ ] T049 [US4] Add error handling for task not found with message "Error: Task #<ID> not found." in src/main.py
- [ ] T050 [US4] Add validation for new title length (1-500 chars) in handle_update() in src/main.py
- [ ] T051 [US4] Add validation for new description length (0-2000 chars) in handle_update() in src/main.py

**Checkpoint**: Users can now edit existing tasks (User Stories 1, 2, 3, 4 functional)

---

## Phase 7: User Story 5 - Task Deletion (Priority: P3)

**Goal**: Enable users to permanently remove tasks that are no longer relevant

**Independent Test**: Create 5 tasks, run `python -m src.main delete 3`, verify task #3 removed and tasks #1, #2, #4, #5 remain with original IDs

### Implementation for User Story 5

- [ ] T052 [US5] Implement delete_task(task_id) function that removes task from list in src/todo_app.py
- [ ] T053 [US5] Add 'delete' subcommand parser with id argument (integer) in src/main.py
- [ ] T054 [US5] Implement handle_delete() function that calls delete_task() and saves in src/main.py
- [ ] T055 [US5] Add success output "Task #<ID> deleted." to handle_delete() in src/main.py
- [ ] T056 [US5] Add error handling for task not found with message "Error: Task #<ID> not found." in src/main.py
- [ ] T057 [US5] Add error handling for invalid ID format with message "Error: Invalid ID '<value>'. Must be a number." in src/main.py
- [ ] T058 [US5] Verify no ID renumbering occurs after deletion (preserve original IDs) in delete_task() in src/todo_app.py

**Checkpoint**: All 5 CRUD operations complete (User Stories 1, 2, 3, 4, 5 functional)

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final quality assurance

- [ ] T059 [P] Add UTF-8 encoding specification to all file open() calls in src/todo_app.py
- [ ] T060 [P] Add sys.exit(1) calls for all error paths in src/main.py
- [ ] T061 [P] Add sys.exit(0) for successful command completion in src/main.py
- [ ] T062 [P] Add type hints to all functions in src/models/task.py
- [ ] T063 [P] Add type hints to all functions in src/todo_app.py
- [ ] T064 [P] Add type hints to all functions in src/main.py
- [ ] T065 [P] Create manual test scenarios document in tests/manual/test_scenarios.md based on contracts/cli-commands.md
- [ ] T066 Add --help flag handling with usage examples in src/main.py
- [ ] T067 Add general error handler for unknown commands in src/main.py
- [ ] T068 Add general error handler for no command provided in src/main.py
- [ ] T069 Verify data directory creation (mkdir exist_ok=True) in save_tasks() in src/todo_app.py
- [ ] T070 Run quickstart.md validation: test all 5 commands end-to-end with data persistence

**Checkpoint**: Production-ready application with complete error handling and documentation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational - Can run independently
- **User Story 2 (Phase 4)**: Depends on Foundational - Can run independently (parallel with US1)
- **User Story 3 (Phase 5)**: Depends on Foundational - Can run independently (parallel with US1/US2)
- **User Story 4 (Phase 6)**: Depends on Foundational - Can run independently (parallel with US1/US2/US3)
- **User Story 5 (Phase 7)**: Depends on Foundational - Can run independently (parallel with US1/US2/US3/US4)
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Foundation only - No dependencies on other stories
- **User Story 2 (P1)**: Foundation only - No dependencies on other stories
- **User Story 3 (P2)**: Foundation only - No dependencies on other stories (uses find_task_by_id helper)
- **User Story 4 (P2)**: Foundation only - No dependencies on other stories (uses find_task_by_id helper)
- **User Story 5 (P3)**: Foundation only - No dependencies on other stories (uses find_task_by_id helper)

### Within Each User Story

**User Story 1 (Task Creation)**:
- T017 (add_task function) → T018 (parser) → T019 (handler) → T020-T023 (error handling)

**User Story 2 (Task Viewing)**:
- T024 (get_all_tasks) → T025 (parser) → T026-T027 (formatting helpers) → T028-T031 (display logic)

**User Story 3 (Completion Toggle)**:
- T032-T033 can run in parallel (helper functions) → T034-T041 (complete/incomplete commands)

**User Story 4 (Task Modification)**:
- T042 (update function) → T043 (parser) → T044-T051 (update handler + validation)

**User Story 5 (Task Deletion)**:
- T052 (delete function) → T053 (parser) → T054-T058 (delete handler + validation)

### Parallel Opportunities

**Setup Phase (Phase 1)**:
- T003, T004, T005, T006, T007 can all run in parallel (different files)

**Foundational Phase (Phase 2)**:
- T008-T012 (task.py) can be done sequentially (same file)
- T013-T015 (todo_app.py) can be done sequentially (same file)
- T016 (main.py) can run in parallel with T008-T015

**User Story Implementation**:
- Once Foundational phase completes, ALL user stories (Phase 3-7) can start in parallel if team capacity allows
- Within User Story 3: T032, T033 can run in parallel (different concerns)

**Polish Phase (Phase 8)**:
- T059-T065 can all run in parallel (different files or non-conflicting edits)

---

## Parallel Example: Foundation + User Stories

```bash
# Foundation Phase (MUST complete before user stories):
Sequential: T008-T012 in src/models/task.py
Sequential: T013-T015 in src/todo_app.py
Parallel: T016 in src/main.py (while T008-T015 are in progress)

# Once Foundation complete, launch all user stories in parallel:
Team Member A: Phase 3 (User Story 1 - Task Creation)
Team Member B: Phase 4 (User Story 2 - Task Viewing)
Team Member C: Phase 5 (User Story 3 - Completion Toggle)
Team Member D: Phase 6 (User Story 4 - Task Modification)
Team Member E: Phase 7 (User Story 5 - Task Deletion)

# Or sequentially by priority:
Solo: US1 → US2 → US3 → US4 → US5
```

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Task Creation)
4. Complete Phase 4: User Story 2 (Task Viewing)
5. **STOP and VALIDATE**: Test add + list operations independently
6. Deploy/demo basic todo app (can add and view tasks)

**Rationale**: Both P1 stories provide minimum viable product - users can capture and review tasks

### Incremental Delivery (Recommended)

1. **Foundation** (Phase 1 + 2) → Core infrastructure ready
2. **MVP** (Phase 3 + 4) → User Story 1 + 2 → Test independently → Deploy/Demo
3. **Enhancement 1** (Phase 5) → Add User Story 3 → Test independently → Deploy/Demo
4. **Enhancement 2** (Phase 6) → Add User Story 4 → Test independently → Deploy/Demo
5. **Enhancement 3** (Phase 7) → Add User Story 5 → Test independently → Deploy/Demo
6. **Polish** (Phase 8) → Final quality pass → Deploy/Demo complete application

Each increment adds value without breaking previous functionality.

### Parallel Team Strategy

With 5 developers:

1. **Together**: Complete Setup + Foundational (everyone contributes)
2. **Parallel** (once Foundational done):
   - Developer A: User Story 1 (T017-T023)
   - Developer B: User Story 2 (T024-T031)
   - Developer C: User Story 3 (T032-T041)
   - Developer D: User Story 4 (T042-T051)
   - Developer E: User Story 5 (T052-T058)
3. **Together**: Polish phase (T059-T070)

Stories complete independently and integrate seamlessly since they operate on the same data model.

---

## Task Statistics

- **Total Tasks**: 70
- **Phase 1 (Setup)**: 7 tasks
- **Phase 2 (Foundational)**: 9 tasks
- **Phase 3 (US1)**: 7 tasks
- **Phase 4 (US2)**: 8 tasks
- **Phase 5 (US3)**: 10 tasks
- **Phase 6 (US4)**: 10 tasks
- **Phase 7 (US5)**: 7 tasks
- **Phase 8 (Polish)**: 12 tasks

**Parallel Opportunities Identified**: 15 tasks marked [P]

**Independent Test Criteria**:
- US1: Can add tasks and verify persistence
- US2: Can list tasks with proper formatting
- US3: Can toggle completion status
- US4: Can update task details
- US5: Can delete tasks without affecting others

**Suggested MVP Scope**: Phase 1 + 2 + 3 + 4 (User Story 1 & 2) = 31 tasks for functional todo app

---

## Notes

- [P] tasks = different files or non-conflicting edits, no dependencies
- [Story] label maps task to specific user story for traceability
- All user stories are independently testable after Foundational phase
- No test tasks included (not requested in specification)
- Commit after each task or logical group of tasks
- Stop at any checkpoint to validate story independently
- Error handling follows consistent pattern from contracts/cli-commands.md
- All paths verified against plan.md structure (single project, src/ at root)
