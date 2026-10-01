/** Lazily loads the Calendly inline-widget script only on pages that embed it. */
export function initCalendly(): void {
  const container = document.querySelector<HTMLElement>("[data-calendly-inline-widget]");
  if (!container) return;

  const existing = document.querySelector('script[src*="calendly.com/assets/external/widget.js"]');
  if (!existing) {
    const script = document.createElement("script");
    script.src = "https://assets.calendly.com/assets/external/widget.js";
    script.async = true;
    document.body.appendChild(script);
  }
}
