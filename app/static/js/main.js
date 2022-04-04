$(document).on('click', '.join_btn', (e) => {
    let name = $('.name_input').val().trim()
    if (name) {
        $('.name_input').prop('disabled', true)
        $(e.target).hide()
        $('.exit_btn').show()
    }
})

$(document).on('click', '.exit_btn', (e) => {
    $('.name_input').prop('disabled', false)
    $(e.target).hide()
    $('.join_btn').show()
})