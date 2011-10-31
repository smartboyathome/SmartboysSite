input_focused = 'white';
input_unfocused = '#473729';
input_border_focused = '1px solid #190f08';
input_border_unfocused = '1px solid #291a10';
check_focused = '/static/checkmark-focused.png';
check_unfocused = '/static/checkmark-unfocused.png';

function toggleInput(input, onfocus) {
    if(onfocus && (input.value == 'Username' || input.value == 'Password')) {
        input.value = '';
        input.style.color = input_focused;
        input.style.border = input_border_focused;
        document.getElementById('loginbutton').src = check_focused;
    } else if(!onfocus && input.value == '') {
        input.style.color = input_unfocused;
        input.style.border = input_border_unfocused;
        document.getElementById('loginbutton').src = check_unfocused;
        if(input.id == 'username') {
            input.value = 'Username';
        } else if(input.id == 'password') {
            input.value = 'Password';
        }
    }
}

function startup() {
    if(document.getElementById('username') != null) {
        if(document.getElementById('username').value == 'Username') {
            document.getElementById('username').style.color = input_unfocused;
            document.getElementById('username').style.border = input_border_unfocused;
        }
        if(document.getElementById('password').value == 'Password') {
            document.getElementById('password').style.color = input_unfocused;
            document.getElementById('password').style.border = input_border_unfocused;
        }
    }
}

if(window.attachEvent) {
    window.attachEvent('onload', startup);
} else {
    if(window.onload) {
        var curronload = window.onload;
        var newonload = function() {
            curronload();
            startup();
        };
        window.onload = newonload;
    } else {
        window.onload = startup;
    }
}
