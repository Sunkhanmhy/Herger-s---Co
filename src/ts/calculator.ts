/**
 * Paid Consultation hourly-rate calculator.
 * Purely a client-side estimate — final billing always confirmed by the firm in writing.
 */
interface SessionType {
  key: string;
  label: string;
  hourlyRateNgn: number;
}

const SESSION_TYPES: SessionType[] = [
  { key: "corporate-advisory", label: "Corporate & Commercial Advisory", hourlyRateNgn: 75000 },
  { key: "mining-energy", label: "Mining, Energy & Production Law", hourlyRateNgn: 95000 },
  { key: "tax-policy", label: "Taxation & Fiscal Policy", hourlyRateNgn: 85000 },
  { key: "shipping-trade", label: "Shipping & International Trade", hourlyRateNgn: 90000 },
  { key: "compliance", label: "Risk & Regulatory Compliance", hourlyRateNgn: 80000 },
  { key: "white-collar", label: "White Collar Defence", hourlyRateNgn: 110000 },
  { key: "real-estate", label: "Real Estate & Property Management", hourlyRateNgn: 65000 },
  { key: "capital-markets", label: "Capital Markets & Securities", hourlyRateNgn: 100000 },
  { key: "private-equity", label: "Privatization & Venture Capital", hourlyRateNgn: 95000 },
  { key: "m-and-a", label: "Mergers & Acquisitions", hourlyRateNgn: 120000 },
  { key: "media-entertainment", label: "Media & Entertainment Law", hourlyRateNgn: 70000 },
  { key: "litigation-adr", label: "Litigation & Alternative Dispute Resolution", hourlyRateNgn: 85000 },
  { key: "corporate-governance", label: "Corporate Governance", hourlyRateNgn: 90000 }
];

const URGENCY_MULTIPLIERS: Record<string, number> = {
  standard: 1,
  priority: 1.25,
  same_day: 1.6
};

function formatNgn(value: number): string {
  return new Intl.NumberFormat("en-NG", {
    style: "currency",
    currency: "NGN",
    maximumFractionDigits: 0
  }).format(value);
}

export function initFeeCalculator(): void {
  const form = document.querySelector<HTMLFormElement>("[data-fee-calculator]");
  if (!form) return;

  const sessionSelect = form.querySelector<HTMLSelectElement>("[data-session-type]");
  const hoursInput = form.querySelector<HTMLInputElement>("[data-hours]");
  const urgencySelect = form.querySelector<HTMLSelectElement>("[data-urgency]");
  const output = form.querySelector<HTMLElement>("[data-fee-output]");
  const rateOutput = form.querySelector<HTMLElement>("[data-rate-output]");
  const hiddenSummary = form.querySelector<HTMLInputElement>("[data-fee-summary-field]");
  if (!sessionSelect || !hoursInput || !urgencySelect || !output) return;

  sessionSelect.innerHTML = SESSION_TYPES.map(
    (s) => `<option value="${s.label}" data-key="${s.key}">${s.label}</option>`
  ).join("");

  function recalculate(): void {
    const selected = SESSION_TYPES.find((s) => s.label === sessionSelect!.value) ?? SESSION_TYPES[0];
    const hours = Math.max(0.5, Number(hoursInput!.value) || 1);
    const multiplier = URGENCY_MULTIPLIERS[urgencySelect!.value] ?? 1;
    const total = selected.hourlyRateNgn * hours * multiplier;

    if (rateOutput) rateOutput.textContent = formatNgn(selected.hourlyRateNgn);
    output!.textContent = formatNgn(total);
    if (hiddenSummary) {
      hiddenSummary.value = `${selected.label} | ${hours}h | ${urgencySelect!.value} | Estimated: ${formatNgn(total)}`;
    }
  }

  sessionSelect.addEventListener("change", recalculate);
  hoursInput.addEventListener("input", recalculate);
  urgencySelect.addEventListener("change", recalculate);
  recalculate();
}
