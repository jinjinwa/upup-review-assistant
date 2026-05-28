const marketList = document.querySelector("#market-list");
const marketCount = document.querySelector("#market-count");
const runButton = document.querySelector("#run-review");
const reviewStatus = document.querySelector("#review-status");
const report = document.querySelector("#report");

function renderMarket(items) {
  marketCount.textContent = `${items.length} synthetic entries`;
  marketList.innerHTML = items
    .map(
      (item) => `
        <article class="demo-card">
          <div class="code">${item.demo_code}</div>
          <h3>${item.name}</h3>
          <p>${item.summary}</p>
          <div class="tags">
            ${item.labels.map((label) => `<span>${label}</span>`).join("")}
          </div>
        </article>
      `,
    )
    .join("");
}

function renderReport(data) {
  const items = data.report?.items || data.items || [];
  if (!items.length) {
    report.className = "report empty";
    report.textContent = "No demo report available yet.";
    return;
  }

  report.className = "report";
  report.innerHTML = `
    <p class="summary">${data.report?.demo_summary || data.demo_summary}</p>
    <div class="score-list">
      ${items
        .map(
          (item) => `
            <div class="score-row">
              <div>
                <strong>${item.name}</strong>
                <span>${item.demo_code} · ${item.band}</span>
              </div>
              <b>${item.toy_score}</b>
            </div>
          `,
        )
        .join("")}
    </div>
  `;
}

async function loadMarket() {
  const response = await fetch("/api/demo/market");
  const data = await response.json();
  renderMarket(data.items);
}

async function runReview() {
  runButton.disabled = true;
  reviewStatus.textContent = "Running";
  report.className = "report empty";
  report.textContent = "Mock review is running locally...";

  try {
    const response = await fetch("/api/demo/review", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ selected_codes: [] }),
    });
    const data = await response.json();
    reviewStatus.textContent = data.status;
    renderReport(data);
  } catch (error) {
    reviewStatus.textContent = "Error";
    report.className = "report empty";
    report.textContent = "The local demo review could not be completed.";
  } finally {
    runButton.disabled = false;
  }
}

runButton.addEventListener("click", runReview);
loadMarket();
