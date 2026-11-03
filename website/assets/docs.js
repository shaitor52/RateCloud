(() => {
  "use strict";

  const body = document.body;
  const base = body.dataset.base || "/";
  const lang = body.dataset.lang || "en";
  const searchButton = document.querySelector("[data-search-open]");
  const dialog = document.getElementById("search-dialog");
  const input = document.getElementById("search-input");
  const results = document.getElementById("search-results");
  const closeButton = document.getElementById("search-close");
  let searchIndex = null;
  let searchLoad = null;
  let debounceTimer = 0;
  let lastFocus = null;

  function safeInternalUrl(value) {
    try {
      const target = new URL(value, window.location.href);
      if (target.origin !== window.location.origin) return null;
      if (!target.pathname.startsWith(base)) return null;
      return target.href;
    } catch (_) {
      return null;
    }
  }

  function loadSearchIndex() {
    if (searchIndex) return Promise.resolve(searchIndex);
    if (searchLoad) return searchLoad;
    const indexUrl = safeInternalUrl(`${base}search/${encodeURIComponent(lang)}.json`);
    if (!indexUrl) return Promise.resolve([]);
    searchLoad = fetch(indexUrl, { credentials: "same-origin", headers: { Accept: "application/json" } })
      .then((response) => {
        if (!response.ok) throw new Error("Search index unavailable");
        return response.json();
      })
      .then((items) => {
        searchIndex = Array.isArray(items) ? items.filter((item) => item && typeof item.title === "string" && typeof item.url === "string") : [];
        return searchIndex;
      })
      .catch(() => {
        searchIndex = [];
        return searchIndex;
      });
    return searchLoad;
  }

  function renderResults(items) {
    if (!results) return;
    results.replaceChildren();
    for (const item of items) {
      const href = safeInternalUrl(item.url);
      if (!href) continue;
      const li = document.createElement("li");
      const link = document.createElement("a");
      const title = document.createElement("strong");
      const excerpt = document.createElement("span");
      title.textContent = item.title;
      excerpt.textContent = item.excerpt || item.text || "";
      link.href = href;
      link.append(title, excerpt);
      li.append(link);
      results.append(li);
    }
    if (!results.childElementCount && input && input.value.trim()) {
      const li = document.createElement("li");
      const empty = document.createElement("span");
      empty.textContent = results.dataset.empty || "No matching pages found.";
      empty.style.cssText = "display:block;padding:1rem;color:var(--muted)";
      li.append(empty);
      results.append(li);
    }
  }

  function score(item, terms) {
    const title = item.title.toLocaleLowerCase();
    const excerpt = (item.excerpt || "").toLocaleLowerCase();
    const text = (item.text || "").toLocaleLowerCase();
    let points = 0;
    for (const term of terms) {
      if (title.includes(term)) points += title === term ? 12 : 7;
      if (excerpt.includes(term)) points += 3;
      if (text.includes(term)) points += 1;
    }
    return points;
  }

  async function searchNow(query) {
    if (!query.trim()) {
      renderResults([]);
      return;
    }
    const index = await loadSearchIndex();
    const terms = query.toLocaleLowerCase().split(/\s+/).filter(Boolean);
    const ranked = index
      .map((item, order) => ({ item, order, points: score(item, terms) }))
      .filter((entry) => entry.points > 0)
      .sort((a, b) => b.points - a.points || a.order - b.order)
      .slice(0, 12)
      .map((entry) => entry.item);
    renderResults(ranked);
  }

  function openSearch() {
    if (!dialog || typeof dialog.showModal !== "function") return;
    lastFocus = document.activeElement;
    if (!dialog.open) dialog.showModal();
    if (input) {
      input.value = "";
      renderResults([]);
      input.focus();
    }
  }

  function closeSearch() {
    if (dialog && dialog.open) dialog.close();
  }

  if (searchButton && dialog) searchButton.addEventListener("click", openSearch);
  if (closeButton) closeButton.addEventListener("click", closeSearch);
  if (dialog) {
    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) closeSearch();
    });
    dialog.addEventListener("close", () => {
      if (lastFocus && typeof lastFocus.focus === "function") lastFocus.focus();
      lastFocus = null;
    });
  }
  if (input) {
    input.addEventListener("input", () => {
      window.clearTimeout(debounceTimer);
      debounceTimer = window.setTimeout(() => searchNow(input.value), 120);
    });
  }
  document.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
      event.preventDefault();
      openSearch();
    }
  });

  const menuButton = document.getElementById("menu-toggle");
  const sidebar = document.getElementById("sidebar");
  const mobileNavQuery = window.matchMedia("(max-width: 700px)");
  function updateSidebarInert(open) {
    if (sidebar) sidebar.inert = mobileNavQuery.matches && !open;
  }
  function setMenuOpen(open) {
    body.classList.toggle("menu-open", open);
    updateSidebarInert(open);
    if (menuButton) menuButton.setAttribute("aria-expanded", String(open));
    if (menuButton) menuButton.setAttribute("aria-label", open ? (menuButton.dataset.closeLabel || "Close navigation") : (menuButton.dataset.openLabel || "Open navigation"));
  }
  if (menuButton) {
    menuButton.setAttribute("aria-expanded", "false");
    menuButton.addEventListener("click", () => setMenuOpen(!body.classList.contains("menu-open")));
  }
  updateSidebarInert(false);
  mobileNavQuery.addEventListener("change", () => {
    if (!mobileNavQuery.matches) setMenuOpen(false);
    else updateSidebarInert(body.classList.contains("menu-open"));
  });
  if (sidebar) {
    // Normal sidebar links navigate to a fresh page with the menu closed.
    // Do not make an activated link inert before navigation completes.
    document.addEventListener("click", (event) => {
      if (body.classList.contains("menu-open") && !sidebar.contains(event.target) && !menuButton?.contains(event.target)) setMenuOpen(false);
    });
  }
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && body.classList.contains("menu-open")) setMenuOpen(false);
  });

  const languageSwitch = document.getElementById("language-switch");
  if (languageSwitch) {
    languageSwitch.addEventListener("change", () => {
      const destination = safeInternalUrl(languageSwitch.value);
      if (destination) window.location.assign(destination);
    });
  }

  const copyLabel = body.dataset.copy || "Copy";
  const copiedLabel = body.dataset.copied || "Copied";
  document.querySelectorAll("button[data-copy], button.code-copy").forEach((button) => {
    button.textContent = copyLabel;
    button.addEventListener("click", async () => {
      let text = button.dataset.copy || "";
      const targetId = button.dataset.copyTarget;
      if (!text && targetId) text = document.getElementById(targetId)?.innerText || "";
      if (!text) text = button.closest(".code-block")?.querySelector("pre")?.innerText || button.parentElement?.querySelector("pre")?.innerText || "";
      if (!text) return;
      try {
        await navigator.clipboard.writeText(text);
        button.textContent = copiedLabel;
        window.setTimeout(() => { button.textContent = copyLabel; }, 1600);
      } catch (_) {
        button.textContent = button.dataset.errorLabel || "Copy failed";
      }
    });
  });
})();
