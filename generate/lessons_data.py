# -*- coding: utf-8 -*-
"""
All course content lives here. Edit this file to change wording, then re-run
build.py to regenerate every lesson.html and slides.pptx.

Each lesson is a dict with:
  id, folder, week, day, order, topic, description,
  key_concepts: [str, ...]
  snippets: [{"def": str, "code": str}, ...]
  example: {"desc": str, "code": str}
  exercises: [str, ...]   (cumulative — includes review of earlier lessons)
  homework: bool
  checks_hw_from: str or None  (id of the lesson whose homework is reviewed today)
"""

LESSONS = [

    # ---------------- WEEK 1 : HTML FOUNDATIONS ----------------
    {
        "id": "lesson01",
        "folder": "week1/lesson01_wed_html_intro",
        "week": 1, "day": "Wednesday", "order": 1,
        "topic": "What is HTML? Building Your First Web Page",
        "description": (
            "HTML (HyperText Markup Language) is the language used to build the content "
            "of every website. It uses ‘tags’ to tell the browser what each piece of "
            "text is — a title, a paragraph, and so on. Today we write our very first "
            "web page from scratch."
        ),
        "key_concepts": [
            "HTML is the structure (skeleton) of a webpage",
            "Tags come in pairs: an opening tag and a closing tag",
            "Every page starts with <!DOCTYPE html>",
            "<html>, <head>, and <body> are the three main parts",
            "Headings <h1>–<h6> and paragraphs <p>",
            "Comments <!-- --> are notes the browser ignores",
        ],
        "snippets": [
            {"def": "This line tells the browser: ‘this is a modern HTML page’.",
             "code": "<!DOCTYPE html>"},
            {"def": "The <html> tag wraps everything on the page.",
             "code": "<html>\n  ...\n</html>"},
            {"def": "<head> holds info about the page (like the browser tab title). <body> holds what you actually SEE.",
             "code": "<head>\n  <title>My Page</title>\n</head>\n<body>\n  ...\n</body>"},
            {"def": "Headings go from biggest (h1) to smallest (h6). Paragraphs hold normal text.",
             "code": "<h1>Biggest Title</h1>\n<h2>Smaller Title</h2>\n<p>This is a paragraph of text.</p>"},
            {"def": "Comments are notes for humans — the browser skips them completely.",
             "code": "<!-- This is a comment, the browser ignores it -->"},
        ],
        "example": {
            "desc": "A tiny but complete web page:",
            "code": (
                "<!DOCTYPE html>\n"
                "<html>\n"
                "<head>\n"
                "  <title>My First Page</title>\n"
                "</head>\n"
                "<body>\n"
                "  <!-- This page is about me -->\n"
                "  <h1>Hello, I'm Ali!</h1>\n"
                "  <p>I am learning HTML this month.</p>\n"
                "</body>\n"
                "</html>"
            ),
        },
        "exercises": [
            "Create a new file called index.html with the basic structure (doctype, html, head with a title, body).",
            "Add one <h1> heading with your name.",
            "Add two <p> paragraphs about your favorite hobby.",
            "Add a comment above the body explaining what the page is about.",
        ],
        "homework": False,
        "checks_hw_from": None,
    },
    {
        "id": "lesson02",
        "folder": "week1/lesson02_sat_text_lists_links_images",
        "week": 1, "day": "Saturday", "order": 2,
        "topic": "Formatting Text, Lists, Links & Images",
        "description": (
            "Now that you can build a page, let's make it richer: bold and italic text, "
            "bullet and numbered lists, clickable links, and pictures."
        ),
        "key_concepts": [
            "<strong> for bold, <em> for italic",
            "<br> for a line break, <hr> for a divider line",
            "Unordered (bullet) list: <ul><li>",
            "Ordered (numbered) list: <ol><li>",
            "Links: <a href=\"...\">text</a>",
            "Images: <img src=\"...\" alt=\"...\">",
        ],
        "snippets": [
            {"def": "strong makes text bold and important; em makes text emphasized (italic).",
             "code": "<p>This is <strong>important</strong> and this is <em>emphasized</em>.</p>"},
            {"def": "br breaks to a new line; hr draws a horizontal divider line.",
             "code": "<p>Line one<br>Line two</p>\n<hr>"},
            {"def": "ul makes a bullet list, ol makes a numbered list — each item goes in <li>.",
             "code": "<ul>\n  <li>Apples</li>\n  <li>Bananas</li>\n</ul>\n<ol>\n  <li>Wake up</li>\n  <li>Brush teeth</li>\n</ol>"},
            {"def": "href is the address the link goes to; the text between the tags is what people click.",
             "code": "<a href=\"https://www.google.com\">Go to Google</a>"},
            {"def": "src is the image file; alt describes the image (for people who can't see it).",
             "code": "<img src=\"cat.jpg\" alt=\"A cute orange cat\">"},
        ],
        "example": {
            "desc": "A small ‘My Favorite Things’ page:",
            "code": (
                "<h1>My Favorite Things</h1>\n"
                "<p>I <strong>really</strong> love pizza and I <em>kind of</em> like broccoli.</p>\n"
                "<ul>\n"
                "  <li>Pizza</li>\n"
                "  <li>Football</li>\n"
                "  <li>Video games</li>\n"
                "</ul>\n"
                "<a href=\"https://www.nasa.gov\">Visit NASA</a>\n"
                "<img src=\"space.jpg\" alt=\"A photo of outer space\">"
            ),
        },
        "exercises": [
            "Review: make sure your page still has the correct doctype/html/head/body structure.",
            "Add a bulleted list of 3 things you like.",
            "Add a numbered list of 3 steps to do something (e.g. make a sandwich).",
            "Add a link to your favorite website.",
            "Add an image with a good alt text describing it.",
        ],
        "homework": True,
        "checks_hw_from": None,
    },
    {
        "id": "lesson03",
        "folder": "week1/lesson03_sun_tables_divs_semantic",
        "week": 1, "day": "Sunday", "order": 3,
        "topic": "Tables, Divs, Spans & Semantic Tags",
        "description": (
            "Websites need ways to group content and show data in rows and columns. "
            "Today: tables for data, div/span as generic containers, and semantic tags "
            "that describe what a section of the page is for."
        ),
        "key_concepts": [
            "<table>, <tr> (row), <td> (cell), <th> (header cell)",
            "<div> = a block container (starts on a new line)",
            "<span> = an inline container (stays in the text flow)",
            "Semantic tags: <header>, <nav>, <main>, <footer>",
            "Semantic tags make pages easier to read and understand",
        ],
        "snippets": [
            {"def": "A table is built from rows (tr) made of cells (td); th is a bold header cell.",
             "code": "<table>\n  <tr>\n    <th>Name</th>\n    <th>Age</th>\n  </tr>\n  <tr>\n    <td>Ali</td>\n    <td>11</td>\n  </tr>\n</table>"},
            {"def": "div groups a block of content; span highlights a small piece of text inside a sentence.",
             "code": "<div>\n  This is a block. It starts on a new line.\n</div>\n<p>This has a <span>highlighted word</span> inside it.</p>"},
            {"def": "Semantic tags name what each part of the page is for, instead of using plain divs everywhere.",
             "code": "<header>My Website</header>\n<nav>Home | About | Contact</nav>\n<main>Main content goes here.</main>\n<footer>Made by me, 2026</footer>"},
        ],
        "example": {
            "desc": "A simple class schedule table inside a semantic page layout:",
            "code": (
                "<header><h1>My Website</h1></header>\n"
                "<nav>Home | About</nav>\n"
                "<main>\n"
                "  <table>\n"
                "    <tr><th>Day</th><th>Subject</th></tr>\n"
                "    <tr><td>Monday</td><td>Math</td></tr>\n"
                "    <tr><td>Tuesday</td><td>Art</td></tr>\n"
                "  </table>\n"
                "</main>\n"
                "<footer>Thanks for visiting!</footer>"
            ),
        },
        "exercises": [
            "Build a table showing 3 friends' names and favorite colors.",
            "Wrap your page content in <header>, <main>, and <footer> tags.",
            "Use a <div> to group the list you made in Lesson 2.",
            "Use a <span> to highlight one word inside a paragraph.",
            "Review: check that your page still has a link and an image from Lesson 2.",
        ],
        "homework": False,
        "checks_hw_from": None,
    },

    # ---------------- WEEK 2 : HTML WRAP-UP + CSS INTRO ----------------
    {
        "id": "lesson04",
        "folder": "week2/lesson04_wed_forms",
        "week": 2, "day": "Wednesday", "order": 4,
        "topic": "Forms & Inputs — Getting Info From Users",
        "description": (
            "Forms let a website ask the user questions, like a name or an email address. "
            "Today we learn the basic pieces of a form — later, JavaScript will make them "
            "actually do something."
        ),
        "key_concepts": [
            "<form> wraps all the pieces of a form",
            "<input type=\"text\"> for typed answers",
            "<input type=\"number\">, type=\"email\" for special answers",
            "<label> describes what an input is for",
            "<input type=\"checkbox\"> for yes/no choices",
            "<button> to submit the form",
        ],
        "snippets": [
            {"def": "label describes the input; the for and id must match so they're connected.",
             "code": "<label for=\"name\">Your Name:</label>\n<input type=\"text\" id=\"name\" name=\"name\">"},
            {"def": "type changes what kind of answer the input expects.",
             "code": "<input type=\"number\" placeholder=\"Your age\">\n<input type=\"email\" placeholder=\"you@example.com\">"},
            {"def": "A checkbox can be checked or unchecked — great for yes/no questions.",
             "code": "<input type=\"checkbox\" id=\"agree\">\n<label for=\"agree\">I agree</label>"},
            {"def": "A button submits the form when clicked.",
             "code": "<button>Submit</button>"},
        ],
        "example": {
            "desc": "A simple sign-up form:",
            "code": (
                "<h1>Sign Up</h1>\n"
                "<form>\n"
                "  <label for=\"name\">Name:</label>\n"
                "  <input type=\"text\" id=\"name\"><br>\n"
                "  <label for=\"email\">Email:</label>\n"
                "  <input type=\"email\" id=\"email\"><br>\n"
                "  <input type=\"checkbox\" id=\"fun\">\n"
                "  <label for=\"fun\">I like having fun</label><br>\n"
                "  <button>Submit</button>\n"
                "</form>"
            ),
        },
        "exercises": [
            "Build a small form asking for a name and favorite color (text inputs).",
            "Add a submit button to your form.",
            "Add one checkbox for ‘I like pizza’.",
            "Put your form inside a <main> tag with an <h1> title above it.",
            "Review: add a table under the form with 2 example rows of data (Lesson 3).",
        ],
        "homework": False,
        "checks_hw_from": "lesson02",
    },
    {
        "id": "lesson05",
        "folder": "week2/lesson05_sat_css_intro",
        "week": 2, "day": "Saturday", "order": 5,
        "topic": "Intro to CSS — Making Pages Pretty",
        "description": (
            "CSS (Cascading Style Sheets) controls how HTML looks — colors, fonts, "
            "spacing. Today we learn the 3 ways to add CSS and how to ‘select’ which "
            "HTML elements to style."
        ),
        "key_concepts": [
            "CSS is the styling language for HTML",
            "Inline CSS: a style=\"...\" attribute on one tag",
            "Internal CSS: a <style> block inside <head>",
            "External CSS: a separate .css file linked with <link>",
            "Selectors: element (p), class (.name), id (#name)",
            "Common properties: color, background-color, font-family, font-size",
        ],
        "snippets": [
            {"def": "Inline CSS styles just one single tag, written right on it.",
             "code": "<p style=\"color: blue;\">Blue text</p>"},
            {"def": "Internal CSS goes inside a <style> tag in the <head> and can style the whole page.",
             "code": "<style>\n  p {\n    color: green;\n  }\n</style>"},
            {"def": "External CSS lives in its own .css file and is linked into the HTML page.",
             "code": "<link rel=\"stylesheet\" href=\"style.css\">\n\n/* inside style.css */\np { color: purple; }"},
            {"def": "A class selector (.name) can be reused on many tags; an id selector (#name) is for one unique tag.",
             "code": "p { color: black; }        /* every paragraph */\n.highlight { color: red; }  /* class=\"highlight\" */\n#title { font-size: 30px; } /* id=\"title\" */"},
        ],
        "example": {
            "desc": "A page styled with an internal <style> block:",
            "code": (
                "<head>\n"
                "  <style>\n"
                "    #title { color: darkgreen; font-size: 32px; }\n"
                "    .highlight { color: orange; font-family: Arial; }\n"
                "  </style>\n"
                "</head>\n"
                "<body>\n"
                "  <h1 id=\"title\">Welcome!</h1>\n"
                "  <p class=\"highlight\">This paragraph stands out.</p>\n"
                "</body>"
            ),
        },
        "exercises": [
            "Add an internal <style> block to your page from Lesson 4.",
            "Give your <h1> a color and a font-family.",
            "Create a class called .highlight and use it on one paragraph.",
            "Give one element an id and style it differently using that id.",
            "Review: check your form, table, list, link and image are all still on the page.",
        ],
        "homework": True,
        "checks_hw_from": None,
    },
    {
        "id": "lesson06",
        "folder": "week2/lesson06_sun_box_model",
        "week": 2, "day": "Sunday", "order": 6,
        "topic": "The CSS Box Model",
        "description": (
            "Every HTML element is a box! Today we learn the 4 layers of every box — "
            "content, padding, border, and margin — and how to control width and height."
        ),
        "key_concepts": [
            "Every element on a page is a rectangular box",
            "Order (inside to outside): content → padding → border → margin",
            "width and height control the content size",
            "padding = space inside the border",
            "margin = space outside the border, between elements",
        ],
        "snippets": [
            {"def": "width and height set the size of the box's content area.",
             "code": "div {\n  width: 200px;\n  height: 100px;\n}"},
            {"def": "padding adds space inside the box; border draws a line around it; margin adds space outside it.",
             "code": "div {\n  padding: 10px;\n  border: 2px solid black;\n  margin: 20px;\n}"},
            {"def": "Four numbers set top, right, bottom, left — in that order, clockwise.",
             "code": "/* top right bottom left */\ndiv {\n  padding: 10px 20px 10px 20px;\n}"},
        ],
        "example": {
            "desc": "A simple styled ‘card’ box:",
            "code": (
                ".card {\n"
                "  width: 220px;\n"
                "  padding: 16px;\n"
                "  border: 2px solid #4a7c59;\n"
                "  margin: 20px;\n"
                "  background-color: #eef6ee;\n"
                "}"
            ),
        },
        "exercises": [
            "Pick one <div> on your page and give it a width, padding, border, and margin.",
            "Change its background-color.",
            "Try changing the margin and padding numbers and see what happens.",
            "Review: make sure your CSS is still inside a <style> tag (Lesson 5).",
            "Review: your <h1> should still have a color from Lesson 5.",
        ],
        "homework": False,
        "checks_hw_from": None,
    },

    # ---------------- WEEK 3 : CSS DEEP DIVE ----------------
    {
        "id": "lesson07",
        "folder": "week3/lesson07_wed_text_backgrounds",
        "week": 3, "day": "Wednesday", "order": 7,
        "topic": "Styling Text & Backgrounds",
        "description": (
            "Let's make our pages look more finished: better fonts, text alignment, and "
            "background colors."
        ),
        "key_concepts": [
            "font-family sets the typeface (with backup fonts)",
            "font-size and font-weight control text size and boldness",
            "text-align: left, center, or right",
            "background-color colors the whole box behind the content",
            "background-image can add a picture behind content (used carefully)",
        ],
        "snippets": [
            {"def": "font-family can list several fonts — the browser uses the first one it has.",
             "code": "body {\n  font-family: Arial, sans-serif;\n  font-size: 18px;\n}"},
            {"def": "font-weight controls boldness; text-align controls horizontal position.",
             "code": "h1 {\n  font-weight: bold;\n  text-align: center;\n}"},
            {"def": "background-color fills the box behind the text with a color.",
             "code": "body {\n  background-color: #f0f8ff;\n}"},
            {"def": "background-image puts a picture behind the content of a box.",
             "code": "div {\n  background-image: url(\"bg.jpg\");\n}"},
        ],
        "example": {
            "desc": "A page with a centered heading and a light background:",
            "code": (
                "<style>\n"
                "  body {\n"
                "    font-family: Arial, sans-serif;\n"
                "    background-color: #f0f8ff;\n"
                "  }\n"
                "  h1 {\n"
                "    text-align: center;\n"
                "    font-weight: bold;\n"
                "  }\n"
                "</style>"
            ),
        },
        "exercises": [
            "Change your whole page's font-family and font-size on the body.",
            "Center your <h1> using text-align.",
            "Give your page's <body> a light background-color.",
            "Review: your card <div> (Lesson 6) should still have padding/border/margin.",
            "Review: your form and table (Lessons 3–4) should still be visible on the page.",
        ],
        "homework": False,
        "checks_hw_from": "lesson05",
    },
    {
        "id": "lesson08",
        "folder": "week3/lesson08_sat_flexbox",
        "week": 3, "day": "Saturday", "order": 8,
        "topic": "Flexbox Basics — Arranging Things in a Row",
        "description": (
            "Flexbox is a simple, powerful way to line boxes up side by side (or stack "
            "them) and control the spacing between them."
        ),
        "key_concepts": [
            "display: flex turns a container into a flex layout",
            "flex-direction: row (default) or column",
            "justify-content lines items up along the main direction",
            "align-items lines items up across the other direction",
            "gap adds space between flex items",
        ],
        "snippets": [
            {"def": "display: flex makes the direct children line up automatically.",
             "code": ".container {\n  display: flex;\n}"},
            {"def": "flex-direction chooses whether items go in a row or a column.",
             "code": ".container {\n  flex-direction: row; /* or column */\n}"},
            {"def": "justify-content spaces items out: center, space-between, flex-end, etc.",
             "code": ".container {\n  justify-content: center; /* or space-between */\n}"},
            {"def": "align-items lines items up on the cross axis; gap adds even spacing between them.",
             "code": ".container {\n  align-items: center;\n  gap: 10px;\n}"},
        ],
        "example": {
            "desc": "Three cards placed in a row and centered:",
            "code": (
                "<style>\n"
                "  .container {\n"
                "    display: flex;\n"
                "    justify-content: center;\n"
                "    align-items: center;\n"
                "    gap: 15px;\n"
                "  }\n"
                "</style>\n"
                "<div class=\"container\">\n"
                "  <div class=\"card\">Card 1</div>\n"
                "  <div class=\"card\">Card 2</div>\n"
                "  <div class=\"card\">Card 3</div>\n"
                "</div>"
            ),
        },
        "exercises": [
            "Put your list items (Lesson 2) or 3 divs inside one container div.",
            "Give the container display: flex.",
            "Try justify-content: center and then space-between — which do you prefer?",
            "Add a gap between the items.",
            "Review: keep your box-model styling (padding/border) on each item (Lesson 6).",
        ],
        "homework": True,
        "checks_hw_from": None,
    },
    {
        "id": "lesson09",
        "folder": "week3/lesson09_sun_mini_project_layout",
        "week": 3, "day": "Sunday", "order": 9,
        "topic": "Mini Project: Build a Profile Card Page",
        "description": (
            "No brand-new topic today — instead we combine everything from Weeks 1–3 "
            "(HTML structure, text, lists, links, images, tables, forms, CSS styling, the "
            "box model, and flexbox) to build one complete ‘About Me’ profile card page."
        ),
        "key_concepts": [
            "Planning a page before coding it",
            "Combining HTML structure with CSS styling",
            "Using flexbox to lay out a card",
            "Reusing everything learned so far in one project",
        ],
        "snippets": [
            {"def": "A card is just a div holding an image, a heading, and a paragraph.",
             "code": "<div class=\"card\">\n  <img src=\"me.jpg\" alt=\"My photo\">\n  <h2>My Name</h2>\n  <p>A short bio about me.</p>\n</div>"},
            {"def": "Flexbox + the box model together make a neat, centered card.",
             "code": ".card {\n  display: flex;\n  flex-direction: column;\n  align-items: center;\n  padding: 20px;\n  border: 2px solid #ccc;\n  border-radius: 10px;\n  width: 250px;\n}"},
            {"def": "A list still works perfectly well inside a styled card.",
             "code": "<ul>\n  <li>Hobby 1</li>\n  <li>Hobby 2</li>\n</ul>"},
        ],
        "example": {
            "desc": "A finished profile card, combining HTML + CSS from the whole month so far:",
            "code": (
                "<div class=\"card\">\n"
                "  <img src=\"me.jpg\" alt=\"My photo\">\n"
                "  <h2>Ali</h2>\n"
                "  <p>I love football and video games.</p>\n"
                "  <ul>\n"
                "    <li>Football</li>\n"
                "    <li>Video games</li>\n"
                "    <li>Drawing</li>\n"
                "  </ul>\n"
                "  <a href=\"https://www.nasa.gov\">My favorite website</a>\n"
                "</div>"
            ),
        },
        "exercises": [
            "Build one ‘profile card’ div with your photo (or placeholder), your name as an <h2>, and a short bio paragraph.",
            "Add a bulleted list of 3 hobbies inside the card.",
            "Style the card using the box model (padding, border, width) and flexbox to arrange it.",
            "Add a link at the bottom of the card to your favorite website.",
            "Give the whole page a background-color and center the card on the page.",
        ],
        "homework": False,
        "checks_hw_from": None,
    },

    # ---------------- WEEK 4 : JAVASCRIPT BASICS ----------------
    {
        "id": "lesson10",
        "folder": "week4/lesson10_wed_js_intro",
        "week": 4, "day": "Wednesday", "order": 10,
        "topic": "Intro to JavaScript — Making Pages Interactive",
        "description": (
            "JavaScript (JS) is the language that makes webpages DO things — react to "
            "clicks, calculate numbers, change content. Today: variables, basic data "
            "types, printing messages, and linking a JS file to HTML."
        ),
        "key_concepts": [
            "JavaScript is the behavior layer of a webpage",
            "Variables store information: let and const",
            "Data types: string (text), number, boolean (true/false)",
            "console.log() prints a message so we can check our code",
            "Linking JS to HTML with <script src=\"...\"></script>",
        ],
        "snippets": [
            {"def": "let makes a variable that can change later; const makes one that can't.",
             "code": "let name = \"Ali\";\nconst age = 11;"},
            {"def": "Every value has a type: text (string), numbers, or true/false (boolean).",
             "code": "let message = \"Hello!\";  // string\nlet count = 5;            // number\nlet isFun = true;         // boolean"},
            {"def": "console.log prints a message to the browser's console so we can see what our code is doing.",
             "code": "console.log(\"Hello, world!\");\nconsole.log(age);"},
            {"def": "This links a JavaScript file to your HTML page, usually near the end of <body>.",
             "code": "<script src=\"script.js\"></script>\n<!-- put this near the end of <body> -->"},
        ],
        "example": {
            "desc": "A simple script.js that builds and logs a greeting:",
            "code": (
                "let name = \"Ali\";\n"
                "let age = 11;\n"
                "console.log(\"Hi, I'm \" + name + \" and I'm \" + age + \" years old.\");"
            ),
        },
        "exercises": [
            "Create a script.js file and link it to your HTML page.",
            "Declare a variable for your name and one for your age.",
            "Use console.log to print ‘Hi, I'm [name] and I'm [age] years old.’",
            "Open the browser console (right-click → Inspect → Console) and check your message appears.",
            "Review: your HTML page should still show your profile card from Lesson 9.",
        ],
        "homework": False,
        "checks_hw_from": "lesson08",
    },
    {
        "id": "lesson11",
        "folder": "week4/lesson11_sat_operators_conditionals_functions",
        "week": 4, "day": "Saturday", "order": 11,
        "topic": "Operators, If/Else & Simple Functions",
        "description": (
            "Now let's make JavaScript make decisions and reuse code. We'll learn math "
            "and comparison operators, if/else statements, and how to write our own "
            "simple functions."
        ),
        "key_concepts": [
            "Math operators: +, -, *, /",
            "Comparison operators: ===, >, <",
            "if / else statements make decisions",
            "Functions let us reuse a block of code",
        ],
        "snippets": [
            {"def": "Math operators work just like in math class.",
             "code": "let total = 5 + 3;\nlet result = 10 - 4;"},
            {"def": "Comparison operators check something and give back true or false.",
             "code": "console.log(5 > 3);    // true\nconsole.log(5 === 5);  // true"},
            {"def": "if runs code only when the condition is true; else runs when it's false.",
             "code": "let age = 11;\nif (age >= 10) {\n  console.log(\"You are a preteen or older!\");\n} else {\n  console.log(\"You are younger than 10.\");\n}"},
            {"def": "A function is a named, reusable block of code. We call it by its name.",
             "code": "function greet(name) {\n  console.log(\"Hello, \" + name + \"!\");\n}\ngreet(\"Ali\");"},
        ],
        "example": {
            "desc": "A function that checks if a number is even or odd:",
            "code": (
                "function checkNumber(n) {\n"
                "  if (n % 2 === 0) {\n"
                "    console.log(n + \" is even\");\n"
                "  } else {\n"
                "    console.log(n + \" is odd\");\n"
                "  }\n"
                "}\n"
                "checkNumber(4);\n"
                "checkNumber(7);"
            ),
        },
        "exercises": [
            "Write a function called greet that takes a name and logs ‘Hello, [name]!’",
            "Call your greet function with both students' names.",
            "Write an if/else that checks if a number is even or odd (hint: number % 2 === 0).",
            "Combine the two ideas into one function called isEven(number).",
            "Review: keep your console.log messages from Lesson 10 working alongside the new code.",
        ],
        "homework": True,
        "checks_hw_from": None,
    },
    {
        "id": "lesson12",
        "folder": "week4/lesson12_sun_dom_final_project",
        "week": 4, "day": "Sunday", "order": 12,
        "topic": "DOM Basics & Final Project — Bringing It All Together",
        "description": (
            "The DOM (Document Object Model) is how JavaScript ‘sees’ and changes your "
            "HTML. Today: selecting elements, changing their text/style, reacting to "
            "clicks, and building one final project using HTML + CSS + JS together."
        ),
        "key_concepts": [
            "The DOM is JavaScript's live map of the HTML page",
            "document.getElementById() / document.querySelector() select elements",
            ".textContent changes an element's text",
            ".style changes an element's CSS from JavaScript",
            "addEventListener(\"click\", ...) reacts to clicks",
        ],
        "snippets": [
            {"def": "getElementById finds one element by its id; querySelector finds one by a CSS-style selector.",
             "code": "const title = document.getElementById(\"title\");\nconst box = document.querySelector(\".card\");"},
            {"def": "Once selected, we can change what an element shows and how it looks.",
             "code": "title.textContent = \"New Title!\";\ntitle.style.color = \"red\";"},
            {"def": "addEventListener runs a function every time that event (like a click) happens.",
             "code": "const button = document.querySelector(\"button\");\nbutton.addEventListener(\"click\", function() {\n  console.log(\"Button was clicked!\");\n});"},
            {"def": "We can combine selecting and events to make a button change the page.",
             "code": "button.addEventListener(\"click\", function() {\n  title.style.color = \"blue\";\n});"},
        ],
        "example": {
            "desc": "A button that changes the profile card's heading when clicked:",
            "code": (
                "const heading = document.querySelector(\"h2\");\n"
                "const button = document.querySelector(\"button\");\n\n"
                "button.addEventListener(\"click\", function() {\n"
                "  heading.textContent = \"Thanks for clicking!\";\n"
                "  heading.style.color = \"blue\";\n"
                "});"
            ),
        },
        "exercises": [
            "Add a button to your profile card page (Lesson 9).",
            "Use document.querySelector to select the button and your <h2> name heading.",
            "Add a click event: when clicked, change the heading's text and color.",
            "Bonus: add a second button that changes the background-color of the whole page.",
            "Final Project: present your complete profile card page (HTML + CSS + JS) — structure, styling, and the interactive button.",
        ],
        "homework": False,
        "checks_hw_from": None,
    },
]
