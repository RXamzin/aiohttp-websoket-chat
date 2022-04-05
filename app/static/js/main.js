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

function create_and_connect_to_websocket(name) {
    let ws = new WebSocket('ws://' + window.location.host + '/ws')
    ws.onopen = function() {
        msg = {}
        msg['TYPE'] = 'CONNECTION'
        msg['USERNAME'] = name
        ws.send(JSON.stringify(msg))
    }
    ws.onmessage = function (event) {
        let msg_data = JSON.parse(event.data);

        let html = '';
        html += '<div class="message">';
        html += `<strong>${msg_data['USERNAME']}:</strong>`;
        html += `<p>${msg_data['MESSAGE']}</p>`;
        html += '</div>';
        $('.chat_div').append(html)
      }
    return ws
}

function recieve_msg() {}