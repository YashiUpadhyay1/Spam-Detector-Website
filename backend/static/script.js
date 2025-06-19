function checkSpam() {
  const message = document.getElementById("message").value;

  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: message })
  })
    .then(response => response.json())
    .then(data => {
      const resultEl = document.getElementById("result");
      const alertBox = document.getElementById("customAlert");
      const alertMsg = document.getElementById("alertMessage");

      resultEl.className = "";

      if (data.result.toLowerCase() === "spam") {
        resultEl.innerText = "Result: Spam ❌";
        resultEl.classList.add("result-spam");
        alertMsg.innerText = "⚠️ Warning: This message is SPAM!";
        alertBox.className = "alert-spam";
      } else {
        resultEl.innerText = "Result: Not Spam ✅";
        resultEl.classList.add("result-not-spam");
        alertMsg.innerText = "✅ This message looks safe.";
        alertBox.className = "alert-safe";
      }

      alertBox.style.display = "block";
      setTimeout(() => alertBox.style.display = "none", 5000);
    })
    .catch(error => {
      console.error("Error:", error);
    });
}
