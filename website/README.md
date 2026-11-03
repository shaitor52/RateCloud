# Building the documentation website

The source articles remain in the repository's language directories. `website/build.py` generates the static `docs/` tree published by GitHub Pages. The default address is https://shaitor52.github.io/RateCloud/.

## Rebuild after editing articles or UI assets

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-docs.txt
.venv/bin/python website/build.py
.venv/bin/python website/check.py
node --check website/assets/docs.js
```

Commit the source changes together with the regenerated `docs/` files. GitHub Pages publishes `main` with `/docs` as its source and `.nojekyll` disables a second content build. No custom runner, paid backend, API key, or analytics integration is required. Publication still uses GitHub's Pages deployment service.

All primary content is present in HTML without JavaScript. JavaScript adds language-scoped local search, code copying, and the mobile menu. Search indexes contain only public articles. Alternate-language links preserve the current article or guide. Canonical URLs, reciprocal `hreflang`, structured metadata, a sitemap, and raw Markdown exports are generated together.

`docs/robots.txt` is a project-path reference. Crawlers consult the host-root robots.txt, which this project cannot control. The generated sitemap and explicit page links are the discovery mechanisms under this project's control. Indexing and AI citations are not guaranteed.

The branded logo and hero artwork come from the owner's public website. `connection-preview.jpg` is a screenshot of the public English connection guide, captured November 3, 2026. It contains no account, credential, or private customer data. Contextual figures link to the official guide. No claim of a live-tested integration is added by the screenshot.

Keep prices in the Russian edition in its original currency; non-Russian editions use USD. Preserve dated pricing and performance caveats. Do not use Unicode U+2014 or U+2013 in content or interface labels.

If a source page is removed or renamed, remove its old generated output as part of the same reviewed change. The builder overwrites generated pages and does not delete unrelated files automatically.
