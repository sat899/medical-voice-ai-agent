const $ = (id) => document.getElementById(id);

const API_BASE = "http://localhost:8000/api/v1";

async function runAgent() {
  const text = $("consultation").value.trim();
  $("status").textContent = "Running...";
  $("run-btn").disabled = true;

  try {
    const res = await fetch(`${API_BASE}/agent/run`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        consultation_text: text || "Sample consultation about chest pain.",
        run_stt: true,
        run_clarifications: true,
        run_actions: true,
      }),
    });

    if (!res.ok) {
      throw new Error(`HTTP ${res.status}`);
    }

    const data = await res.json();

    $("stt").textContent = JSON.stringify(data.stt, null, 2);
    $("clarifications").textContent = JSON.stringify(
      data.clarifications,
      null,
      2
    );
    $("actions").textContent = JSON.stringify(data.actions, null, 2);
    $("status").textContent = "Done.";
  } catch (err) {
    console.error(err);
    $("status").textContent = "Error – check console.";
  } finally {
    $("run-btn").disabled = false;
  }
}

window.addEventListener("DOMContentLoaded", () => {
  $("run-btn").addEventListener("click", runAgent);
});

