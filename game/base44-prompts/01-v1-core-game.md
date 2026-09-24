# Pocket Island v1: core game

Build a mobile-first web game for children aged 4 to 12 called **"Pocket Island"**.

## Concept
The child looks after a small, friendly island. They design their own creatures, decorate the island, and help the island's residents through short, funny puzzle adventures. Children should want to come back because it's fun and surprising, not because they feel pressured.

## Core loop (3 modes, reachable from one home screen)
1. **Create:** build creatures from parts (body, eyes, ears, tail, pattern, color) and name them. Paint and decorate the island with drag-and-drop items: trees, houses, bridges, flowers. Everything the child makes is saved and visible on the island.
2. **Adventures:** short quests of 3 to 5 minutes, e.g. "the penguin lost his hat in the jungle", "help the bees get home". Each quest is a light puzzle: matching, find the path, sort by color and shape, simple counting and logic. Every quest ends with a funny animated ending and a clear, calm stopping point ("The island is asleep. See you next time!").
3. **Explore:** walk around the island, tap anything and something funny happens (a tree sneezes, a fish jumps). Hide small surprises everywhere.

**Coming back:** between visits the island changes gently. A new flower has bloomed, a new creature has come to visit, a house has grown taller. **Nothing is ever lost, wilts or gets "punished"** while the child is away.

## Three age levels (chosen in the parent zone)
- **Little (4-6):** no reading needed at all. Voice narration, icons, large buttons, very simple puzzles, no failure (a wrong answer gets a gentle hint).
- **Middle (7-9):** short text with optional narration, medium puzzles, a few more parts for creatures.
- **Big (10-12):** harder logic puzzles, longer stories with jokes.
- Difficulty adjusts itself quietly: after 2 mistakes it gets easier, after easy successes it gets a little harder.

## Look and sound
Colorful, rounded and cheerful, like a picture book. Short, smooth animations. Pleasant music with a mute button always visible. Lots of humor: silly sounds, creatures that react to touch.

## Hard rules (must not be broken)
- No ads of any kind.
- No purchases inside the child's area. The child never sees a store, prices or "buy" buttons.
- No virtual currency, no loot boxes or surprise boxes, no random rewards bought with money.
- No streaks, no "you missed a day", no countdown timers, no limited-time offers.
- No notifications that create guilt or FOMO. No notifications at all by default.
- No chat, no contact with other users, no friends list.
- No creature that is "sad" or "hungry" because the child didn't come in.
- A visible exit button on every screen. The child can stop at any moment and nothing is lost.
- No sign-up for the child. No name, email, location or photo collected from the child. Progress is saved locally on the device.

## Parent zone
- Behind a parent gate (e.g. "press and hold for 3 seconds and solve 14 + 9").
- Choose the age level, turn sound on or off, reset progress.
- An optional daily play reminder that the *parent* sets. The game ends a session with a friendly screen, never with a hard cutoff mid-activity.
- A short summary: which adventures were completed and what the child created (a creations gallery the parent can save as images).
- Purchases happen only here: the first area is free, then a one-time purchase unlocks the whole island, or there is a family subscription with new content every month.
- A clear page explaining what data is stored (only local progress) and why.

## Technical
- Mobile-first responsive web, works great on a phone in portrait and on a tablet.
- Installable as a PWA and works offline after the first load.
- Touch targets at least 48px, fast load, no lag.
- Accessible: high contrast, color is never the only cue in a puzzle, narration for everything in Little mode.

## Scope of this version
Home screen, creature creator, an island with decoration, 6 full adventures (2 per age level), the explore mode with surprises, and the parent zone with the gate and settings (payment flow as a placeholder).
