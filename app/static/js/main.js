$(document).on('click', '.join_btn', (e) => {
    let name = $('.name_input').val().trim()
    if (name) {
        $('.name_input').prop('disabled', true)
        $(e.target).hide()
        $('.exit_btn').show()
        var ws = create_and_connect_to_websocket(name) // Set ws global
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

function create_and_connect_to_websocket(name) {
    let ws = new WebSocket('ws://' + window.location.host + '/ws')
    ws.onopen = function() {
        msg = {}
        msg['TYPE'] = 'CONNECTION'
        msg['USERNAME'] = name
        ws.send(JSON.stringify(msg))
    }
    return ws
}