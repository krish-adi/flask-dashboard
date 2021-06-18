$(document).ready(function() {
    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });

    $('#dismiss, .overlay').on('click', function() {
        $('#sidebar').removeClass('sactive');
        $('.overlay').removeClass('sactive');
    });

    $('#sidebarCollapse').on('click', function() {
        $('#sidebar').addClass('sactive');
        $('.overlay').addClass('sactive');
        $('#sidebar, #page-content').toggleClass('bactive');
    });
});
