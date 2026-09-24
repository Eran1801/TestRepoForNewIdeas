# Pocket Island v6: Hebrew and English, accessibility, healthy metrics, launch

Update the existing **Pocket Island** app. Keep all v1 to v5 features.

## Goal of this version
Get ready for launch: two languages, full accessibility, performance, and success metrics that measure fun rather than screen time.

## 1. Hebrew and English
- Full support for **Hebrew (right-to-left)** and **English**. The parent chooses the language in the parent zone; the default follows the device language.
- Mirror the layout correctly for RTL (menus, arrows, path puzzles, reading direction in stories).
- Record narration in both languages for everything in Little mode (4-6).
- Jokes and names should be adapted for each language, not just translated word for word.

## 2. Accessibility
- All puzzles are playable without relying on color alone (use shapes and patterns too).
- Larger-text option and a "calm mode" (softer colors, fewer animations, no sudden sounds).
- Works with the screen reader for parent-zone screens.
- A left-handed layout option.

## 3. Healthy success metrics (parent dashboard + internal admin page)
Track only anonymous, aggregated counts; no tracking of the individual child beyond what the game needs:
- **Voluntary return:** share of families who come back after a break of 3 days or more.
- **Satisfying endings:** share of sessions that end through the calm "Go to sleep" ending rather than the app being closed mid-activity.
- **Creations:** number of creatures, adventures and tunes made per week.
- **Parent satisfaction:** a monthly one-question email (scheduled task, 1st of the month, opted-in parents only): "How do you feel about Pocket Island for your child?" with 5 faces, answered with one tap.
- **Do not** show or optimize for time spent, session length or daily active streaks anywhere.

## 4. Performance and reliability
- First load under 3 seconds on a mid-range phone on 4G. Compress images and audio.
- Everything playable offline after the first load; sync when back online.
- Friendly error screens with a creature ("Oops, the boat got lost at sea. Try again!").

## 5. Launch checklist page (internal admin only)
- List all scheduled tasks (Sunday digest, nightly island, monthly visitor, 15th coloring page, renewal reminders, monthly survey) with last run time and status, plus a "Run now" test button for each.
- List every email template, with a preview in both languages.
- A "privacy check" section confirming: no ads SDK, no third-party trackers, no child emails stored, and a working "delete everything" button.

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
- Switching to Hebrew mirrors every screen correctly and all Little-mode narration plays in Hebrew.
- The admin page shows all scheduled tasks running successfully.
- Nowhere in the app or admin is "time spent" or "session length" shown as a goal.
