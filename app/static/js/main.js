let ws

$(document).on('click', '.join_btn', (e) => {
    let name = $('.name_input').val().trim();
    if (name) {
        $('.name_input').prop('disabled', true);
        $(e.target).hide();
        $('.exit_btn').show();
        $('.send_btn').show();
        $('.msg_input').show();
        ws = create_and_connect_to_websocket(name); // Set ws global
    }
})

$(document).on('click', '.exit_btn', (e) => {
    $('.name_input').prop('disabled', false);
    $(e.target).hide();
    $('.send_btn').hide();
    $('.msg_input').val('');
    $('.msg_input').hide();
    $('.join_btn').show();

    msg = {};
    msg['TYPE'] = 'EXIT';
    msg['USERNAME'] = $('.name_input').val().trim();
    ws.send(JSON.stringify(msg));
})

function create_and_connect_to_websocket(name) {
    ws = new WebSocket('ws://' + window.location.host + '/ws');
    ws.onopen = function () {
        msg = {};
        msg['TYPE'] = 'CONNECTION';
        msg['USERNAME'] = name;
        ws.send(JSON.stringify(msg));
    }
    ws.onmessage = function (event) {
        let msg_data = JSON.parse(event.data);

        let html = '';
        html += '<div class="message">';
        html += `<strong>${msg_data['USERNAME']}:</strong>`;
        html += `<p>${msg_data['MESSAGE']}</p>`;
        html += '</div>';
        $('.chat_div').append(html);
    }
    return ws;
}

$(document).on('click', '.send_btn', (e) => {
    let text = $('.msg_input').val().trim();

    if (text) {
        msg = {};
        msg['TYPE'] = 'MESSAGE';
        msg['USERNAME'] = $('.name_input').val().trim();
        msg['MESSAGE'] = text
        ws.send(JSON.stringify(msg));
        $('.msg_input').val('')

        let html = '';
        html += '<div class="message">';
        html += `<strong>${msg['USERNAME']}:</strong>`;
        html += `<p>${msg['MESSAGE']}</p>`;
        html += '</div>';
        $('.chat_div').append(html);
    }
})