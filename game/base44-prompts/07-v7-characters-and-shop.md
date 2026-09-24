# Pocket Island v7: a real character cast and a product shop

Update the existing **Pocket Island** app. Keep all v1 to v6 features.

## Goal of this version
1. Turn the island's residents into a **cast of serious characters with real personality**: backstory, values, flaws and relationships, so families get attached to them the way they do to characters in good children's books.
2. Build a **shop that sells Pocket Island products** (digital and physical) **to parents**, turning those characters into a brand.

---

## Part A: The cast

Change the tone of the residents: less slapstick, more character. Humor still exists, but it comes from **who the character is**, not random silly sounds. Every character has a consistent voice, look, color palette and signature object.

| Character | Who they are | Strength | Flaw | What they teach |
|---|---|---|---|---|
| **Captain Oren** (sea turtle, 180 years old) | Founded the island and keeps the lighthouse. Speaks slowly, remembers everything. | Patience, wisdom | Stubborn about "the old way" | Patience, listening |
| **Mira** (red fox, cartographer) | Maps every corner of the island, always with a pencil behind her ear. | Brave, curious | Rushes in without a plan | Curiosity, learning from mistakes |
| **Bolt** (robot built from a shipwreck) | The island's engineer. Logical and literal. | Builds anything | Doesn't understand jokes or feelings (yet) | Problem solving, understanding others |
| **Nana Pip** (hedgehog, baker and healer) | Warm and firm. Everyone comes to her kitchen. | Caring, practical | Afraid of storms | Kindness, facing fears |
| **Kavi** (owl, librarian and storyteller) | Knows every story but is too shy to tell them out loud. | Knowledge, imagination | Shyness | Courage, self-expression |
| **Zuzu** (monkey, trickster) | Causes trouble, but is honest at heart and always fixes what she breaks. | Creative, funny | Acts before thinking of others | Responsibility, honesty |

**Relationships (use them in stories):** Mira and Bolt argue about "go now" versus "plan first", and learn from each other. Zuzu plays tricks on Captain Oren, who secretly enjoys them. Kavi writes down all of Nana Pip's recipes. Bolt tries to understand why Zuzu laughs.

**Character arcs:** each character has a 5-adventure **Story Saga** in which they grow: Kavi finally tells a story at the island festival, Bolt learns what "sad" means, Nana Pip goes through a storm to help a friend, and so on.

**In the game:**
- A "Meet the Island" gallery: each character has a page with their story, favorite things, drawings and a voice line. No prices here.
- Characters appear in existing adventures with consistent personalities.
- The child's own creatures can befriend the cast (e.g. Bolt builds your creature a house).
- Create a character style guide page in the admin (colors, poses, expressions, do and don't) so every product looks consistent.

**Character rules:**
- Characters never ask the child to buy anything, never say they "need" a product, and are never sad or disappointed because of something the child didn't do or buy.
- No products appear inside adventures or stories.

---

## Part B: The shop (for parents)

### Where it lives
- **Parent Shop** inside the parent zone (behind the parent gate).
- **A public shop page** on the website (outside the game) that parents can reach directly, with a hero banner of the cast.
- The child's area has **no shop, no prices and no buy buttons**. Locked content shows only: "Ask a grown-up to open this part of the island."

### Digital products
- **Character Saga packs:** each character's 5-adventure saga, sold separately or as "All Sagas" at a discount.
- **Pocket Island Full** (one-time) and **Family Plan** (subscription), as in v5.
- **Gift cards:** a parent or grandparent buys the game or a saga as a gift. The recipient gets a code by email.

### Physical products (character merchandise)
- **Plush toys** of each of the 6 characters.
- **Illustrated storybooks:** one hardcover per character saga.
- **"My Creature" personalized products**, the star product: the child's own creature from the game printed as a **personalized storybook** (the child's creature goes on an adventure with the cast), a **poster of the child's island**, or a **sticker sheet**.
- **Coloring books and sticker packs** of the cast.
- **Bundles:** e.g. "Kavi plush + Kavi's storybook".

### Product pages
- Large photos, character-themed design, price in real currency (₪ and $), shipping cost and delivery time shown up front.
- For personalized products: a live preview built from the child's actual creation (the parent picks which creature).
- Reviews from parents only (verified purchases).

### Checkout and orders
- Cart, shipping address and payment (Stripe) for the parent only.
- Save orders in an **Orders** table: products, personalization data, address, status (new / in production / shipped / delivered).
- **Admin order page:** list of orders, filters, status update and CSV export for the print and fulfillment partner.
- For personalized items, generate a high-resolution print file (PDF) of the creature, book pages or poster and attach it to the order.

### Emails
- Order confirmation with a summary and receipt.
- Status emails: "in production", "shipped" (with a tracking number field), "delivered".
- An email to the **store owner** for every new order, with the print file attached.
- **Marketing emails are a separate opt-in** (a separate checkbox, unchecked by default, not bundled with the weekly digest). At most one per month, on a **scheduled task on the 1st of the month**: "New on the island this month" with new sagas and products. Always with one-tap unsubscribe.
- Abandoned cart: at most **one** gentle reminder email 24 hours later, only to parents who opted in to marketing, with no fake urgency ("only 2 left", "price goes up tonight" are forbidden).

### Promotions (allowed)
- Seasonal bundles (e.g. holiday gift box) that are available for a normal season, with no countdown timers.
- A coupon code field at checkout.
- "Buy the plush, get the digital saga free" bundles.

### Admin: products and sales
- Manage products: name, character, type (digital / physical / personalized), price, stock, images, active or inactive.
- Sales dashboard: revenue per day, week and month; best-selling products; best-selling character; share of orders that are personalized; average order value.

---

## Hard rules (still apply)
- No ads. No shop, prices or buy buttons in the child's area. Only a parent, behind the parent gate, can buy.
- No virtual currency, loot boxes or paid random rewards.
- No streaks, countdown timers, "limited time" or "only X left" pressure.
- Characters never pressure, guilt or ask the child for anything.
- The child never enters an email, name, address or photo. Shipping and payment details belong to the parent only.
- Marketing emails only with a separate opt-in, at most monthly, always with unsubscribe.

## Done when
- Each of the 6 characters has a gallery page, a consistent look and a playable 5-adventure saga.
- A parent can buy a plush, a saga pack and a personalized "My Creature" book in one order, receive confirmation and status emails, and the owner receives the order with a print-ready PDF.
- Tapping every locked item in the child's area never shows a price or a shop.
- The admin sales dashboard shows revenue and best sellers.
