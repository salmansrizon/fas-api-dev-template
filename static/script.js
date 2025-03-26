document.getElementById("predictionForm").addEventListener("submit", async (e) => {
    e.preventDefault();
  
    const textInput = document.getElementById("textInput").value;
    const resultDiv = document.getElementById("result");
  
    try {
      const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: textInput }),
      });
  
      const data = await response.json();
      resultDiv.innerHTML = `<strong>Predicted Language:</strong> ${data.language}`;
    } catch (error) {
      resultDiv.innerHTML = "<strong>Error:</strong> Failed to detect language.";
    }
  });