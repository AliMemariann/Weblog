const passwordInput = document.getElementById("password");
const togglePasswordButton = document.getElementById("toggle-password");

togglePasswordButton.addEventListener("click", () => {
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        togglePasswordButton.textContent = "🙈";
    } else {
        passwordInput.type = "password";
        togglePasswordButton.textContent = "👁";
    }
});