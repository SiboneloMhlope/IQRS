/* =========================================================
   UNIZULU COURSE FINDER — front-end logic
   NOTE: This is a static front-end demo only. Real programme
   data, marks storage and chatbot intelligence will be
   provided by the Django backend + database in the full
   group project. Canned replies below are placeholders.
   ========================================================= */

/* ---------------- 1. LANGUAGE (EN / isiZulu) ---------------- */
const i18n = {
  en: {
    appTitle: "UNIZULU Course Finder",
    appSubtitle: "University of Zululand · Umeluleki Wezifundo",
    tabChat: "Chat", tabMarks: "My Marks", tabFeedback: "Feedback",
    greetTitle: "Sawubona! 👋 Welcome to the UNIZULU Course Finder",
    greetBody: "I'm here to help you explore study options at the <strong>University of Zululand</strong> across all 4 faculties:",
    facArts: "Faculty of Arts", facCommerce: "Faculty of Commerce, Administration & Law",
    facEdu: "Faculty of Education", facSci: "Faculty of Science, Agriculture & Engineering",
    howHelp: "How I can help you:",
    help1: "Answer questions about programmes and entry requirements",
    help2: "Recommend programmes based on your high school marks",
    help3: "Respond in both English and isiZulu",
    hint: "💡 Start by uploading your marks in the \"My Marks\" tab, then ask me to recommend programmes.",
    q1: "What programmes can I study at UNIZULU? ›", q2: "What are the APS requirements for Law? ›",
    q3: "Yiziphi izifundo engingafunda zona? ›", q4: "Recommend programmes based on my marks ›",
    chatPlaceholder: "Ask about UNIZULU programmes...",
    marksTitle: "Upload Your Marks",
    marksDesc: "Enter your NSC (matric) subject levels so the chatbot can recommend programmes you qualify for at UNIZULU.",
    savedFor: "Marks saved for",
    fullName: "Full Name *", email: "Email",
    subjectLevels: "Subject Levels (NSC)",
    subjectDesc: "Select achievement levels (1–7) for the subjects you took. Only fill in subjects relevant to you.",
    saveMarks: "💾 Save My Marks",
    fbTitle: "Share Your Feedback",
    fbDesc: "Help us improve the UNIZULU Course Finder. Report issues, suggest features, or let us know if any information is incorrect.",
    fbType: "Feedback Type", fbBug: "Bug Report", fbSuggestion: "Suggestion",
    fbIncorrect: "Incorrect Info", fbGeneral: "General", fbRating: "Rating *",
    fbMessage: "Your Message *", fbPlaceholder: "Tell us what you think or what we can improve...",
    fbSubmit: "📨 Submit Feedback",
    fbThanks: "✅ Thank you! Your feedback has been recorded.",
    footer: "4CPS212 Group Project · University of Zululand — A Node for African Thought",
    fillRequired: "Please add a rating and a message before submitting.",
    botFallback: "Thanks for your question! In the full version, this will be answered from the UNIZULU programme database. Try one of the suggestions below, or ask about a faculty, APS score or subject.",
  },
  zu: {
    appTitle: "UNIZULU Course Finder",
    appSubtitle: "I-University of Zululand · Umeluleki Wezifundo",
    tabChat: "Ingxoxo", tabMarks: "Amamaki Ami", tabFeedback: "Impendulo",
    greetTitle: "Sawubona! 👋 Wamukelekile ku-UNIZULU Course Finder",
    greetBody: "Ngilapha ukukusiza uhlole izinketho zokufunda e-<strong>University of Zululand</strong> kuzo zonke izikhungo ezi-4:",
    facArts: "Isikhungo Sobuciko", facCommerce: "Isikhungo Sezohwebo, Ezokuphatha Nezomthetho",
    facEdu: "Isikhungo Sezemfundo", facSci: "Isikhungo Sesayensi, Ezolimo Nobunjiniyela",
    howHelp: "Indlela engikusiza ngayo:",
    help1: "Ukuphendula imibuzo mayelana nezifundo nezimfuneko zokungena",
    help2: "Ukuncoma izifundo ngokusekelwe emamakini akho ebanga lokugcina",
    help3: "Ukuphendula ngesiNgisi nangesiZulu",
    hint: "💡 Qala ngokulayisha amamaki akho ku-\"Amamaki Ami\", bese ungicela ukuncoma izifundo.",
    q1: "Yiziphi izifundo enginganfunda zona e-UNIZULU? ›", q2: "Ziyini izidingo ze-APS zoMthetho? ›",
    q3: "Yiziphi izifundo engingafunda zona? ›", q4: "Ngincome izifundo ngokusekelwe emamakini ami ›",
    chatPlaceholder: "Buza nge-UNIZULU...",
    marksTitle: "Layisha Amamaki Akho",
    marksDesc: "Faka amazinga ezifundo zakho ze-NSC ukuze i-chatbot ikwazi ukuncoma izifundo ozifanelekelayo e-UNIZULU.",
    savedFor: "Amamaki alondoloziwe ka",
    fullName: "Igama Eliphelele *", email: "I-imeyili",
    subjectLevels: "Amazinga Ezifundo (NSC)",
    subjectDesc: "Khetha amazinga okuphumelela (1–7) ezifundo ozithathile. Gcwalisa kuphela izifundo ezikufanele.",
    saveMarks: "💾 Londoloza Amamaki Ami",
    fbTitle: "Yabelana Ngempendulo Yakho",
    fbDesc: "Sisize sithuthukise i-UNIZULU Course Finder. Bika izinkinga, phakamisa izici, noma usazise uma kunolwazi olungalungile.",
    fbType: "Uhlobo Lwempendulo", fbBug: "Inkinga Yohlelo", fbSuggestion: "Isiphakamiso",
    fbIncorrect: "Ulwazi Olungalungile", fbGeneral: "Jikelele", fbRating: "Isilinganiso *",
    fbMessage: "Umlayezo Wakho *", fbPlaceholder: "Sitshele umbono wakho noma esingakuthuthukisa...",
    fbSubmit: "📨 Thumela Impendulo",
    fbThanks: "✅ Siyabonga! Impendulo yakho iqoshiwe.",
    footer: "4CPS212 Iphrojekthi Yeqembu · University of Zululand — A Node for African Thought",
    fillRequired: "Sicela wengeze isilinganiso nomlayezo ngaphambi kokuthumela.",
    botFallback: "Siyabonga ngombuzo wakho! Kunguqu ephelele, lokhu kuzophendulwa kusuka kusizindalwazi se-UNIZULU. Zama esinye seziphakamiso, noma ubuze ngesikhungo, i-APS noma isifundo.",
  }
};
let currentLang = "en";

function applyLanguage(lang){
  currentLang = lang;
  document.getElementById("langEn").classList.toggle("active", lang === "en");
  document.getElementById("langZu").classList.toggle("active", lang === "zu");
  document.querySelectorAll("[data-i18n]").forEach(el=>{
    const key = el.getAttribute("data-i18n");
    if(i18n[lang][key] !== undefined) el.innerHTML = i18n[lang][key];
  });
  document.querySelectorAll("[data-i18n-ph]").forEach(el=>{
    const key = el.getAttribute("data-i18n-ph");
    if(i18n[lang][key] !== undefined) el.setAttribute("placeholder", i18n[lang][key]);
  });
}
document.getElementById("langEn").addEventListener("click", ()=>applyLanguage("en"));
document.getElementById("langZu").addEventListener("click", ()=>applyLanguage("zu"));

/* ---------------- 2. TABS ---------------- */
document.querySelectorAll(".tab-btn").forEach(btn=>{
  btn.addEventListener("click", ()=>{
    document.querySelectorAll(".tab-btn").forEach(b=>{b.classList.remove("active"); b.setAttribute("aria-selected","false");});
    document.querySelectorAll(".panel").forEach(p=>p.classList.remove("active"));
    btn.classList.add("active");
    btn.setAttribute("aria-selected","true");
    document.getElementById("panel-" + btn.dataset.tab).classList.add("active");
  });
});

/* ---------------- 3. SUBJECTS + APS CALCULATOR ---------------- */
const SUBJECTS = [
  "English Home Language","IsiZulu Home Language","Mathematics","Mathematical Literacy",
  "Physical Sciences","Life Sciences","Geography","History",
  "Accounting","Business Studies","Economics","Consumer Studies",
  "Tourism","Dramatic Arts","Information Technology","Agricultural Sciences","Life Orientation"
];
const LEVELS = [
  {v:"",  label:"—"},
  {v:"1", label:"1 (0-29%)"},
  {v:"2", label:"2 (30-39%)"},
  {v:"3", label:"3 (40-49%)"},
  {v:"4", label:"4 (50-59%)"},
  {v:"5", label:"5 (60-69%)"},
  {v:"6", label:"6 (70-79%)"},
  {v:"7", label:"7 (80-100%)"},
];

const subjectGrid = document.getElementById("subjectGrid");
SUBJECTS.forEach((subj, i)=>{
  const wrap = document.createElement("label");
  wrap.className = "field subject-field";
  const short = subj.length > 14 ? subj.slice(0,12) + "…" : subj;
  wrap.title = subj;
  wrap.innerHTML = `<span>${short}</span>`;
  const select = document.createElement("select");
  select.id = "subj-" + i;
  select.dataset.subject = subj;
  LEVELS.forEach(l=>{
    const opt = document.createElement("option");
    opt.value = l.v; opt.textContent = l.label;
    select.appendChild(opt);
  });
  wrap.appendChild(select);
  subjectGrid.appendChild(wrap);
  select.addEventListener("change", updateAPS);
});

function updateAPS(){
  const selects = subjectGrid.querySelectorAll("select");
  let total = 0, count = 0;
  selects.forEach(s=>{
    if(s.value){ total += parseInt(s.value,10); count++; }
  });
  document.getElementById("apsScore").textContent = total;
  document.getElementById("apsCount").textContent = `(${count} subject${count===1?"":"s"})`;
  return {total, count};
}

/* ---------------- 4. SAVE / LOAD MARKS (localStorage demo) ---------------- */
const marksForm = document.getElementById("marksForm");
marksForm.addEventListener("submit", e=>{
  e.preventDefault();
  const name = document.getElementById("fullName").value.trim();
  const email = document.getElementById("email").value.trim();
  const {total, count} = updateAPS();
  if(!name){ document.getElementById("fullName").focus(); return; }

  const subjects = {};
  subjectGrid.querySelectorAll("select").forEach(s=>{
    if(s.value) subjects[s.dataset.subject] = s.value;
  });

  const data = {name, email, aps: total, subjectCount: count, subjects};
  localStorage.setItem("unizulu_marks", JSON.stringify(data));

  document.getElementById("savedName").textContent = name;
  document.getElementById("savedAps").textContent = total;
  document.getElementById("savedBanner").hidden = false;
});

function loadSavedMarks(){
  const raw = localStorage.getItem("unizulu_marks");
  if(!raw) return;
  try{
    const data = JSON.parse(raw);
    document.getElementById("fullName").value = data.name || "";
    document.getElementById("email").value = data.email || "";
    subjectGrid.querySelectorAll("select").forEach(s=>{
      if(data.subjects && data.subjects[s.dataset.subject]) s.value = data.subjects[s.dataset.subject];
    });
    updateAPS();
    if(data.name){
      document.getElementById("savedName").textContent = data.name;
      document.getElementById("savedAps").textContent = data.aps;
      document.getElementById("savedBanner").hidden = false;
    }
  }catch(err){ /* ignore corrupt storage */ }
}
loadSavedMarks();

/* ---------------- 5. CHATBOT (placeholder rule-based demo) ---------------- */
const chatWindow = document.getElementById("chatWindow");
const chatForm = document.getElementById("chatForm");
const chatInput = document.getElementById("chatInput");

function addMessage(text, sender){
  const row = document.createElement("div");
  row.className = "msg " + sender;
  if(sender === "bot"){
    row.innerHTML = `<img class="avatar" src="assets/unizulu-logo.png" alt=""><div class="bubble">${text}</div>`;
  } else {
    row.innerHTML = `<div class="bubble">${text}</div>`;
  }
  chatWindow.appendChild(row);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function botReply(userText){
  const t = userText.toLowerCase();
  const saved = JSON.parse(localStorage.getItem("unizulu_marks") || "null");

  if(t.includes("programme") || t.includes("course") || t.includes("study") && !t.includes("aps")){
    return "UNIZULU offers programmes across <strong>Arts</strong>, <strong>Commerce, Administration &amp; Law</strong>, <strong>Education</strong>, and <strong>Science, Agriculture &amp; Engineering</strong>. Which faculty would you like to know more about?";
  }
  if(t.includes("law")){
    return "The <strong>Bachelor of Laws (LLB)</strong> typically requires an APS of around <strong>30+</strong>, including a level 4 in English and Mathematics/Maths Literacy. (Full requirements come from the UNIZULU database in the live version.)";
  }
  if(t.includes("recommend")){
    if(saved && saved.aps){
      return `Based on your saved marks (APS <strong>${saved.aps}</strong>), you could be a good fit for programmes in Commerce, Education or Science depending on your subject choices. Head to the official UNIZULU prospectus for exact cut-offs — full matching will be powered by the Django backend.`;
    }
    return "I don't see any saved marks yet. Please go to the <strong>My Marks</strong> tab and save your subject levels first, then ask me again!";
  }
  if(t.includes("aps")){
    return "APS (Admission Point Score) is the sum of your NSC achievement levels. Enter your subjects in the <strong>My Marks</strong> tab and I'll calculate it for you automatically.";
  }
  if(t.includes("isizulu") || t.includes("zulu") || /[a-zA-Z]* nga| yini | ziphi/.test(t)){
    return "Ngingakusiza ngezifundo, izimfuneko zokungena, kanye nokuncoma izifundo ngokusekelwe emamakini akho. Vula i-thebhu ethi \"Amamaki Ami\" ukuze siqale!";
  }
  return i18n[currentLang].botFallback;
}

chatForm.addEventListener("submit", e=>{
  e.preventDefault();
  const text = chatInput.value.trim();
  if(!text) return;
  addMessage(text, "user");
  chatInput.value = "";
  setTimeout(()=> addMessage(botReply(text), "bot"), 350);
});

document.getElementById("quickReplies").addEventListener("click", e=>{
  const chip = e.target.closest(".chip");
  if(!chip) return;
  const label = chip.textContent.replace(" ›","").trim();
  addMessage(label, "user");
  setTimeout(()=> addMessage(botReply(chip.dataset.q), "bot"), 350);
});

/* ---------------- 6. FEEDBACK ---------------- */
let selectedType = "general";
let selectedRating = 0;

document.getElementById("feedbackType").addEventListener("click", e=>{
  const pill = e.target.closest(".pill");
  if(!pill) return;
  document.querySelectorAll("#feedbackType .pill").forEach(p=>p.classList.remove("active"));
  pill.classList.add("active");
  selectedType = pill.dataset.type;
});

const starEls = document.querySelectorAll("#starRating .star");
starEls.forEach(star=>{
  star.addEventListener("click", ()=>{
    selectedRating = parseInt(star.dataset.val,10);
    starEls.forEach(s=>{
      s.classList.toggle("filled", parseInt(s.dataset.val,10) <= selectedRating);
      s.textContent = parseInt(s.dataset.val,10) <= selectedRating ? "★" : "☆";
    });
  });
});

document.getElementById("submitFeedback").addEventListener("click", ()=>{
  const message = document.getElementById("fbMessage").value.trim();
  const toast = document.getElementById("fbToast");
  if(!message || selectedRating === 0){
    toast.hidden = false;
    toast.style.background = "#FDECEC";
    toast.style.borderColor = "#F3B4B4";
    toast.style.color = "#9A2E2E";
    toast.textContent = i18n[currentLang].fillRequired;
    return;
  }
  const entries = JSON.parse(localStorage.getItem("unizulu_feedback") || "[]");
  entries.push({type: selectedType, rating: selectedRating, message, date: new Date().toISOString()});
  localStorage.setItem("unizulu_feedback", JSON.stringify(entries));

  toast.hidden = false;
  toast.style.background = "#E9F9EE";
  toast.style.borderColor = "#8FDDB0";
  toast.style.color = "#1E7A44";
  toast.textContent = i18n[currentLang].fbThanks;

  document.getElementById("fbMessage").value = "";
  selectedRating = 0;
  starEls.forEach(s=>{s.classList.remove("filled"); s.textContent = "☆";});
});
