/**
 * Handles submission of all four form categories to the PHP + Resend backend.
 * Every form uses progressive enhancement: plain HTML POST works without JS,
 * this module intercepts submit to give inline success/error feedback instead.
 */
function setStatus(container: HTMLElement, kind: "loading" | "success" | "error", message: string): void {
  container.hidden = false;
  container.textContent = message;
  container.dataset.state = kind;
}

async function handleSubmit(form: HTMLFormElement, endpoint: string, statusEl: HTMLElement): Promise<void> {
  const honeypot = form.querySelector<HTMLInputElement>('input[name="hp_confirm"]');
  if (honeypot && honeypot.value.trim() !== "") {
    // Bot filled the hidden field — silently drop, pretend success to avoid tipping off scrapers.
    setStatus(statusEl, "success", "Thank you — your submission has been received.");
    form.reset();
    return;
  }

  const submitBtn = form.querySelector<HTMLButtonElement>('button[type="submit"]');
  submitBtn?.setAttribute("disabled", "true");
  setStatus(statusEl, "loading", "Submitting…");

  try {
    const formData = new FormData(form);
    const response = await fetch(endpoint, {
      method: "POST",
      headers: { Accept: "application/json" },
      body: formData
    });
    const payload = await response.json().catch(() => ({}));

    if (!response.ok || !payload.ok) {
      throw new Error(payload.message || "Something went wrong. Please try again.");
    }

    setStatus(statusEl, "success", payload.message || "Thank you — we have received your submission.");
    form.reset();
  } catch (err) {
    const message = err instanceof Error ? err.message : "Something went wrong. Please try again.";
    setStatus(statusEl, "error", message);
  } finally {
    submitBtn?.removeAttribute("disabled");
  }
}

export function initForms(): void {
  const forms = document.querySelectorAll<HTMLFormElement>("[data-api-form]");
  forms.forEach((form) => {
    const endpoint = form.getAttribute("data-api-form");
    const statusEl = form.querySelector<HTMLElement>("[data-form-status]");
    if (!endpoint || !statusEl) return;

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      void handleSubmit(form, endpoint, statusEl);
    });
  });
}
