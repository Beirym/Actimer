function changePage(new_page) {
    href = window.location.href.split('?')[0];
    window.history.pushState(state="", unused="", url=href+'?page={0}'.f(new_page));
}