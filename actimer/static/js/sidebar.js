$(document).ready(function setColourForSelectedSidebarChapter() {
    selectedChapter = String(document.URL.split('/')[3]);
    if (selectedChapter == '') {
        selectedChapter = 'timers'
    }
    $('#' + selectedChapter).addClass('active-page');
})


const sidebar = document.querySelector('#sidebar');
const sidebarButton = document.querySelector('#sidebar-button');
const sidebarButtonImg = document.querySelector('#sidebar-button-img');

sidebarButton.onclick = () => {
    if (sidebar.classList.toggle('open')) {
        sidebarButtonImg.src = "../../static/icons/sidebar/close-button.svg";
    } else {
        sidebarButtonImg.src = "../../static/icons/sidebar/open-button.svg";
    }
}