// Year
document.getElementById("year").textContent = new Date().getFullYear();

// Reveal on scroll
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll(".reveal").forEach((el) => revealObserver.observe(el));

// Animate skill bars when in view
const skillObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const level = el.getAttribute("data-level");
      const bar = el.querySelector(".bar");
      if (bar) bar.style.width = level + "%";
      skillObserver.unobserve(el);
    }
  });
}, { threshold: 0.4 });
document.querySelectorAll(".skill").forEach((el) => skillObserver.observe(el));

// Contact form -> POST to Django (which sends Twilio SMS)
const form = document.getElementById("contact-form");
const status = document.getElementById("form-status");
const btn = document.getElementById("submit-btn");

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
  return "";
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  btn.disabled = true;
  btn.textContent = "Sending...";
  status.className = "text-sm text-slate-400";
  status.textContent = "";
  status.classList.remove("hidden");

  const data = new FormData(form);
  try {
    const res = await fetch("/contact/", {
      method: "POST",
      body: data,
      headers: { "X-CSRFToken": getCookie("csrftoken") },
    });
    const json = await res.json();
    if (res.ok && json.ok) {
      status.className = "text-sm text-emerald-400";
      status.textContent = json.message || "Thanks! Your message has been sent.";
      form.reset();
    } else {
      status.className = "text-sm text-red-400";
      status.textContent = json.message || "Something went wrong. Please try again.";
    }
  } catch (err) {
    status.className = "text-sm text-red-400";
    status.textContent = "Network error. Please try again.";
  } finally {
    btn.disabled = false;
    btn.textContent = "Send Message";
  }
});
