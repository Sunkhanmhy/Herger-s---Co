import { initNav } from "./nav";
import { initAccordions, initTabs } from "./accordion";
import { initFeeCalculator } from "./calculator";
import { initForms } from "./forms";
import { initCalendly } from "./calendly";

document.addEventListener("DOMContentLoaded", () => {
  initNav();
  initAccordions();
  initTabs();
  initFeeCalculator();
  initForms();
  initCalendly();
});
