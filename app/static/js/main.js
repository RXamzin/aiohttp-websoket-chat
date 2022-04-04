$(document).on('click', '.join_btn', (e) => {
    let name = $('.name_input').val().trim()
    if (name) {
        $('.name_input').prop('disabled', true)
        $(e.target).hide()
        $('.exit_btn').show()
        let ws = create_and_connect_to_websocket()
    }
})

$(document).on('click', '.exit_btn', (e) => {
    $('.name_input').prop('disabled', false)
    $(e.target).hide()
    $('.join_btn').show()
})

/*             <div class="message">
                <strong>USER:</strong>
                <p>Some message</p>
            </div>  */

function create_and_connect_to_websocket() {
    let ws = new WebSocket('ws://' + window.location.host + '/ws')
    return ws
}