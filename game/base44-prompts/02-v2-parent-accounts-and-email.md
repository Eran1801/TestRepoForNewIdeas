# Pocket Island v2: parent accounts, cloud save and weekly parent email

Update the existing **Pocket Island** app. Keep everything that works today; do not redesign the child's screens.

## Goal of this version
Let a parent optionally create an account so progress is backed up and they receive a short, friendly weekly email about what their child created. The game must still work fully **without** any account.

## 1. Optional parent account
- In the parent zone (behind the parent gate), add "Create a parent account" and "Log in".
- Sign-up asks for the parent's email and password only, plus two separate checkboxes (both unchecked by default): "Back up progress to the cloud" and "Send me a weekly summary email".
- Add a clear confirmation that the parent is an adult and is the child's parent or guardian.
- The child's screens never show login, account or email UI.

## 2. Cloud save
- If "Back up progress" is on, sync the island, creatures and completed adventures to the parent's account.
- Local play keeps working offline; sync happens in the background when online. On conflict, keep the version with the most recent change and never delete creations.
- Parent zone: "Restore on a new device" (log in, then the island appears) and "Delete all cloud data" (deletes immediately and confirms by email).

## 3. Weekly parent email (scheduled task)
- Create a **scheduled task that runs every Sunday at 18:00** (parent's local time zone, fall back to UTC).
- For each parent who opted in and whose child played that week, send one email:
  - Subject: "What happened on Pocket Island this week"
  - Up to 3 images of creatures or island scenes the child created that week
  - Adventures completed (names only)
  - One "talk about it together" question, e.g. "Ask them what their newest creature's name is and why."
- If the child did not play that week: **send nothing**. Never send "we miss you" emails.
- Footer: what data is stored, a link to the parent zone, and a one-tap unsubscribe link.

## 4. Welcome email
- When a parent creates an account, send one welcome email explaining: what is stored, what is never collected, how to turn off emails, and how to delete everything.

## 5. Small fixes
- Make the exit button a friendly "Go to sleep" icon that takes the child to a calm goodbye screen and saves automatically.
- Add a "Saved ✓" indicator after every change.

## Hard rules (unchanged, still apply to everything in this version)
- No ads. No store, prices or "buy" buttons anywhere in the child's area.
- No virtual currency, loot boxes, surprise boxes or paid random rewards.
- No streaks, "you missed a day", countdown timers or limited-time offers.
- No chat, no contact between users, no friends list.
- No creature is ever sad, hungry or hurt because the child was away. Nothing is ever lost.
- A visible exit button on every screen; the child can stop at any moment without losing anything.
- The child never signs up and never types an email, a real name, a location or a photo.
- Emails go **only to the parent**, only after the parent opts in, always with a one-tap unsubscribe link, and never contain marketing, urgency or guilt ("your child misses the island" is forbidden).

## Done when
- The game works end to end with no account.
- A parent can sign up, turn on backup, move to a second device and see the same island.
- The Sunday task sends the digest only to opted-in parents whose child played, and the unsubscribe link works.
- "Delete all cloud data" removes everything and sends a confirmation email.
