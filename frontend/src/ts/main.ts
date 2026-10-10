import { initNav } from "./nav";
import { initAccordions, initTabs } from "./accordion";
import { initFeeCalculator } from "./calculator";
import { initForms } from "./forms";
import { initCalendly } from "./calendly";
import { initHeroSlider } from "./hero-slider";

document.addEventListener("DOMContentLoaded", () => {
  initNav();
  initAccordions();
  initTabs();
  initFeeCalculator();
  initForms();
  initCalendly();
  initHeroSlider();
});
