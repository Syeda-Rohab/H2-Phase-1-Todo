# Feature Specification: Mark Task Complete/Incomplete

**Feature Branch**: `005-complete-task`
**Created**: 2025-12-26
**Status**: Draft
**Input**: Fifth feature for The Evolution of Todo - Mark task complete/incomplete functionality

## User Scenarios & Testing

### User Story 1 - Mark Task as Complete (Priority: P1)

As a user, I want to mark a task as complete so that I can track my progress and know what I've finished.

**Why this priority**: This is core todo functionality - users need to mark tasks done. Without this, the app is just a task creation tool.

**Independent Test**: Can be fully tested by creating a task, marking it complete, and verifying the status changes in the list.

**Acceptance Scenarios**:

1. **Given** a task exists with ID 1 and is incomplete, **When** I execute `python -m src.main complete 1`, **Then** the task status changes to complete
2. **Given** a task has been marked complete, **When** I list tasks, **Then** the task shows "[X] Complete" status
3. **Given** I mark a task complete, **When** I restart the application, **Then** the completion status persists

---

### User Story 2 - Mark Task as Incomplete (Priority: P1)

As a user, I want to mark a complete task as incomplete so that I can correct mistakes or re-open tasks.

**Why this priority**: Users need to toggle status back if they mark something complete by accident or if a task needs to be redone.

**Independent Test**: Can be fully tested by marking a task complete, then marking it incomplete, and verifying the status toggles.

**Acceptance Scenarios**:

1. **Given** a task exists with ID 1 and is complete, **When** I execute `python -m src.main incomplete 1`, **Then** the task status changes to incomplete
2. **Given** a task has been marked incomplete, **When** I list tasks, **Then** the task shows "[ ] Incomplete" status
3. **Given** I toggle task status, **When** I restart the application, **Then** the status change persists

---

### Edge Cases

- What happens when the task ID doesn't exist?
- What happens when ID is not a valid integer?
- What happens when marking an already complete task as complete?
- What happens when marking an already incomplete task as incomplete?
- What happens with no task ID provided?

## Requirements

### Functional Requirements

- **FR-001**: System MUST accept task ID for complete command
- **FR-002**: System MUST accept task ID for incomplete command
- **FR-003**: System MUST validate that task ID exists
- **FR-004**: System MUST validate that ID is a valid integer
- **FR-005**: System MUST update task completed status to true for complete command
- **FR-006**: System MUST update task completed status to false for incomplete command
- **FR-007**: System MUST persist the status change to storage
- **FR-008**: System MUST display confirmation message with task ID and new status
- **FR-009**: System MUST provide clear error messages for invalid input
- **FR-010**: System MUST handle idempotent operations (marking complete task as complete is OK)

## Success Criteria

### Measurable Outcomes

- **SC-001**: Users can successfully toggle task status in under 3 seconds
- **SC-002**: Status changes persist across application restarts 100% of the time
- **SC-003**: Clear error messages for invalid or non-existent task ID
- **SC-004**: List command correctly displays status indicators for all tasks

## Technical Notes

### Command Syntax
```bash
python -m src.main complete <ID>
python -m src.main incomplete <ID>
```

### Expected Outputs
```
[OK] Task 1 marked as complete!
[OK] Task 1 marked as incomplete!
```

### Error Outputs
```
[ERROR] Task ID 99 not found
[ERROR] Invalid task ID: must be an integer
[ERROR] Task ID is required
```

### Status Display in List
```
1     | Buy groceries     | [X] Complete   | 2025-12-26T14:56:48
2     | Complete homework | [ ] Incomplete | 2025-12-26T14:30:00
```

## Out of Scope

- Tracking completion timestamp
- Partial completion or progress tracking
- Completion history or audit trail
- Batch marking multiple tasks
- Auto-completion based on rules
