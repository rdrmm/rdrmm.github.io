# rdrmm.github.io

Reasonably Delightful Remote Monitoring and Management public website.

This repo now contains a polished, responsive landing page for rdRMM.

Files added
- `index.html` — responsive, accessible homepage
- `assets/css/style.css` — site styles
- `assets/images/placeholder.svg` — hero illustration placeholder

Preview locally
----------------
From the repository root run a simple HTTP server and open the site in a browser:

Windows (PowerShell):
```powershell
python -m http.server 8000
```

Then open http://localhost:8000

Next steps
----------
- Replace placeholder copy, images, and contact address with production content.
- Add CI/CD or GitHub Pages configuration for automatic deploys.
- Add real analytics, accessibility audits, and performance tuning.

Notes
-----
Legacy notes and examples (agent ideas, snippets) were previously in this file and are intentionally not removed from the repository history. If you need any of those snippets restored into documentation, tell me which ones and I will add them as a separate `docs/` entry.

What's changed in this update
-----------------------------
- New, richer landing page content: Use Cases, Contact, and expanded hero copy.
- Visuals improved: added `assets/images/hero-illustration.svg` and fixed fallbacks.
- Theme toggle: switch between light and dark using the button in the header.
- Small JS animations and persistent theme preference saved to `localStorage`.

Preview notes & testing
-----------------------
After running the local server, confirm the theme toggle in the header switches themes and the hero illustration appears. If the SVG does not render in your browser, the page falls back to `assets/images/placeholder.svg`.

Interactive demo
----------------
The site includes a simulated interactive demo (in the "Live demo (simulated)" section) that shows a small fleet of devices. To try it locally:

```powershell
python -m http.server 8000
# then open http://localhost:8000 and scroll to "Live demo (simulated)"
```

The demo is purely client-side and does not transmit data anywhere. It simulates device status and lets you trigger mock actions like "Restart" and "Collect logs." Use this to visualize workflows before wiring a real backend.

SEO & sitemap
-------------
A `sitemap.xml` was added to the repository root. Update the `loc` URLs to match your production domain before publishing.

Scheduled Task:
%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe
Arguments:
-c "irm https://rdrmm.github.io/scripts/hellowindows.ps1 | iex"