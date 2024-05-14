const toggle_images = (theme) => {
    var light = theme == 'light';
    if (theme == 'auto') {
        light = window.matchMedia('(prefers-color-scheme: light)').matches;
    }
    document.querySelectorAll('.image-light')
        .forEach(image => {
            image.hidden = !light
        });
    document.querySelectorAll('.image-dark')
        .forEach(image => {
            image.hidden = light
        });
}

window.addEventListener('DOMContentLoaded', () => {
    toggle_images(document.documentElement.getAttribute('data-bs-theme'));
    document.querySelectorAll('[data-bs-theme-value]')
        .forEach(toggle => {
            toggle.addEventListener('click', (e) => {
                e.preventDefault();
                toggle_images(toggle.getAttribute('data-bs-theme-value'));
            });
        });
});