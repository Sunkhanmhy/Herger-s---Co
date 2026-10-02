/**
 * Mobile navigation + accordion-style mega menu for the primary header.
 * The desktop mega menu is pure CSS (:hover via group classes); this only
 * handles the collapsed mobile drawer where menus must be tap-toggled.
 */
export function initNav(): void {
  const toggle = document.querySelector<HTMLButtonElement>("[data-nav-toggle]");
  const drawer = document.querySelector<HTMLElement>("[data-nav-drawer]");
  if (!toggle || !drawer) return;

  toggle.addEventListener("click", () => {
    const isOpen = drawer.getAttribute("data-open") === "true";
    drawer.setAttribute("data-open", String(!isOpen));
    toggle.setAttribute("aria-expanded", String(!isOpen));
    document.body.classList.toggle("overflow-hidden", !isOpen);
  });

  const subToggles = drawer.querySelectorAll<HTMLButtonElement>("[data-submenu-toggle]");
  subToggles.forEach((btn) => {
    btn.addEventListener("click", () => {
      const panel = btn.nextElementSibling as HTMLElement | null;
      if (!panel) return;
      const isOpen = panel.getAttribute("data-open") === "true";
      panel.setAttribute("data-open", String(!isOpen));
      btn.setAttribute("aria-expanded", String(!isOpen));
      btn.querySelector("[data-chevron]")?.classList.toggle("rotate-180", !isOpen);
    });
  });

  // Solid header gains a stronger shadow once the page scrolls, staying solid (never glass).
  const header = document.querySelector<HTMLElement>("[data-site-header]");
  if (header) {
    window.addEventListener(
      "scroll",
      () => {
        header.classList.toggle("shadow-lg", window.scrollY > 8);
      },
      { passive: true }
    );
  }
}
