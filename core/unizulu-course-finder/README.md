# UNIZULU Course Finder — Frontend (4CPS212 Group Project)

A responsive, bilingual (English / isiZulu) chatbot-style front end for the
University of Zululand course/programme advisor. **Frontend only** — plain
HTML, CSS and vanilla JavaScript. No frameworks, no build step, no backend.
Your Django app + database will plug in where noted below.

## Folder structure
```
unizulu-course-finder/
├── index.html          → page structure (3 tabs: Chat, My Marks, Feedback)
├── css/
│   └── style.css       → UNIZULU brand styling (blue, maroon, yellow, grey, white)
├── js/
│   └── script.js       → language toggle, tab switching, APS calculator,
│                          chatbot demo logic, form handling
├── assets/
│   └── unizulu-logo.png→ university emblem (cropped from official crest)
└── README.md
```

## Running it

**VS Code**
1. Open the `unizulu-course-finder` folder in VS Code.
2. Install the "Live Server" extension (optional but recommended).
3. Right-click `index.html` → "Open with Live Server".
   (Or just double-click `index.html` to open it directly in a browser.)

**PyCharm**
1. Open the folder as a PyCharm project.
2. Right-click `index.html` in the project tree → "Open in Browser".
   PyCharm's built-in preview server works too (the small browser icons
   in the top-right gutter of the HTML editor).

No `pip install` or `npm install` is needed — it's static HTML/CSS/JS.

## What's implemented (frontend demo)
- **Header** with the UNIZULU emblem, title, and an EN / ZU language toggle
  that translates all interface text live.
- **Chat tab** — a chat-style UI with a welcome message, quick-reply chips,
  and a free-text input. Replies are currently **rule-based placeholders**
  (keyword matching in `script.js`) so the interface is fully clickable
  and demoable before the backend is wired up.
- **My Marks tab** — a form with Full Name, Email, and a dropdown per NSC
  subject (achievement levels 1–7). An **APS score updates live** as levels
  are selected. Data is currently saved to the browser's `localStorage` so
  the demo persists between reloads.
- **Feedback tab** — feedback type pills, a 5-star rating, and a message
  box, saved to `localStorage` on submit.
- Fully **responsive**: tab labels collapse to icons, forms stack to a
  single column, and the chat window resizes on phones.

## Where the Django backend plugs in
Everything that currently reads/writes `localStorage` in `js/script.js` is
meant to be swapped for `fetch()` calls to your Django REST endpoints:

| Frontend demo behaviour                         | Replace with |
|--------------------------------------------------|--------------|
| `botReply()` keyword matching                     | `POST /api/chat/` → Django view queries the programmes DB and returns a real answer |
| `localStorage.setItem("unizulu_marks", ...)`      | `POST /api/marks/` → save learner marks to the DB |
| `loadSavedMarks()`                                | `GET /api/marks/<id>/` → fetch saved marks |
| `localStorage.setItem("unizulu_feedback", ...)`   | `POST /api/feedback/` → save feedback to the DB |
| Static `SUBJECTS` array                           | `GET /api/subjects/` → subject list from DB (optional) |

The HTML/CSS structure and element IDs are kept simple and consistent
specifically so a teammate can wire up the API calls without needing to
restructure the markup.

## Brand notes
Colours are drawn from the official UNIZULU crest: deep blue (primary),
maroon (accents, e.g. the bug-report pill), yellow (highlights, star
ratings, active tab underline), grey (neutral text/borders) and white
(base background). Headings use Poppins; body text uses Inter.
