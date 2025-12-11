# 🧭 UX – PresiScope

PresiScope is designed as a multilingual, sovereign sanctuary. Its user experience is festive, adaptive, and respectful of political neutrality.

---

## 🎯 Entry Points

- **index.html** – public homepage with multilingual banner, APK button, and iframe to Streamlit
- **app.py** – adaptive AI interface (Streamlit)
- **#admin** – triggers admin mode (password: `@Action26`)
- **APK** – installable Android version
- **PWA** – installable web app with offline support

---

## 🧠 User Roles

| Role | Access |
|------|--------|
| Visitor | Multilingual interface, public analysis |
| Admin (`#admin`) | Access to premium tools, reset, and PayPal logic |
| Contributor | Can fork, translate, or extend the sanctuary |

---

## 🌐 Language Flow

- Auto-detects browser language (fr, en, ar)
- Fallback: English
- Language can be switched manually via dropdown or flags

---

## 🔄 Monthly Reset

- On the 1st of each month:
  - `st.session_state.clear()` and `st.cache_data.clear()` in Streamlit
  - `localStorage.clear()` and `sessionStorage.clear()` in browser
  - Optional banner: “🌕 New political cycle. PresiScope has been reset.”

---

## 🧩 Modules

- **Multilingual UI** – HTML + JS + CSS
- **Adaptive AI** – Streamlit
- **Admin Mode** – JS + Streamlit
- **PayPal Checkout** – JS (localized)
- **PWA** – manifest + service worker
- **APK** – linked in homepage

---

PresiScope is not a dashboard. It is a ritual of observation.
