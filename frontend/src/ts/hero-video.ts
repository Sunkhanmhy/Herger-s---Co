/**
 * Lazy-loads the hero banner's background video: the real `src` is only assigned
 * (from `data-src`) once the element is about to enter the viewport, via IntersectionObserver.
 */
export function initHeroVideo(): void {
  const videos = document.querySelectorAll<HTMLVideoElement>("[data-hero-video]");
  if (!videos.length) return;

  const load = (video: HTMLVideoElement) => {
    const src = video.dataset.src;
    if (!src || video.src) return;
    video.src = src;
    video.load();
    void video.play().catch(() => {
      // Autoplay can be blocked by the browser until user interaction; safe to ignore.
    });
  };

  if (!("IntersectionObserver" in window)) {
    videos.forEach(load);
    return;
  }

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        load(entry.target as HTMLVideoElement);
        obs.unobserve(entry.target);
      });
    },
    { rootMargin: "200px" }
  );

  videos.forEach((video) => observer.observe(video));
}
