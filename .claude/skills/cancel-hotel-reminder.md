# Cancel Hotel Reminder

Cancel or modify scheduled reminders using the hotel-reminder-scheduler agent.

## Usage

This skill manages reminder cancellations for:
- Guest check-ins/check-outs that changed
- Cancelled reservations
- Rescheduled maintenance
- Modified housekeeping schedules
- Changed wake-up call times

## Prompt

Use the hotel-reminder-scheduler agent to cancel or modify a scheduled reminder. Gather:
- Reminder identifier (time, room number, or description)
- Action (cancel completely or reschedule)
- If rescheduling: new date and time
- Reason for cancellation (optional)

Cancel or update the reminder and confirm the action. If multiple matching reminders are found, list them and ask for clarification.
