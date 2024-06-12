// Clase para manejar la validación de formularios
class FormValidator {
    constructor(form) {
        this.form = form;
        this.inputs = form.querySelectorAll('input, textarea');
        this.init();
    }

    init() {
        this.form.addEventListener('submit', (e) => this.validateForm(e));
        this.inputs.forEach(input => input.addEventListener('input', () => this.clearError(input)));
    }

    validateForm(event) {
        let isValid = true;
        this.inputs.forEach(input => {
            if (!this.validateInput(input)) {
                isValid = false;
            }
        });
        if (!isValid) {
            event.preventDefault();
        }
    }

    validateInput(input) {
        if (input.value.trim() === '') {
            this.showError(input, 'Este campo es obligatorio.');
            return false;
        }
        this.clearError(input);
        return true;
    }

    showError(input, message) {
        let error = input.nextElementSibling;
        if (!error || !error.classList.contains('error')) {
            error = document.createElement('div');
            error.classList.add('error');
            input.parentNode.insertBefore(error, input.nextSibling);
        }
        error.textContent = message;
    }

    clearError(input) {
        const error = input.nextElementSibling;
        if (error && error.classList.contains('error')) {
            error.remove();
        }
    }
}

// Aplicar la validación a todos los formularios en la página
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => new FormValidator(form));
});
