//var temaGuardado = localStorage.getItem()



const temaOscuro = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "dark");
    document.querySelector("#dl-icon").setAttribute("class", "bi bi-sun-fill");
    localStorage.setItem("temaSeleccionado", "dark");
};

const temaClaro = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "light");
    document.querySelector("#dl-icon").setAttribute("class", "bi bi-moon-fill");
    localStorage.setItem("temaSeleccionado", "light");
};

const cambiarTema = () => {
    const temaGuardado = localStorage.getItem("temaSeleccionado");
    if (temaGuardado === 'light') {
        temaOscuro();
    } else {
        temaClaro();
    }
};

document.addEventListener("DOMContentLoaded", () => {
    const temaGuardado = localStorage.getItem("temaSeleccionado");
    if (temaGuardado === 'light') {
        temaClaro(); // Cambiar tema a claro si estaba seleccionado
    } else {
        temaOscuro(); // Por defecto, mantener el tema oscuro
    }
});
