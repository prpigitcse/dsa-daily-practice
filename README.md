# Algorithm Logbook — Daily DSA Practice

A structured, consistency-driven platform for mastering Data Structures & Algorithms one problem at a time.

🌐 **Live site:** [dsa-daily-practice.vercel.app](https://dsa-daily-practice.vercel.app)

---

## Tech Stack

- **Framework:** [Next.js](https://nextjs.org) (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS v4
- **Syntax Highlighting:** highlight.js
- **Analytics:** Vercel Analytics
- **Deployment:** Vercel

---

## Getting Started

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the app.

---

## Problem Structure

Problems are organised in the `problems/` directory by month and week:

```
problems/
└── month{M}/
    └── week{W}/
        ├── week{W}-day1-{problem-slug}.py
        ├── week{W}-day2-{problem-slug}.py
        ├── ...
        └── week{W}-day7-{problem-slug}.py
```

### File Naming Convention

```
week{W}-day{D}-{problem-slug}.py
```

### Problem File Format

Each `.py` file follows a consistent docstring structure that the site parses and renders automatically:

```python
"""
Problem Statement:
<description of the problem>

Intuition:
<key insight to solve the problem>

Approach:
<step-by-step solution strategy>

Time Complexity:
<Big-O time analysis>

Space Complexity:
<Big-O space analysis>

Common Mistakes:
<pitfalls to watch out for>

Final Thoughts:
<takeaways and real-world relevance>
"""

# Actual solution code below
def solution():
    ...
```

All sections are optional — the site gracefully skips any that are missing.

---

## Adding a New Problem

1. Create a new `.py` file under the appropriate `problems/month{M}/week{W}/` directory.
2. Name it `week{W}-day{D}-{problem-slug}.py`.
3. Fill in the docstring sections listed above.
4. Add the solution code below the docstring.
5. The problem will be automatically discovered and rendered on the site — no config changes needed.

---

## Project Structure

```
app/
├── components/
│   ├── CodeBlock.tsx          # Syntax-highlighted code viewer with copy button
│   ├── CollapsibleSection.tsx # Expandable content sections
│   ├── CompletionTracker.tsx  # Per-problem completion state (localStorage)
│   ├── DailyQuote.tsx         # Motivational quote block
│   ├── MarkComplete.tsx       # Mark problem as done button
│   └── ThemeToggle.tsx        # Light / dark mode toggle
├── month-[month]/
│   └── week-[week]/
│       └── [slug]/
│           └── page.tsx       # Dynamic problem page
├── privacy/
│   └── page.tsx               # Privacy policy page
├── globals.css
├── layout.tsx                 # Root layout with header & footer
├── page.tsx                   # Home page (problem listing)
├── robots.ts
└── sitemap.ts
lib/
└── parsePracticeStructure.ts  # Reads & parses the problems/ directory
problems/                      # All DSA problem files (see above)
```

---

## License

Educational content for personal learning and reference. © Pradosh Ranjan Pattanayak
