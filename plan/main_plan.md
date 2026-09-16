# One-Month HTML/CSS/JS Course for Two Beginner Students (ages ~10-12)

## Context
The user is privately tutoring two beginner students, 3 sessions/week (Wed, Sat, Sun). Homework is assigned Saturday and reviewed the following Wednesday (Sunday has no homework check, since there's no gap before it). In one month (12 lessons) the course must cover HTML, CSS, and JS basics. For every lesson the user wants two deliverables — one lesson **HTML** page and one **PPT** slide deck — built from a fixed, simplified structure, with small files and no overcomplication. This plan lays out the 12-lesson curriculum and the concrete files to generate.

Decisions confirmed with the user:
- PPTs will be real `.pptx` files, generated with `python-pptx` (needs `pip install python-pptx` — not yet installed).
- Layout: `week1/`…`week4/` folders, each containing one subfolder per lesson with `lesson.html` + `slides.pptx` inside.

## Curriculum (12 lessons)

**Week 1 — HTML Foundations**
1. Wed — What is HTML? Page structure (`<!DOCTYPE>`, `html`, `head`, `body`), headings, paragraphs, comments.
2. Sat — Text formatting (bold/italic/line breaks), lists (`ul`/`ol`/`li`), links (`a`), images (`img`). *Homework assigned.*
3. Sun — Tables (`table`/`tr`/`td`/`th`), `div`/`span`, intro to semantic tags (`header`, `nav`, `main`, `footer`).

**Week 2 — HTML wrap-up + CSS intro**
4. Wed — *Check Sat HW.* Forms & inputs (`form`, `input` types, `label`, `button`).
5. Sat — Intro to CSS: what CSS is, 3 ways to apply it (inline/internal/external), selectors (element/class/id), colors & fonts. *Homework assigned.*
6. Sun — CSS Box Model: margin, border, padding, width/height.

**Week 3 — CSS deep dive**
7. Wed — *Check Sat HW.* Text styling & backgrounds (`font-family`, `font-size`, `text-align`, `background-color`, `background-image`).
8. Sat — Flexbox basics (`display:flex`, `justify-content`, `align-items`, `flex-direction`). *Homework assigned.*
9. Sun — Mini project: build a simple "profile card" page combining everything from Weeks 1–3.

**Week 4 — JavaScript basics**
10. Wed — *Check Sat HW.* Intro to JS: variables (`let`/`const`), data types, `console.log`, linking a `.js` file to HTML.
11. Sat — Operators, `if`/`else`, simple functions. *Homework assigned.*
12. Sun — DOM basics: `getElementById`/`querySelector`, changing text/style, click events. Final mini project combining HTML+CSS+JS.

Every lesson's **exercises** section is cumulative — it reuses concepts from all prior lessons plus the new material, per the user's requirement ("from what has been covered so far and so far in this lesson"). No images are used anywhere (user confirmed not needed at this basic level); everything stays plain HTML/CSS/JS snippets.

## File/Content structure (identical for every lesson)
Each `lesson.html` follows exactly this order:
1. **Topic** (title)
2. **Description** (2-4 simple sentences, no jargon)
3. **Key Concepts** (short bullet list)
4. **Code Samples/Snippets** (small `<pre><code>` blocks, each with a one-line plain-English definition above it)
5. **Examples** (a slightly bigger worked example showing the concepts together)
6. **Exercises** (3-5 short, easy tasks — cumulative with prior lessons)

Each `slides.pptx` mirrors the same structure in ~6-8 slides: Title → Description → Key Concepts → 1-2 Code slides → Example → Exercises. Plain, large, readable text (kid-friendly), one consistent simple color theme, no images.

## Implementation steps
1. `pip3 install python-pptx` (only new dependency needed).
2. Create folder tree under `/Users/furb-x/Desktop/new_lesson/`:
   - `week1/lesson01_wed_html_intro/`, `week1/lesson02_sat_text_lists_links_images/`, `week1/lesson03_sun_tables_divs_semantic/`
   - `week2/lesson04_wed_forms/`, `week2/lesson05_sat_css_intro/`, `week2/lesson06_sun_box_model/`
   - `week3/lesson07_wed_text_backgrounds/`, `week3/lesson08_sat_flexbox/`, `week3/lesson09_sun_mini_project_layout/`
   - `week4/lesson10_wed_js_intro/`, `week4/lesson11_sat_operators_conditionals_functions/`, `week4/lesson12_sun_dom_final_project/`
3. Write one shared, small `style.css` at project root (simple, friendly, readable — big headings, soft colors, code blocks styled) that every `lesson.html` links to via a relative path.
4. Write a single Python data file (`generate/lessons_data.py`) holding all 12 lessons' content (topic, description, key concepts, code snippets + definitions, example, exercises) — this is the actual authored curriculum content.
5. Write one generator script (`generate/build.py`) that reads the data file and, for each lesson, produces:
   - `lesson.html` from an HTML template following the fixed 6-part structure above.
   - `slides.pptx` via `python-pptx` following the same structure.
6. Run the generator to produce all 24 files.
7. Write a root `index.html` — a simple one-page course overview/schedule table (Week/Day/Topic) linking to every `lesson.html`, so the user has one entry point.
8. Spot-check: read 2-3 generated `lesson.html` files and re-open 1-2 `.pptx` files (via python-pptx) to confirm structure/content came through correctly; verify file sizes stay small.
9. Leave the `generate/` scripts in the project (not deleted) so the user can tweak wording later and regenerate instead of hand-editing 24 files.

## Verification
- Open a couple of `lesson.html` files directly (file:// or a quick static server) to confirm styling renders and structure/order is correct.
- Confirm each `.pptx` opens and slide count/content matches the lesson (re-read via `python-pptx`).
- Confirm folder/file count: 12 lesson folders × 2 files + shared `style.css` + root `index.html` + `generate/` scripts.
