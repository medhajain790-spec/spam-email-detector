const API_URL = "http://127.0.0.1:5001/predict";


const emailInput = document.getElementById("emailInput");
const checkBtn = document.getElementById("checkBtn");
const resultBox = document.getElementById("result");
const predictionText = document.getElementById("prediction");
const confidenceText = document.getElementById("confidence");
const noteText = document.getElementById("note");


function showResult(type, prediction, confidence, note) {

    resultBox.className = "result " + type;

    predictionText.textContent = prediction;
    confidenceText.textContent = confidence;
    noteText.textContent = note;
}


async function checkEmail() {

    const email = emailInput.value.trim();

    if (email === "") {
        showResult("error", "⚠️ Please paste an email first.", "", "");
        return;
    }

    checkBtn.disabled = true;
    checkBtn.textContent = "Checking...";

    try {

        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email: email }),
        });

        const data = await response.json();

        if (!response.ok) {
            showResult("error", "⚠️ " + data.error, "", "");
            return;
        }

        const note = "This is the model's estimate, not a guarantee.";
        const confidence = "Spam probability: " + data.spam_probability + "%";

        if (data.label === "SPAM") {
            showResult("spam", "Prediction: 🚨 SPAM", confidence, note);
        } else {
            showResult("ham", "Prediction: ✅ NOT SPAM", confidence, note);
        }

    } catch (error) {

        showResult(
            "error",
            "⚠️ Could not reach the server.",
            "Is the Flask backend running?",
            ""
        );

    } finally {

        checkBtn.disabled = false;
        checkBtn.textContent = "Check Email";
    }
}


checkBtn.addEventListener("click", checkEmail);