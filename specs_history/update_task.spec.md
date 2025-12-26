# Feature Specification: Update Task

**Feature Branch**: `003-update-task`
**Created**: 2025-12-26
**Status**: Draft
**Input**: Third feature for The Evolution of Todo - Update task functionality

## User Scenarios & Testing

### User Story 1 - Update Task Title and Description (Priority: P1)

As a user, I want to update a task's title and description so that I can correct mistakes or refine task details.

**Why this priority**: Users need to modify tasks when requirements change or when they made mistakes during initial entry.

**Independent Test**: Can be fully tested by creating a task, updating it with new title/description, and verifying the changes persist.

**Acceptance Scenarios**:

1. **Given** a task exists with ID 1, **When** I execute `python -m src.main update 1 "New Title" "New Description"`, **Then** the task title and description are updated and saved
2. **Given** a task has been updated, **When** I list tasks, **Then** the updated information is displayed
3. **Given** I update a task, **When** I restart the application, **Then** the updated task data persists

---

### Edge Cases

- What happens when the task ID doesn't exist?
- What happens when ID is not a valid integer?
- What happens when title or description is missing?
- What happens when title or description is empty?
- What happens when updating multiple times?

## Requirements

### Functional Requirements

- **FR-001**: System MUST accept task ID, new title, and new description as arguments
- **FR-002**: System MUST validate that task ID exists
- **FR-003**: System MUST validate that ID is a valid integer
- **FR-004**: System MUST validate that both title and description are provided and non-empty
- **FR-005**: System MUST update the task in memory and persist to storage
- **FR-006**: System MUST preserve task ID, completed status, and created timestamp
- **FR-007**: System MUST display confirmation message with task ID
- **FR-008**: System MUST provide clear error messages for invalid input

## Success Criteria

### Measurable Outcomes

- **SC-001**: Users can successfully update a task in under 5 seconds
- **SC-002**: Updated data persists across application restarts 100% of the time
- **SC-003**: Clear error messages for invalid task ID
- **SC-004**: Original task metadata (ID, created, completed) is preserved

## Technical Notes

### Command Syntax
```bash
python -m src.main update <ID> "New Title" "New Description"
```

### Expected Output
```
[OK] Task 1 updated successfully!
```

### Error Outputs
```
[ERROR] Task ID 99 not found
[ERROR] Invalid task ID: must be an integer
[ERROR] Both title and description are required
```

## Out of Scope

- Updating only title or only description (both required)
- Updating completion status (covered in complete_task.spec.md)
- Updating created timestamp
- Batch updates of multiple tasks
