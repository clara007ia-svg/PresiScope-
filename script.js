// 🌐 Détection de langue
const lang = navigator.language || navigator.userLanguage;
const banner = document.getElementById("banner");
const subtitle = document.getElementById("subtitle");

if (lang.startsWith("fr")) {
  banner.textContent = "🧠 PrésiScope – Intelligence présidentielle adaptative";
  subtitle.textContent = "Un sanctuaire politique multilingue et neutre";
} else if (lang.startsWith("ar")) {
  banner.textContent = "🧠 بريسي سكوب – ذكاء رئاسي متكيف";
  subtitle.textContent = "ملاذ سياسي متعدد اللغات ومحايد";
} else {
  banner.textContent = "🧠 PresiScope – Adaptive Presidential Intelligence";
  subtitle.textContent = "A multilingual, neutral political sanctuary";
}

// 🔐 Mode admin
document.addEventListener("keydown", function (e) {
  if (e.key === "#" && confirm("Enter admin password:") === "@Action26") {
    alert("🔐 Admin mode activated");
    localStorage.setItem("admin", "true");
  }
});

// 🔄 Réinitialisation automatique le 1er du mois
const today = new Date();
if (today.getDate() === 1) {
  localStorage.clear();
  sessionStorage.clear();
  alert("🔄 PresiScope a été réinitialisé pour le nouveau mois.");
}

// 💳 Paiement PayPal (structure à compléter)
function launchPayPal(locale = "en_US", currency = "USD") {
  alert(`💳 Paiement PayPal simulé (${locale}, ${currency})`);
  // Ici tu peux intégrer le vrai bouton PayPal selon la région
}
