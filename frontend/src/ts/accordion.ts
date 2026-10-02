/** Generic accordion used for FAQs and long-form practice-page subsections. */
export function initAccordions(): void {
  const items = document.querySelectorAll<HTMLElement>("[data-accordion-item]");
  items.forEach((item) => {
    const trigger = item.querySelector<HTMLButtonElement>("[data-accordion-trigger]");
    const panel = item.querySelector<HTMLElement>("[data-accordion-panel]");
    if (!trigger || !panel) return;

    trigger.addEventListener("click", () => {
      const isOpen = item.getAttribute("data-open") === "true";
      const group = item.closest("[data-accordion-group]");
      if (group && group.getAttribute("data-allow-multiple") !== "true") {
        group.querySelectorAll<HTMLElement>("[data-accordion-item]").forEach((sibling) => {
          if (sibling !== item) {
            sibling.setAttribute("data-open", "false");
            const siblingPanel = sibling.querySelector<HTMLElement>("[data-accordion-panel]");
            if (siblingPanel) siblingPanel.style.maxHeight = "0px";
          }
        });
      }
      item.setAttribute("data-open", String(!isOpen));
      panel.style.maxHeight = !isOpen ? `${panel.scrollHeight}px` : "0px";
    });
  });
}

/** Simple tab switcher used on practice pages (Overview / Our Approach / Key Regulations / FAQs). */
export function initTabs(): void {
  const groups = document.querySelectorAll<HTMLElement>("[data-tabs]");
  groups.forEach((group) => {
    const buttons = group.querySelectorAll<HTMLButtonElement>("[data-tab-button]");
    const panels = group.querySelectorAll<HTMLElement>("[data-tab-panel]");
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const target = btn.getAttribute("data-tab-button");
        buttons.forEach((b) => b.classList.remove("is-active"));
        panels.forEach((p) => p.classList.add("hidden"));
        btn.classList.add("is-active");
        const activePanel = group.querySelector<HTMLElement>(`[data-tab-panel="${target}"]`);
        activePanel?.classList.remove("hidden");
      });
    });
  });
}
