# Test1
Test of the revision control
# Standard Normal Area Explorer

Interactive web app for teaching normal-model area questions with sliders and live graph shading.

## What it does

- Computes and visualizes standard normal areas for:
  - `z > a`
  - `z < a`
  - `a < z < b`
  - `|z| > a`
- Uses slider bars so students can quickly test new values.
- Includes one-click classroom examples matching common textbook prompts.

## Run locally

Open `index.html` directly in a browser, or serve the folder with a small static server:

```bash
python3 -m http.server 8000
```

Then go to `http://localhost:8000`.

## Deploy to GitHub Pages

1. Create a GitHub repo and push this project.
2. In GitHub, open **Settings → Pages**.
3. Under **Build and deployment**, choose:
   - **Source**: `Deploy from a branch`
   - **Branch**: `main` (or your default branch), `/root`
4. Save and wait for the Pages URL to appear.

Your app will be live at a URL like:

`https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`