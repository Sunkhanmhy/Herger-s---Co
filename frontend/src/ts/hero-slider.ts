export function initHeroSlider(): void {
  const sliders = document.querySelectorAll<HTMLElement>("[data-hero-slider]");

  sliders.forEach((slider) => {
    const track = slider.querySelector<HTMLElement>("[data-hero-slider-track]");
    const dotsHost = slider.querySelector<HTMLElement>("[data-hero-slider-dots]");
    if (!track) return;

    const slides = Array.from(track.children) as HTMLElement[];
    if (slides.length <= 1) return;

    let index = 0;
    let timer: number | undefined;
    const dots: HTMLButtonElement[] = [];

    const render = () => {
      track.style.transform = `translateX(-${index * 100}%)`;
      dots.forEach((dot, i) => dot.setAttribute("aria-current", i === index ? "true" : "false"));
    };

    const goTo = (next: number) => {
      index = (next + slides.length) % slides.length;
      render();
    };

    const start = () => {
      timer = window.setInterval(() => goTo(index + 1), 5000);
    };
    const stop = () => {
      if (timer !== undefined) window.clearInterval(timer);
    };

    if (dotsHost) {
      slides.forEach((_, i) => {
        const dot = document.createElement("button");
        dot.type = "button";
        dot.className = "img-slider-dot";
        dot.setAttribute("aria-label", `Show slide ${i + 1}`);
        dot.addEventListener("click", () => {
          goTo(i);
          stop();
          start();
        });
        dotsHost.appendChild(dot);
        dots.push(dot);
      });
    }

    slider.addEventListener("mouseenter", stop);
    slider.addEventListener("mouseleave", start);

    render();
    start();
  });
}
