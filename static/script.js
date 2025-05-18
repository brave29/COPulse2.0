document.querySelectorAll('input[name="digitaltwin"]').forEach((elem) => {
  elem.addEventListener("change", function(event) {
    const manualEntrySection = document.getElementById("manual-entry");
    if (event.target.value === "No") {
      manualEntrySection.style.display = "block";
    } else {
      manualEntrySection.style.display = "none";
    }
  });
});
