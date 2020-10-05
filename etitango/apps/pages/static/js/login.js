const passwordInput = document.getElementById('current-password');
const togglePasswordButton = document.getElementById('toggle-password');

togglePasswordButton.addEventListener('click', togglePassword);

function togglePassword() {
  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    togglePasswordButton.textContent = 'Ocultar contrasena';
    togglePasswordButton.setAttribute('aria-label',
      'Ocultar contrasena');
  } else {
    passwordInput.type = 'password';
    togglePasswordButton.textContent = 'Mostrar contrasena';
    togglePasswordButton.setAttribute('aria-label',
      'Mostrar contrasena ' +
      'ATENCION: esto revelara tu contrasena en la pantalla');
  }
}