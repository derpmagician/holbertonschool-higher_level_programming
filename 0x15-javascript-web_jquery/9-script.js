const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.get(url, data => $('DIV#hello').html(data.hello));
